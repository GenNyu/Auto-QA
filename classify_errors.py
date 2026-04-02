
import json
import argparse
import os
from typing import List, Optional, Dict
from pathlib import Path
from config import (
    DEFAULT_PROVIDER, 
    PROVIDER_KIND_MAP, 
    OLLAMA_TIMEOUT,
    DEFAULT_OLLAMA_URL,
    DEFAULT_OLLAMA_MODEL
)
from providers.factory import create_provider

# Thử import các hàm hỗ trợ từ evaluate nếu có, nếu không thì tự định nghĩa
try:
    from evaluate import resolve_api_key, normalize_provider_name
except ImportError:
    def normalize_provider_name(name: str) -> str:
        return name.lower().strip()
    
    def resolve_api_key(provider_name: str, api_key: Optional[str] = None) -> Optional[str]:
        if api_key:
            return api_key
        env_var = f"{provider_name.upper()}_API_KEY"
        return os.getenv(env_var)

def load_env_file():
    """Đọc file .env đơn giản"""
    env_path = Path("document-qa-pipeline/.env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                parts = line.split("=", 1)
                if len(parts) == 2:
                    key, value = parts
                    os.environ[key.strip()] = value.strip()


def ensure_parent_dir(path: str) -> None:
    """Ensure parent directory exists for a file path."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def resolve_env_override(provider_name: str, suffix: str) -> Optional[str]:
    """Resolve provider-specific env overrides (e.g., OPENAI_MODEL, OPENAI_BASE_URL)."""
    env_key = f"{provider_name.upper()}_{suffix}"
    return os.getenv(env_key)

# Định nghĩa 3 nhóm lỗi theo đúng yêu cầu của bạn
ERROR_CATEGORIES = {
    "INFORMATION_INACCURACY": "Information Inaccuracy",
    "SOURCE_RETRIEVAL_ERROR": "Source Retrieval Error",
    "MISSING_INFORMATION": "Missing Information"
}

CLASSIFY_SYSTEM_PROMPT = f"""
Bạn là chuyên gia phân tích hệ thống RAG. Nhiệm vụ của bạn là phân loại các lỗi "incorrect" vào 3 nhóm sau:

1. "{ERROR_CATEGORIES['SOURCE_RETRIEVAL_ERROR']}":
   - Dấu hiệu: Tên file gốc (trường 'file') KHÔNG xuất hiện trong danh sách các file 'source'.
   - LƯU Ý: Tên file source có thể thêm mã hash (ví dụ: _hlvvapw1) hoặc khác biệt ký tự đặc biệt (chấm, gạch dưới) nhưng nếu tên chính khớp nhau thì vẫn coi là CÙNG 1 FILE.

2. "{ERROR_CATEGORIES['MISSING_INFORMATION']}":
   - Dấu hiệu: File gốc CÓ trong danh sách 'source', nội dung 'chunk' CÓ chứa câu trả lời đúng, nhưng 'answer' lại nói "không có thông tin", "không tìm thấy", "xin lỗi".

3. "{ERROR_CATEGORIES['INFORMATION_INACCURACY']}":
   - Dấu hiệu: Hệ thống tìm đúng file, LLM có trả lời nhưng dữ liệu trong 'answer' bị SAI (sai con số, sai danh mục, sai tên người) so với 'chunk'.

LƯU Ý: Nếu người dùng báo rằng file đã được tìm thấy (CÓ TRONG danh sách Sources), tuyệt đối KHÔNG ĐƯỢC chọn nhóm 1.

Hãy trả về kết quả dưới định dạng JSON duy nhất:
{{
  "error_type": "Tên nhóm lỗi",
  "reasoning": "Giải thích ngắn gọn tại sao chọn nhóm này (tiếng Việt)"
}}
"""

def get_bar(count: int, max_count: int, width: int = 40) -> str:
    if max_count == 0: return ""
    return "█" * int(count * width / max_count)

def print_all_stats(total: int, eval_stats: Dict, score_dist: Dict, error_stats: Dict):
    """In đầy đủ cả Evaluation Summary và Error Classification"""
    avg_score = eval_stats['total_score'] / total if total > 0 else 0
    
    print("\nEvaluation Summary:")
    print(f"   Total      : {total}")
    print(f"   Correct    : {eval_stats['correct']:3d} ({eval_stats['correct']/total*100:5.1f}%) [score ≥ 6]")
    print(f"   Unclear    : {eval_stats['unclear']:3d} ({eval_stats['unclear']/total*100:5.1f}%) [score = 5]")
    print(f"   Incorrect  : {eval_stats['incorrect']:3d} ({eval_stats['incorrect']/total*100:5.1f}%) [score ≤ 4]")
    print(f"   Error      : {eval_stats['error']:3d} ({eval_stats['error']/total*100:5.1f}%)")
    print(f"   Avg Score  : {avg_score:.2f}/10")

    print("\nScore Distribution:")
    max_dist = max(score_dist.values()) if score_dist else 0
    for s in range(10, 0, -1):
        count = score_dist.get(s, 0)
        bar = get_bar(count, max_dist)
        print(f"   {s:2d}: {count:3d} {bar}")

    print("\n" + "="*80)
    print("📊 THỐNG KÊ PHÂN LOẠI LỖI (ERROR CLASSIFICATION)")
    print("="*80)
    incorrect_total = eval_stats['incorrect']
    print(f"{'Error Category':25} | {'Count':5} | {'% of Incorrect':15} | {'% of Total':10}")
    print("-" * 80)
    
    for err_name in ERROR_CATEGORIES.values():
        count = error_stats.get(err_name, 0)
        p_incorrect = (count / incorrect_total * 100) if incorrect_total > 0 else 0
        p_total = (count / total * 100) if total > 0 else 0
        print(f"{err_name:25} | {count:5d} | {p_incorrect:13.1f}% | {p_total:9.1f}%")
    
    unknown_count = error_stats.get("Unknown", 0)
    if unknown_count > 0:
        p_total_unk = (unknown_count / total * 100) if total > 0 else 0
        print(f"{'Unknown/Error':25} | {unknown_count:5d} | {'-':13} | {p_total_unk:9.1f}%")
    print("="*80 + "\n")

def classify_errors(input_path: str, output_path: str, provider_name: str, api_key_arg: str = None, base_url: str = None, model: str = None):
    load_env_file()
    
    if not os.path.exists(input_path):
        print(f"Lỗi: Không tìm thấy file {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    last_bracket = content.rfind(']')
    if last_bracket != -1:
        content = content[:last_bracket + 1]

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Lỗi khi parse JSON: {e}")
        return

    p_name = normalize_provider_name(provider_name)
    api_key = resolve_api_key(p_name, api_key_arg)
    env_base_url = resolve_env_override(p_name, "BASE_URL")
    env_model = resolve_env_override(p_name, "MODEL")

    try:
        provider = create_provider(
            provider_name=p_name,
            api_key=api_key,
            ollama_url=os.getenv("OLLAMA_URL", DEFAULT_OLLAMA_URL),
            ollama_model=os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL),
            ollama_timeout=OLLAMA_TIMEOUT,
            base_url=base_url or env_base_url,
            model=model or env_model
        )
    except Exception as e:
        print(f"❌ Lỗi khởi tạo provider: {e}")
        return

    # Statistics containers
    eval_stats = {"correct": 0, "incorrect": 0, "unclear": 0, "error": 0, "total_score": 0}
    score_dist = {i: 0 for i in range(1, 11)}
    error_stats = {name: 0 for name in ERROR_CATEGORIES.values()}
    error_stats["Unknown"] = 0
    
    results = []
    total = len(data)

    print(f"--- Bắt đầu phân loại lỗi cho {total} mục ---")

    for idx, entry in enumerate(data, 1):
        score = entry.get("score", 0)
        eval_label = entry.get("evaluate", "error")
        
        # Update evaluation stats
        eval_stats[eval_label] += 1
        eval_stats["total_score"] += score
        if 1 <= score <= 10:
            score_dist[score] += 1

        if eval_label == "incorrect":
            # Classification logic
            def norm(name: str) -> str:
                # Xóa .md và các ký tự đặc biệt, chỉ giữ chữ và số
                clean = name.lower().replace(".md", "")
                return "".join(c for c in clean if c.isalnum())

            target_file = entry.get("file", "")
            target_norm = norm(target_file)
            sources = entry.get("source", [])
            
            is_retrieval_error = True
            for s in sources:
                if target_norm in norm(s):
                    is_retrieval_error = False
                    break
            
            if is_retrieval_error:
                err_type = ERROR_CATEGORIES["SOURCE_RETRIEVAL_ERROR"]
                entry["error_classification"] = {
                    "error_type": err_type,
                    "reasoning": f"File gốc '{target_file}' không xuất hiện trong danh sách source truy vấn được."
                }
                error_stats[err_type] += 1
                print(f"[{idx}] {err_type}")
            else:
                # Nếu Code đã tìm thấy file, dặn LLM KHÔNG ĐƯỢC chọn Retrieval Error
                user_prompt = f"""
                LƯU Ý: Tôi đã kiểm tra và xác nhận file gốc '{target_file}' CÓ TRONG danh sách Sources Found (có thể khác dấu chấm/gạch dưới hoặc thêm mã hash). 
                VÌ VẬY, TUYỆT ĐỐI KHÔNG ĐƯỢC PHÂN LOẠI LÀ 'Source Retrieval Error'.

                Question: {entry.get('question')}
                Target File: {target_file}
                Sources Found: {entry.get('source')}
                Chunk Content: {entry.get('chunk')}
                LLM Answer: {entry.get('answer')}
                Scorer Check: {entry.get('check')}
                """
                try:
                    messages = [{"role": "system", "content": CLASSIFY_SYSTEM_PROMPT}, {"role": "user", "content": user_prompt}]
                    response = provider.chat(messages=messages, temperature=0.0)
                    clean_res = response.strip()
                    if "```json" in clean_res: clean_res = clean_res.split("```json")[1].split("```")[0].strip()
                    elif "```" in clean_res: clean_res = clean_res.split("```")[1].split("```")[0].strip()
                    
                    classification = json.loads(clean_res)
                    entry["error_classification"] = classification
                    err_type = classification.get("error_type")
                    if err_type in error_stats: error_stats[err_type] += 1
                    else: error_stats["Unknown"] += 1
                    print(f"[{idx}] {err_type}")
                except Exception as e:
                    print(f"Lỗi tại mục {idx}: {e}")
                    entry["error_classification"] = {"error_type": "Unknown", "reasoning": str(e)}
                    error_stats["Unknown"] += 1
        
        results.append(entry)

    # In thống kê đầy đủ
    print_all_stats(total, eval_stats, score_dist, error_stats)

    # Lưu kết quả
    ensure_parent_dir(output_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        # Ghi summary vào cuối file (Extra data)
        f.write("\n\n/* Evaluation Summary:\n")
        f.write(f"   Total      : {total}\n")
        f.write(f"   Correct    : {eval_stats['correct']} [score ≥ 6]\n")
        f.write(f"   Incorrect  : {eval_stats['incorrect']} [score ≤ 4]\n")
        f.write(f"   Avg Score  : {eval_stats['total_score']/total if total>0 else 0:.2f}/10\n\n")
        f.write("📊 THỐNG KÊ PHÂN LOẠI LỖI\n")
        for name, count in error_stats.items():
            if count > 0: f.write(f"{name:25}: {count}\n")
        f.write("*/\n")

    print(f"Hoàn thành! Kết quả tại {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/kb/KB_output_semantic_scored.json")
    parser.add_argument("--output", default="outputs/kb/KB_output_classified.json")
    parser.add_argument("--provider", default=DEFAULT_PROVIDER)
    parser.add_argument("--api-key", help="API Key")
    parser.add_argument("--base-url", help="Custom API Base URL")
    parser.add_argument("--model", help="Model name")
    args = parser.parse_args()
    classify_errors(args.input, args.output, args.provider, args.api_key, args.base_url, args.model)
