from comparison.models import ComparisonResult


class ContractComparator:

    @staticmethod
    def compare(contract_a, contract_b):

        results = []

        fields = [

            "termination_clause",

            "governing_law",

            "term",

            "liability_cap",

            "confidentiality_period",

            "non_compete"

        ]

        for field in fields:

            value_a = getattr(contract_a, field)

            value_b = getattr(contract_b, field)

            status = "Same"

            if str(value_a).strip().lower() != str(value_b).strip().lower():

                status = "Different"

            results.append(

                ComparisonResult(

                    clause=field,

                    contract_a=str(value_a),

                    contract_b=str(value_b),

                    status=status

                )

            )

        return results