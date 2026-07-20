from evaluation.evaluator import Evaluator

evaluator = Evaluator()

accuracy, results = evaluator.evaluate()

print("\n========== EVALUATION ==========\n")

print(f"Retrieval Accuracy : {accuracy}%")

print()

for item in results:

    print("=" * 70)

    print(item["question"])

    print()

    print(item["retrieved"])

    print()

    print(item["correct"])

    print()