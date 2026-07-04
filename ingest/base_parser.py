from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Abstract Base Class for all document parsers.
    Every parser must implement extract_text().
    """

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def extract_text(self):
        pass