"""
Configuration defaults for RAG question generation.
"""
from dataclasses import dataclass
from typing import Dict, Optional

DEFAULT_PROVIDER = "deepseek"
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
    "openai": ProviderConfig(model="gpt-4o-mini"),
    "anthropic": ProviderConfig(model="glm-4.7"),
}

PROVIDER_KIND_MAP: Dict[str, str] = {
    "deepseek": "api",
    "openai": "api",
    "anthropic": "api",
    "ollama": "local",
}

# Optional API keys stored in config (leave empty to use env/CLI).
PROVIDER_API_KEYS: Dict[str, str] = {
    "deepseek": "",
    "openai": "sk-A08WIZrBeajxCt-08Q5FXg",
    "anthropic": "sk-A08WIZrBeajxCt-08Q5FXg",
}
