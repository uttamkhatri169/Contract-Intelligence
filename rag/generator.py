from rag.prompt_builder import PromptBuilder
from llm.provider_factory import ProviderFactory


class Generator:

    def __init__(self):

        self.llm = ProviderFactory.create()

    def answer(self, question, context):

        prompt = PromptBuilder.qa_prompt(
            question,
            context
        )

        return self.llm.generate(prompt)