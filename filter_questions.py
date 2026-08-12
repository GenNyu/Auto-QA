"""
Script để filter dataset RAG evaluation bằng cách loại bỏ những câu hỏi không rõ context.
Có thể sử dụng như standalone filter hoặc tích hợp vào generate pipeline.
"""
import json
import argparse
from pathlib import Path
from typing import Optional
from core.validate import filter_questions, FilterConfig, ValidationReason, QuestionValidator


def load_qa_dataset(filepath: str) -> list:
    """Load dataset từ JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_qa_dataset(data: list, filepath: str):
    """Save dataset ra JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def print_statistics(stats: dict):
    """In ra thống kê chi tiết."""
    print("\n" + "="*60)
    print("📊 THỐNG KÊ FILTERING")
    print("="*60)
    print(f"✅ Tổng câu hỏi: {stats['total']}")
    print(f"✅ Câu hỏi hợp lệ: {stats['valid']} ({stats['valid']/max(stats['total'], 1)*100:.1f}%)")
    print(f"❌ Câu hỏi bị loại: {stats['rejected']} ({stats['rejected']/max(stats['total'], 1)*100:.1f}%)")
    
    if stats['by_reason']:
        print("\n📋 Chi tiết loại bỏ:")
        for reason, count in sorted(stats['by_reason'].items(), key=lambda x: x[1], reverse=True):
            pct = count / max(stats['rejected'], 1) * 100
            print(f"   • {reason}: {count} ({pct:.1f}%)")
    
    print("="*60 + "\n")


def validate_and_report(qa_pairs: list, output_report: Optional[str] = None):
    """Validate tất cả câu hỏi và tạo report chi tiết."""
    validator = QuestionValidator()
    rejected_samples = {reason.value: [] for reason in ValidationReason}
    
    for pair in qa_pairs:
        question = pair.get("question", "")
        chunk = pair.get("chunk", "")
        result = validator.validate(question, chunk)
        
        if not result.is_valid:
            rejected_samples[result.reason.value].append({
                "question": question,
                "chunk": chunk[:100] + "..." if len(chunk) > 100 else chunk,
                "file": pair.get("file", ""),
                "details": result.details
            })
    
    # Print report
    print("\n" + "="*80)
    print("🔍 BÁO CÁO CHI TIẾT CÁC CÂU HỎI BỊ LOẠI")
    print("="*80)
    
    for reason, samples in rejected_samples.items():
        if samples:
            print(f"\n❌ {reason} ({len(samples)} câu hỏi)")
            print("-" * 80)
            for i, sample in enumerate(samples[:3], 1):  # Hiển thị 3 mẫu đầu tiên
                print(f"\n   Mẫu {i}:")
                print(f"   Q: {sample['question']}")
                print(f"   File: {sample['file']}")
                print(f"   Chunk: {sample['chunk']}")
                print(f"   Lý do: {sample['details']}")
            
            if len(samples) > 3:
                print(f"\n   ... và {len(samples) - 3} câu hỏi khác")
    
    print("\n" + "="*80 + "\n")
    
    # Save report
    if output_report:
        with open(output_report, 'w', encoding='utf-8') as f:
            json.dump(rejected_samples, f, ensure_ascii=False, indent=2)
        print(f"✅ Report đã được lưu: {output_report}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Filter dataset RAG evaluation bằng cách loại bỏ câu hỏi vô nghĩa"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Đường dẫn file JSON input (dataset RAG evaluation)"
    )
    parser.add_argument(
        "--output",
        default="rag_eval_filtered.json",
        help="Đường dẫn file JSON output (default: rag_eval_filtered.json)"
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Đường dẫn file report chi tiết (optional)"
    )
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.7,
        help="Mức confidence tối thiểu để accept câu hỏi (0.0-1.0, default: 0.7)"
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        default=None,
        help="Các loại câu hỏi cần loại bỏ (metadata_metric, generic_purpose, ...)"
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Hiển thị preview những câu hỏi bị loại (không lưu file)"
    )
    
    args = parser.parse_args()
    
    # Load data
    print(f"📂 Loading dataset từ {args.input}...")
    qa_pairs = load_qa_dataset(args.input)
    print(f"✅ Loaded {len(qa_pairs)} QA pairs\n")
    
    # Cấu hình filter
    exclude_reasons = None
    if args.exclude:
        # Map string names sang enum
        exclude_reasons = []
        reason_map = {r.value: r for r in ValidationReason}
        for exc in args.exclude:
            if exc in reason_map:
                exclude_reasons.append(reason_map[exc])
    
    config = FilterConfig(
        min_confidence=args.min_confidence,
        exclude_reasons=exclude_reasons
    )
    
    # Filter
    print(f"🔍 Filtering câu hỏi...")
    filtered_pairs, stats = filter_questions(qa_pairs, config=config)
    
    # Print statistics
    print_statistics(stats)
    
    # Validate và report
    if args.preview or args.report:
        validate_and_report(qa_pairs, args.report)
    
    # Save
    if not args.preview:
        save_qa_dataset(filtered_pairs, args.output)
        print(f"💾 Saved {len(filtered_pairs)} câu hỏi hợp lệ -> {args.output}")
    else:
        print(f"🔍 Preview mode: không lưu file")


if __name__ == "__main__":
    main()