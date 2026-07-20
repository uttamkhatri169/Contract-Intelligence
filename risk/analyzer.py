from risk.rules import RISK_RULES
from risk.models import RiskResult


class RiskAnalyzer:

    @staticmethod
    def analyze(chunks):

        risks = []

        for chunk in chunks:

            text = chunk.text.lower()

            for rule, config in RISK_RULES.items():

                for keyword in config["keywords"]:

                    if keyword in text:

                        risks.append(

                            RiskResult(

                                clause=rule,

                                level=config["level"],

                                reason=f"Matched keyword: '{keyword}'",

                                evidence=chunk.text

                            )

                        )

                        break

        return risks