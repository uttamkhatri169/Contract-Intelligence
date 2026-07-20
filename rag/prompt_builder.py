"""
Prompt templates used throughout ClauseCraft.
"""


class PromptBuilder:

    @staticmethod
    def qa_prompt(
        question: str,
        context: str
    ) -> str:

        return f"""
You are ClauseCraft, an AI legal assistant.

Answer ONLY using the supplied context.

If the answer is not contained in the context,
reply exactly:

I don't know based on the provided contract.

----------------------------

CONTEXT

{context}

----------------------------

QUESTION

{question}

----------------------------

Return:

1. Short answer

2. Supporting explanation

Do not invent information.
"""