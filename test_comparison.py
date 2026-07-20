from parser.contract_schema import ContractSchema
from comparison.comparator import ContractComparator


contract_a = ContractSchema(
    document_type="NDA",
    party_a="ABC Pvt Ltd",
    party_b="XYZ Technologies",
    effective_date="2025-01-01",
    term="2 years",
    termination_clause="30 days notice",
    governing_law="India",
    liability_cap="Unlimited",
    confidentiality_period="5 years",
    non_compete=True
)

contract_b = ContractSchema(
    document_type="NDA",
    party_a="ABC Pvt Ltd",
    party_b="XYZ Innovations",
    effective_date="2025-01-01",
    term="3 years",
    termination_clause="60 days notice",
    governing_law="Singapore",
    liability_cap="₹5,00,000",
    confidentiality_period="3 years",
    non_compete=True
)

results = ContractComparator.compare(contract_a, contract_b)

print("\n========== CONTRACT COMPARISON ==========\n")

for result in results:

    print("=" * 70)

    print(f"Clause      : {result.clause}")

    print(f"Contract A  : {result.contract_a}")

    print(f"Contract B  : {result.contract_b}")

    print(f"Status      : {result.status}")

    print()