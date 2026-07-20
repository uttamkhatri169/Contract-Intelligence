from dataclasses import dataclass


@dataclass
class RiskResult:

    clause: str

    level: str

    reason: str

    evidence: str