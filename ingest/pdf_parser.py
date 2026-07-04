import fitz
from loader import save_json
from base_parser import BaseParser


class PDFParser(BaseParser):

    def __init__(self, file_path):
        super().__init__(file_path)

    def extract_text(self):

        document = fitz.open(self.file_path)

        pages = []

        for page_number in range(len(document)):

            page = document.load_page(page_number)

            text = page.get_text()

            paragraphs = [
                p.strip()
                for p in text.split("\n")
                if p.strip()
            ]

            pages.append({
                "page": page_number + 1,
                "paragraphs": paragraphs
            })

        document.close()

        return pages


if __name__ == "__main__":

    parser = PDFParser("data/contracts/nda/NDA.pdf")

    pages = parser.extract_text()

    save_json(
        pages,
        "data/processed/NDA.json"
    )

    print("PDF Parsed Successfully!")