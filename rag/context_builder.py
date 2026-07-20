"""
Context Builder

Formats retrieved chunks into
LLM-ready context.
"""


class ContextBuilder:

    @staticmethod
    def build(results):

        context = ""

        for i, result in enumerate(results, start=1):

            chunk = result["chunk"]

            context += (
                f"========== Document {i} ==========\n"
                f"Document : {chunk.document_name}\n"
                f"Page : {chunk.page}\n"
                f"Section : {chunk.section}\n"
                f"Clause Type : {chunk.clause_type}\n\n"
                f"{chunk.text}\n\n"
            )

        return context