"""
Citation Engine

Generates citations from retrieved chunks.
"""


class CitationEngine:

    @staticmethod
    def generate(results):

        citations = []

        for index, result in enumerate(results, start=1):

            chunk = result["chunk"]

            citations.append(
                {
                    "id": index,
                    "document": chunk.document_name,
                    "page": chunk.page,
                    "section": chunk.section,
                    "clause_type": chunk.clause_type,
                    "score": round(result["score"], 4),
                    "evidence": chunk.text
                }
            )

        return citations

    @staticmethod
    def print(citations):

        print("\n========== CITATIONS ==========\n")

        for citation in citations:

            print("=" * 70)

            print(f"[{citation['id']}]")

            print(f"Document : {citation['document']}")

            print(f"Page     : {citation['page']}")

            print(f"Section  : {citation['section']}")

            print(f"Clause   : {citation['clause_type']}")

            print(f"Score    : {citation['score']}")

            print("\nEvidence:\n")

            print(citation["evidence"])

            print()