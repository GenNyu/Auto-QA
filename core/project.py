"""
Project configuration: one YAML file per document set, under projects/.

A project holds every setting a run needs, so the CLI stays a single command.
Every field has a default; a minimal project file only needs `source`.
"""
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from core.env import PROJECT_ROOT

PROJECTS_DIR = PROJECT_ROOT / "projects"
RUNS_DIR = PROJECT_ROOT / "runs"

# Dùng khi cả YAML lẫn .env đều không khai. Trùng với mặc định trong tests/KB.spec.ts.
DEFAULT_CHAT_URL = "https://chat.urbox.dev/"
DEFAULT_CHAT_MODEL = "ENGR Test1"


class ProjectError(Exception):
    """Raised when a project file is missing or malformed."""


@dataclass(frozen=True)
class ProjectConfig:
    """Everything one evaluation run needs."""

    key: str                      # file stem, e.g. "iso27001"
    name: str                     # human label, e.g. "ISO 27001"
    source: str                   # document folder or file to generate questions from
    questions: int = 25

    # Chatbot step
    spec: str = "tests/KB.spec.ts"
    # Bỏ trống trong YAML thì lấy theo CHAT_URL / CHAT_MODEL trong .env.
    # Trang chat và model là thứ của cả máy, không phải của riêng một bộ đánh giá,
    # nên chỗ ở tự nhiên của chúng là .env; YAML chỉ dùng khi cần chạy khác đi.
    chat_url: Optional[str] = None
    chat_model: Optional[str] = None
    batch_size: int = 10

    # Scoring step
    threshold: int = 6
    deep_check: bool = True
    kb_dir: Optional[str] = None  # defaults to `source` when it is a folder

    # LLM used for generating and scoring
    provider: str = "openai"
    model: Optional[str] = None
    base_url: Optional[str] = None   # gateway của công ty; bỏ trống = API chính thức

    @property
    def run_dir(self) -> Path:
        return RUNS_DIR / self.key

    @property
    def questions_file(self) -> Path:
        return self.run_dir / "questions.json"

    @property
    def answers_file(self) -> Path:
        return self.run_dir / "answers.json"

    @property
    def scored_file(self) -> Path:
        # Matches how evaluate.py names its output.
        return self.run_dir / "answers_semantic_scored.json"

    @property
    def report_file(self) -> Path:
        return self.run_dir / "report.html"

    def resolved_chat_url(self) -> str:
        """Trang chatbot sẽ mở: YAML > .env (CHAT_URL) > mặc định."""
        return self.chat_url or os.getenv("CHAT_URL") or DEFAULT_CHAT_URL

    def resolved_chat_model(self) -> str:
        """Model chọn trên trang đó: YAML > .env (CHAT_MODEL) > mặc định."""
        return self.chat_model or os.getenv("CHAT_MODEL") or DEFAULT_CHAT_MODEL

    def resolved_kb_dir(self) -> Optional[str]:
        """Folder of source .md files used for the deep (2-pass) check."""
        if self.kb_dir:
            return self.kb_dir
        source_path = PROJECT_ROOT / self.source
        return self.source if source_path.is_dir() else None


def _project_path(key: str) -> Path:
    return PROJECTS_DIR / f"{key}.yaml"


def list_projects() -> List[str]:
    """Names of every configured project, sorted."""
    if not PROJECTS_DIR.is_dir():
        return []
    return sorted(p.stem for p in PROJECTS_DIR.glob("*.yaml"))


def load_project(key: str) -> ProjectConfig:
    """Read projects/<key>.yaml into a ProjectConfig."""
    path = _project_path(key)
    if not path.exists():
        available = list_projects()
        hint = ", ".join(available) if available else "(chưa có project nào)"
        raise ProjectError(
            f"Không tìm thấy project '{key}'.\n"
            f"   File cần có: {path.relative_to(PROJECT_ROOT)}\n"
            f"   Project hiện có: {hint}"
        )

    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ProjectError(f"File {path.name} không phải YAML hợp lệ:\n   {exc}") from exc

    if not isinstance(raw, dict):
        raise ProjectError(f"File {path.name} phải là một khối key: value.")

    source = raw.get("source")
    if not source:
        raise ProjectError(f"File {path.name} thiếu trường bắt buộc 'source'.")

    chatbot: Dict = raw.get("chatbot") or {}
    scoring: Dict = raw.get("scoring") or {}
    llm: Dict = raw.get("llm") or {}

    return ProjectConfig(
        key=key,
        name=raw.get("name") or key,
        source=str(source),
        questions=int(raw.get("questions", 25)),
        spec=str(chatbot.get("spec", "tests/KB.spec.ts")),
        chat_url=chatbot.get("url"),
        chat_model=chatbot.get("model"),
        batch_size=int(chatbot.get("batch_size", 10)),
        threshold=int(scoring.get("threshold", 6)),
        deep_check=bool(scoring.get("deep_check", True)),
        kb_dir=scoring.get("kb_dir"),
        provider=str(llm.get("provider", "openai")),
        model=llm.get("model"),
        base_url=llm.get("base_url"),
    )
