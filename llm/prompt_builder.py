@staticmethod
def extraction_prompt(context):

    return f"""
You are an expert legal AI.

Extract the following information ONLY from the contract.

Return ONLY valid JSON.

Fields:

document_type

party_a

party_b

effective_date

term

termination_clause

governing_law

liability_cap

confidentiality_period

non_compete

Contract:

{context}
"""