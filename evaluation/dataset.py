import json


class EvaluationDataset:

    @staticmethod
    def load(path):

        with open(path, "r") as file:

            return json.load(file)