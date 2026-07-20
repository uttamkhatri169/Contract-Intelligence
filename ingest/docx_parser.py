from docx import Document
from ingest.utils import save_json
from ingest.base_parser import BaseParser


class DOCXParser(BaseParser):

    def __init__(self, file_path):
        super().__init__(file_path)

    def extract_text(self):

        document = Document(self.file_path)

        paragraphs = [
            para.text.strip()
            for para in document.paragraphs
            if para.text.strip()
        ]

        return [
            {
                "document_name": self.document_name,
                "page": 1,
                "paragraphs": paragraphs
            }
        ]


if __name__ == "__main__":

    parser = DOCXParser("data/contracts/nda/NDA.docx")

    pages = parser.extract_text()

    save_json(
        pages,
        "data/processed/NDA_docx.json"
    )

    print("DOCX Parsed Successfully!")