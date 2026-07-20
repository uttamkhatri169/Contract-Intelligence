from dataclasses import dataclass


@dataclass
class ComparisonResult:

    clause: str

    contract_a: str

    contract_b: str

    status: str 