from docx import Document
from loader import save_json
from base_parser import BaseParser


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