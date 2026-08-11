"""
Anthropic API provider implementation.
"""
from typing import Any, Dict, List, Optional

from providers.base import LLMProvider


class AnthropicProvider(LLMProvider):
    """Provider for Anthropic Claude chat API.

    base_url lets this point at a company gateway that speaks the Anthropic
    protocol; leave it unset to call the official API.
    """

    def __init__(self, api_key: str, model: str, base_url: Optional[str] = None) -> None:
        super().__init__()
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    def chat(self, messages: List[Dict[str, str]], **kwargs: Any) -> str:
        self.clear_error()
        try:
            import anthropic
        except ImportError:
            print("❌ Anthropic library not installed. Run: pip install anthropic")
            self.last_error = "missing_anthropic_library"
            return ""

        try:
            client_kwargs: Dict[str, Any] = {"api_key": self.api_key}
            if self.base_url:
                client_kwargs["base_url"] = self.base_url
            client = anthropic.Anthropic(**client_kwargs)
            max_tokens = kwargs.get("max_tokens")
            payload: Dict[str, Any] = {
                "model": self.model,
                "max_tokens": max_tokens if max_tokens is not None else 4000,
                "messages": messages,
            }
            message = client.messages.create(**payload)
            if not message.content:
                return ""
            return message.content[0].text

        except Exception as exc:
            print(f"❌ Anthropic API error: {exc}")
            self.last_error = str(exc)
            return ""
