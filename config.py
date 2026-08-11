"""
Configuration defaults for RAG question generation.
"""
from dataclasses import dataclass
from typing import Dict, Optional

# Gateway của công ty nói giao thức OpenAI, khai báo qua provider "openai"
# cùng OPENAI_BASE_URL / OPENAI_MODEL trong .env.
DEFAULT_PROVIDER = "openai"
DEFAULT_NUM_QUESTIONS = 20
DEFAULT_OUTPUT = "outputs/rag/rag_eval.json"

MAX_RETRY = 2
MAX_TOKENS = 9999
TEMPERATURE = 0.3

DEFAULT_OLLAMA_MODEL = "qwen2.5:7b"
DEFAULT_OLLAMA_URL = "http://localhost:11434"
OLLAMA_TIMEOUT = 60


@dataclass(frozen=True)
class ProviderConfig:
    """Model configuration for a provider."""

    model: str
    base_url: Optional[str] = None


PROVIDER_CONFIGS: Dict[str, ProviderConfig] = {
    "deepseek": ProviderConfig(
        model="deepseek-chat",
        base_url="https://api.deepseek.com",
    ),
    # base_url để None: lấy từ {PROVIDER}_BASE_URL trong .env, hoặc --base-url.
    # model ở đây chỉ là fallback khi .env không đặt {PROVIDER}_MODEL.
    "openai": ProviderConfig(model="gpt-4o-mini"),
    "anthropic": ProviderConfig(model="claude-sonnet-4-20250514"),
}

PROVIDER_KIND_MAP: Dict[str, str] = {
    "deepseek": "api",
    "openai": "api",
    "anthropic": "api",
    "ollama": "local",
}

# API keys are never stored here. They are read from .env or the --api-key flag
# as {PROVIDER}_API_KEY (e.g. OPENAI_API_KEY). See .env.example.
