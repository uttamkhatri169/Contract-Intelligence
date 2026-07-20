"""
Hallucination Guard

Blocks the LLM from answering
when retrieval confidence is too low.
"""

from rag.config import SIMILARITY_THRESHOLD


class HallucinationGuard:

    @staticmethod
    def should_answer(results):

        if not results:
            return False

        best_score = results[0]["score"]

        return best_score >= SIMILARITY_THRESHOLD

    @staticmethod
    def refusal_message():

        return (
            "\nUnable to answer confidently.\n\n"
            "Reason:\n"
            "- No sufficiently relevant clauses were retrieved.\n"
            "- Please rephrase your question or verify that the contract "
            "contains the requested information."
        )