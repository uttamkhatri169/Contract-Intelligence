from ollama import Client

from llm.base_provider import BaseLLMProvider
from llm.config import OLLAMA_MODEL, OLLAMA_URL


class OllamaProvider(BaseLLMProvider):

    def __init__(self):

        self.client = Client(host=OLLAMA_URL)

    def generate(self, prompt: str) -> str:

        response = self.client.chat(

            model=OLLAMA_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]