"""
Gemini LLM wrapper.
"""

import os

from dotenv import load_dotenv
from google import genai
from rag.config import LLM_MODEL


load_dotenv()


class LLMService:

    def __init__(self):

        self.client = None
        self.last_error = None

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:
            self.last_error = "Gemini API key not found."
            return

        try:
            self.client = genai.Client(
                api_key=api_key
            )
        except Exception as exc:
            self.last_error = str(exc)

    def _fallback_response(self, prompt: str, error: str | None = None) -> str:
        if error:
            return (
                "I couldn't reach the Gemini model. "
                f"Please try again later. Details: {error}"
            )

        return "I don't know based on the provided contract."

    def generate(
        self,
        prompt: str
    ) -> str:

        if self.client is None:
            return self._fallback_response(
                prompt,
                self.last_error,
            )

        try:
            response = self.client.models.generate_content(
                model=LLM_MODEL,
                contents=prompt,
            )

            return getattr(response, "text", str(response))

        except Exception as exc:
            self.last_error = str(exc)
            print(f"LLM generation failed: {exc}")
            return self._fallback_response(
                prompt,
                self.last_error,
            )