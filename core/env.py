"""
Shared resolution of secrets and per-provider settings.

Precedence is always: CLI flag > environment variable > .env file > None.
API keys are never read from source files. See .env.example.
"""
import os
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"


def load_env_file(env_path: Optional[Path] = None) -> None:
    """Load key=value pairs from a .env file into the process environment.

    Existing environment variables are never overwritten.
    """
    path = Path(env_path) if env_path else ENV_FILE
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def resolve_api_key(provider_name: str, cli_key: Optional[str] = None) -> Optional[str]:
    """Resolve the API key for a provider from the CLI flag or {PROVIDER}_API_KEY."""
    if cli_key:
        return cli_key
    return os.getenv(f"{provider_name.upper()}_API_KEY")


def resolve_env_override(provider_name: str, suffix: str) -> Optional[str]:
    """Resolve provider-specific overrides such as OPENAI_MODEL or OPENAI_BASE_URL."""
    value = os.getenv(f"{provider_name.upper()}_{suffix}")
    if value:
        return value
    # Backward-compatible alias for Anthropic model name
    if provider_name == "anthropic" and suffix == "MODEL":
        return os.getenv("ANTHROPIC_DEFAULT_SONNET_MODEL")
    return None
