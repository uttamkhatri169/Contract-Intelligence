class Metrics:
    
    @staticmethod
    def retrieval_accuracy(results):

        total = len(results)

        correct = 0

        for result in results:

            if result["correct"]:

                correct += 1

        if total == 0:
            return 0

        return round(correct / total * 100, 2)