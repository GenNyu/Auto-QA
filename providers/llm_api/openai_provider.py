"""
OpenAI API provider implementation.
"""
from typing import Any, Dict, List, Optional

from config import API_TIMEOUT, DEFAULT_STREAM
from providers.base import LLMProvider


class StreamInterrupted(Exception):
    """Stream đứt sau khi đã nhận được một phần câu trả lời."""

    def __init__(self, reason: str, received: str) -> None:
        super().__init__(reason)
        self.reason = reason
        self.received = received


class OpenAIProvider(LLMProvider):
    """Provider for OpenAI chat API."""

    def __init__(
        self,
        provider_name: str,
        api_key: str,
        model: str,
        base_url: Optional[str] = None,
        stream: bool = DEFAULT_STREAM,
        timeout: int = API_TIMEOUT,
    ) -> None:
        super().__init__()
        self.provider_name = provider_name
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.stream = stream
        self.timeout = timeout

    def _label(self) -> str:
        return "DeepSeek" if self.provider_name == "deepseek" else "OpenAI"

    def _collect_stream(self, response: Any) -> str:
        """Gộp các delta của một response SSE thành văn bản hoàn chỉnh.

        Ném lỗi nếu stream đứt giữa chừng, kèm phần đã nhận được, để phía gọi
        phân biệt được "mạng đứt" với "model trả JSON sai".
        """
        pieces: List[str] = []
        try:
            for chunk in response:
                # Có gateway gửi kèm chunk chỉ chứa usage, không có choices.
                if not getattr(chunk, "choices", None):
                    continue
                delta = chunk.choices[0].delta
                # reasoning_content (model suy luận như glm-5) cố ý bỏ qua: nó
                # giữ kết nối không im lặng, nhưng không thuộc câu trả lời.
                piece = getattr(delta, "content", None)
                if piece:
                    pieces.append(piece)
        except Exception as exc:
            received = "".join(pieces)
            raise StreamInterrupted(str(exc), received) from exc

        return "".join(pieces)

    def chat(self, messages: List[Dict[str, str]], **kwargs: Any) -> str:
        self.clear_error()
        try:
            from openai import OpenAI
        except ImportError:
            print("❌ OpenAI library not installed. Run: pip install openai")
            self.last_error = "missing_openai_library"
            return ""

        try:
            client_kwargs: Dict[str, Any] = {
                "api_key": self.api_key,
                "timeout": self.timeout,
            }
            if self.base_url:
                client_kwargs["base_url"] = self.base_url

            client = OpenAI(**client_kwargs)
            params: Dict[str, Any] = {
                "model": self.model,
                "messages": messages,
            }
            if "max_tokens" in kwargs and kwargs["max_tokens"] is not None:
                params["max_tokens"] = kwargs["max_tokens"]
            if "temperature" in kwargs and kwargs["temperature"] is not None:
                params["temperature"] = kwargs["temperature"]

            if not self.stream:
                response = client.chat.completions.create(**params)
                return response.choices[0].message.content or ""

            response = client.chat.completions.create(stream=True, **params)
            return self._collect_stream(response)

        except StreamInterrupted as exc:
            print(f"❌ {self._label()} stream đứt giữa chừng: {exc.reason}")
            print(f"   (đã nhận {len(exc.received)} ký tự trước khi đứt)")
            self.last_error = f"stream_interrupted: {exc.reason}"
            return ""

        except Exception as exc:
            print(f"❌ {self._label()} API error: {exc}")
            self.last_error = str(exc)
            return ""
