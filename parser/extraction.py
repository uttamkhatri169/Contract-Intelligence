import json

from parser.contract_schema import ContractSchema
from llm.provider_factory import ProviderFactory
from llm.prompt_builder import extraction_prompt


class ContractExtractor:

    def __init__(self):

        self.llm = ProviderFactory.create()

    def extract(self, context):

        prompt = extraction_prompt(
            context
        )

        response = self.llm.generate(prompt)

        data = json.loads(response)

        return ContractSchema(**data)