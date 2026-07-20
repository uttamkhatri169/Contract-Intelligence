from llm.config import LLM_PROVIDER
from llm.ollama_provider import OllamaProvider


class ProviderFactory:

    @staticmethod
    def create():

        if LLM_PROVIDER == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unknown provider: {LLM_PROVIDER}"
        )