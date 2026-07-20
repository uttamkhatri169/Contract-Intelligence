from pydantic import BaseModel


class ContractSchema(BaseModel):

    document_type: str

    party_a: str

    party_b: str

    effective_date: str

    term: str

    termination_clause: str

    governing_law: str

    liability_cap: str

    confidentiality_period: str

    non_compete: bool