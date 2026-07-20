from evaluation.dataset import EvaluationDataset
from evaluation.metrics import Metrics

from rag.retriever import Retriever


class Evaluator:

    def __init__(self):

        self.retriever = Retriever()

    def evaluate(self):

        dataset = EvaluationDataset.load(
            "evaluation/test_questions.json"
        )

        results = []

        for item in dataset:

            retrieved = self.retriever.retrieve(
                item["question"],
                top_k=1
            )

            if len(retrieved) == 0:

                results.append(
                    {
                        "question": item["question"],
                        "correct": False
                    }
                )

                continue

            chunk = retrieved[0]["chunk"]

            correct = (

                chunk.section == item["expected_section"]

            )

            results.append(
                {
                    "question": item["question"],
                    "correct": correct,
                    "retrieved": chunk.section
                }
            )

        accuracy = Metrics.retrieval_accuracy(
            results
        )

        return accuracy, results