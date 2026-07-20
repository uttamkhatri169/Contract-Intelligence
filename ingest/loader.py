import os

from ingest.pdf_parser import PDFParser
from ingest.docx_parser import DOCXParser


class DocumentLoader:
    """
    Factory class responsible for selecting
    the correct parser based on file extension.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def get_parser(self):
        extension = os.path.splitext(self.file_path)[1].lower()

        if extension == ".pdf":
            return PDFParser(self.file_path)

        elif extension == ".docx":
            return DOCXParser(self.file_path)

        else:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

    def load(self):
        parser = self.get_parser()
        return parser.extract_text()