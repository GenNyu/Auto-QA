#!/usr/bin/env python3
"""
Auto-QA — công cụ đánh giá chất lượng trả lời của chatbot.

Cách gọn nhất là dùng `just` (không cần activate môi trường ảo):

    just new tai_lieu/     # tạo bộ đánh giá mới từ một thư mục tài liệu
    just run iso27001      # chạy trọn 4 bước rồi mở báo cáo
    just list              # xem có những bộ đánh giá nào
    just check             # kiểm tra máy đã cài đủ chưa

Chạy từng bước riêng khi cần:

    just gen    iso27001   # 1. sinh câu hỏi từ tài liệu
    just ask    iso27001   # 2. hỏi chatbot, thu câu trả lời
    just score  iso27001   # 3. chấm điểm từng câu trả lời
    just report iso27001   # 4. dựng lại báo cáo HTML

Không có `just` thì gọi thẳng, nhớ dùng Python trong môi trường ảo:

    .venv/bin/python qa.py run iso27001
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path
from typing import List, Optional

from core.env import PROJECT_ROOT, load_env_file, resolve_api_key
from core.project import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_CHAT_URL,
    PROJECTS_DIR,
    ProjectConfig,
    ProjectError,
    list_projects,
    load_project,
)

PYTHON = sys.executable


# ─────────────────────────────────────────────
# TRÌNH BÀY
# ─────────────────────────────────────────────

def hint(command: str) -> str:
    """Gợi ý lệnh, viết theo đúng cách người dùng đang gọi công cụ này."""
    if shutil.which("just") and (PROJECT_ROOT / "justfile").exists():
        return f"just {command}"
    return f"{PYTHON} qa.py {command}"


def step(number: int, total: int, title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  Bước {number}/{total} · {title}")
    print(f"{'─' * 60}")


def fail(message: str) -> int:
    print(f"\n❌ {message}")
    return 1


def llm_flags(project: ProjectConfig) -> List[str]:
    """Cờ LLM dùng chung cho cả bước sinh câu hỏi và bước chấm điểm,
    để hai bước luôn đi qua cùng một gateway và cùng một model."""
    flags: List[str] = []
    if project.model:
        flags += ["--model", project.model]
    if project.base_url:
        flags += ["--base-url", project.base_url]
    return flags


def run_command(command: List[str], env: Optional[dict] = None) -> int:
    """Chạy một lệnh con, trả về exit code."""
    merged = {**os.environ, **(env or {})}
    return subprocess.call(command, cwd=str(PROJECT_ROOT), env=merged)


# ─────────────────────────────────────────────
# CÁC BƯỚC
# ─────────────────────────────────────────────

def do_gen(project: ProjectConfig, force: bool = False) -> int:
    """Bước 1 — sinh câu hỏi từ tài liệu nguồn."""
    source = PROJECT_ROOT / project.source
    if not source.exists():
        return fail(f"Không tìm thấy tài liệu nguồn: {project.source}")

    project.run_dir.mkdir(parents=True, exist_ok=True)
    command = [
        PYTHON, "script.py",
        "--input", project.source,
        "--output", str(project.questions_file),
        "--no-timestamp",
        "--num-questions", str(project.questions),
        "--provider", project.provider,
    ]
    if force:
        command.append("--force")
    command += llm_flags(project)

    code = run_command(command)
    if code != 0:
        return fail("Bước sinh câu hỏi thất bại.")
    return 0


def do_ask(project: ProjectConfig) -> int:
    """Bước 2 — hỏi chatbot và thu câu trả lời."""
    if not project.questions_file.exists():
        return fail(
            f"Chưa có câu hỏi. Chạy trước:  {hint(f'gen {project.key}')}"
        )
    if not (PROJECT_ROOT / project.spec).exists():
        return fail(f"Không tìm thấy kịch bản chatbot: {project.spec}")

    code = run_command(
        ["npx", "playwright", "test", project.spec],
        env={
            "QA_INPUT": str(project.questions_file),
            "QA_OUTPUT": str(project.answers_file),
            "QA_MAX_PER_SESSION": str(project.batch_size),
            "CHAT_MODEL": project.resolved_chat_model(),
            "CHAT_URL": project.resolved_chat_url(),
        },
    )
    if code != 0:
        return fail("Bước hỏi chatbot thất bại. Xem log phía trên để biết lý do.")
    return 0


def do_score(project: ProjectConfig) -> int:
    """Bước 3 — chấm điểm từng câu trả lời."""
    if not project.answers_file.exists():
        return fail(
            f"Chưa có câu trả lời. Chạy trước:  {hint(f'ask {project.key}')}"
        )

    command = [
        PYTHON, "evaluate.py",
        "--input", str(project.answers_file),
        "--provider", project.provider,
    ]
    command += llm_flags(project)

    kb_dir = project.resolved_kb_dir()
    if kb_dir:
        command += ["--kb-dir", kb_dir]
    if not project.deep_check:
        command += ["--no-pass2"]

    code = run_command(command)
    if code != 0:
        return fail("Bước chấm điểm thất bại.")
    return 0


def do_report(project: ProjectConfig, open_browser: bool = True) -> int:
    """Bước 4 — dựng báo cáo HTML."""
    from core.report import build_report

    if not project.scored_file.exists():
        return fail(
            f"Chưa có kết quả chấm điểm. Chạy trước:  {hint(f'score {project.key}')}"
        )

    data = json.loads(project.scored_file.read_text(encoding="utf-8"))
    build_report(project, data, project.report_file)

    print(f"\n📄 Báo cáo: {project.report_file}")
    if open_browser:
        webbrowser.open(project.report_file.as_uri())
    return 0


def do_run(project: ProjectConfig) -> int:
    """Chạy trọn cả 4 bước."""
    print(f"\n🚀 {project.name}  ·  {project.questions} câu hỏi")
    print(f"   Tài liệu : {project.source}")
    print(f"   Chatbot  : {project.resolved_chat_model()}  ·  {project.resolved_chat_url()}")
    print(f"   Kết quả  : {project.run_dir.relative_to(PROJECT_ROOT)}/")

    step(1, 4, "Sinh câu hỏi từ tài liệu")
    if do_gen(project) != 0:
        return 1

    step(2, 4, "Hỏi chatbot và thu câu trả lời")
    if do_ask(project) != 0:
        return 1

    step(3, 4, "Chấm điểm từng câu trả lời")
    if do_score(project) != 0:
        return 1

    step(4, 4, "Dựng báo cáo")
    return do_report(project)


# ─────────────────────────────────────────────
# CHẨN ĐOÁN
# ─────────────────────────────────────────────

def do_check() -> int:
    """Kiểm tra máy đã sẵn sàng chạy chưa."""
    print("\nKiểm tra môi trường\n" + "─" * 60)
    problems: List[str] = []

    def report(label: str, ok: bool, detail: str, fix: str = "") -> None:
        print(f"  {'✅' if ok else '❌'}  {label:<26} {detail}")
        if not ok and fix:
            problems.append(fix)

    report("Python", True, sys.version.split()[0])

    try:
        import yaml  # noqa: F401
        report("Thư viện Python", True, "đã cài đủ")
    except ImportError:
        report("Thư viện Python", False, "thiếu PyYAML",
               "pip install -r requirements.txt")

    node = shutil.which("npx")
    report("Node / npx", bool(node), node or "chưa cài",
           "Cài Node.js: https://nodejs.org")

    playwright_ok = (PROJECT_ROOT / "node_modules" / "@playwright").is_dir()
    report("Playwright", playwright_ok,
           "đã cài" if playwright_ok else "chưa cài",
           "npm install && npx playwright install chromium")

    env_path = PROJECT_ROOT / ".env"
    report("File .env", env_path.exists(),
           str(env_path.name) if env_path.exists() else "chưa có",
           "cp .env.example .env  rồi điền thông tin")

    load_env_file()
    for key in ("CHAT_EMAIL", "CHAT_PASSWORD"):
        report(f"  {key}", bool(os.getenv(key)),
               "đã có" if os.getenv(key) else "chưa điền",
               f"Điền {key} vào file .env")

    # Hai trường này luôn có giá trị dùng được, nên chỉ hiện ra để đối chiếu
    # với những gì thấy trên giao diện chat.
    for key, fallback in (("CHAT_URL", DEFAULT_CHAT_URL), ("CHAT_MODEL", DEFAULT_CHAT_MODEL)):
        value = os.getenv(key)
        report(f"  {key}", True, value or f"{fallback}  (mặc định)")

    projects = list_projects()
    report("Bộ đánh giá", bool(projects),
           ", ".join(projects) if projects else "chưa có",
           "Tạo file projects/<tên>.yaml")

    for key in projects:
        try:
            project = load_project(key)
        except ProjectError:
            report(f"  {key}", False, "file cấu hình lỗi", f"Sửa projects/{key}.yaml")
            continue
        has_key = bool(resolve_api_key(project.provider))
        report(f"  {key}", has_key,
               f"provider={project.provider}" + ("" if has_key else " · thiếu API key"),
               f"Điền {project.provider.upper()}_API_KEY vào file .env")

    print("─" * 60)
    if problems:
        print("\nCần xử lý:")
        for item in dict.fromkeys(problems):
            print(f"   • {item}")
        return 1

    print(f"\n✅ Mọi thứ đã sẵn sàng. Chạy:  {hint('run <tên bộ đánh giá>')}")
    return 0


# ─────────────────────────────────────────────
# TẠO BỘ ĐÁNH GIÁ MỚI
# ─────────────────────────────────────────────

# Mật độ câu hỏi: ~1 câu cho mỗi ngần này ký tự tài liệu.
# Dày hơn thì các câu hỏi bắt đầu lặp ý, vì tài liệu hết chỗ để hỏi.
CHARS_PER_QUESTION = 250
MIN_QUESTIONS = 8
MAX_QUESTIONS = 30

# Giống hệt resolve_input_paths() trong script.py, để số liệu đếm ra đúng bằng
# số file bước sinh câu hỏi thật sự đọc.
SOURCE_SUFFIXES = (".md", ".txt")


def scan_source_files(folder: Path) -> List[Path]:
    """Các file tài liệu bước sinh câu hỏi sẽ đọc trong thư mục này."""
    return [
        f for f in sorted(folder.iterdir())
        if f.is_file() and f.suffix in SOURCE_SUFFIXES and not f.name.startswith("_")
    ]


def suggest_questions(files: List[Path]) -> int:
    """Số câu hỏi mỗi file, suy từ độ dài trung bình của tài liệu."""
    if not files:
        return 20
    sizes = [f.stat().st_size for f in files]
    average = sum(sizes) / len(sizes)
    return max(MIN_QUESTIONS, min(MAX_QUESTIONS, round(average / CHARS_PER_QUESTION)))


def slugify(text: str) -> str:
    """Tên thư mục → tên project: chỉ chữ thường, số và gạch dưới."""
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return slug or "bo_danh_gia"


def do_new(folder_arg: str, key: Optional[str], force: bool) -> int:
    """Đọc một thư mục tài liệu rồi viết sẵn file projects/<tên>.yaml."""
    folder = Path(folder_arg)
    if not folder.is_absolute():
        folder = PROJECT_ROOT / folder
    folder = folder.resolve()

    if not folder.is_dir():
        return fail(f"Không tìm thấy thư mục tài liệu: {folder_arg}")

    try:
        source = str(folder.relative_to(PROJECT_ROOT)) + "/"
    except ValueError:
        return fail(
            f"Thư mục nằm ngoài dự án: {folder}\n"
            f"   Chép tài liệu vào trong {PROJECT_ROOT.name}/ rồi chạy lại."
        )

    files = scan_source_files(folder)
    if not files:
        return fail(
            f"Thư mục {source} không có file .md hoặc .txt nào.\n"
            f"   (file bắt đầu bằng dấu _ bị bỏ qua)"
        )

    key = slugify(key or folder.name)
    path = PROJECTS_DIR / f"{key}.yaml"
    if path.exists() and not force:
        return fail(
            f"Đã có {path.relative_to(PROJECT_ROOT)}.\n"
            f"   Sửa thẳng file đó, hoặc ghi đè:  {hint(f'new {folder_arg} {key} --force')}"
        )

    questions = suggest_questions(files)
    total_chars = sum(f.stat().st_size for f in files)
    average = total_chars // len(files)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""# {key} — sinh tự động từ {source}
# Sửa thoải mái, mọi trường đều có mặc định. Xem README mục 4.

name: {folder.name}
source: {source}

# {len(files)} file · trung bình {average:,} ký tự/file
# → ~1 câu hỏi cho mỗi {CHARS_PER_QUESTION} ký tự. Tăng lên nếu thấy câu hỏi còn thưa,
#   giảm xuống nếu thấy nhiều câu hỏi trùng ý nhau.
questions: {questions}

chatbot:
  # Trang chat và model lấy theo CHAT_URL / CHAT_MODEL trong .env.
  # Chỉ khai ở đây khi bộ này cần chạy khác với phần còn lại:
  #   url: "https://chat.urbox.dev/"
  #   model: "ENGR Test1"
  batch_size: 10           # khởi động lại trình duyệt sau mỗi N câu

scoring:
  threshold: 6             # từ mấy điểm trở lên là ĐẠT
  deep_check: true         # đối chiếu lại tài liệu gốc khi cần

llm:
  # Bỏ trống model/base_url thì lấy theo OPENAI_MODEL / OPENAI_BASE_URL trong .env
  provider: openai
""",
        encoding="utf-8",
    )

    print(f"\n✅ Đã tạo {path.relative_to(PROJECT_ROOT)}")
    print("─" * 60)
    print(f"  Tài liệu   {len(files)} file · {total_chars:,} ký tự · trung bình {average:,}/file")
    print(f"  Câu hỏi    {questions} câu/file  →  khoảng {questions * len(files):,} câu tổng cộng")
    print(f"  Chatbot    {os.getenv('CHAT_MODEL') or DEFAULT_CHAT_MODEL}"
          f"  ·  {os.getenv('CHAT_URL') or DEFAULT_CHAT_URL}   (theo .env)")
    print("─" * 60)
    print(f"\nXem lại file rồi chạy:  {hint(f'run {key}')}")
    print(f"Đã có sẵn bộ câu hỏi thì bỏ qua bước sinh — xem README mục 4.")
    return 0


def do_list() -> int:
    projects = list_projects()
    if not projects:
        print("\nChưa có bộ đánh giá nào. Tạo một file trong thư mục projects/.")
        return 0

    print("\nCác bộ đánh giá hiện có\n" + "─" * 60)
    for key in projects:
        try:
            project = load_project(key)
        except ProjectError as exc:
            print(f"  {key:<14} ⚠️  {exc}")
            continue
        done = "  ✔ đã có báo cáo" if project.report_file.exists() else ""
        print(f"  {key:<14} {project.name}  ·  {project.questions} câu  ·  {project.source}{done}")
    print("─" * 60)
    print(f"\nChạy:  {hint('run <tên>')}")
    return 0


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="qa.py",
        description="Đánh giá chất lượng trả lời của chatbot.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command")

    for name, help_text in [
        ("run", "Chạy trọn 3 bước rồi mở báo cáo"),
        ("ask", "Chỉ hỏi chatbot"),
        ("score", "Chỉ chấm điểm"),
        ("report", "Chỉ dựng lại báo cáo"),
    ]:
        p = sub.add_parser(name, help=help_text)
        p.add_argument("project", help=f"Tên bộ đánh giá (xem: {hint('list')})")

    # gen has extra --force flag
    p_gen = sub.add_parser("gen", help="Chỉ sinh câu hỏi")
    p_gen.add_argument("project", help=f"Tên bộ đánh giá (xem: {hint('list')})")
    p_gen.add_argument("--force", action="store_true", help="Xoá cache và regenerate tất cả")

    sub.add_parser("list", help="Liệt kê các bộ đánh giá")
    sub.add_parser("check", help="Kiểm tra máy đã cài đủ chưa")

    p_new = sub.add_parser("new", help="Tạo bộ đánh giá mới từ một thư mục tài liệu")
    p_new.add_argument("folder", help="Thư mục chứa tài liệu .md/.txt")
    p_new.add_argument("name", nargs="?", help="Tên bộ đánh giá (mặc định: tên thư mục)")
    p_new.add_argument("--force", action="store_true", help="Ghi đè file cấu hình đã có")
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0
    if args.command == "check":
        return do_check()

    load_env_file()
    if args.command == "list":
        return do_list()
    if args.command == "new":
        return do_new(args.folder, args.name, args.force)

    try:
        project = load_project(args.project)
    except ProjectError as exc:
        return fail(str(exc))

    return {
        "run": do_run,
        "gen": lambda p: do_gen(p, getattr(args, 'force', False)),
        "ask": do_ask,
        "score": do_score,
        "report": do_report,
    }[args.command](project)


if __name__ == "__main__":
    sys.exit(main())
