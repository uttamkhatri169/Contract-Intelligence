import re


class TextPreprocessor:
    """
    Cleans extracted document text before chunking.
    """

    @staticmethod
    def clean_paragraph(text: str) -> str:
        """
        Clean a single paragraph.
        """

        # Remove leading/trailing spaces
        text = text.strip()

        # Replace multiple spaces with one
        text = re.sub(r"\s+", " ", text)

        return text

    @staticmethod
    def preprocess_document(document):

        processed_pages = []

        for page in document:

            cleaned = []

            for paragraph in page["paragraphs"]:

                paragraph = TextPreprocessor.clean_paragraph(paragraph)

                if paragraph:
                    cleaned.append(paragraph)

            processed_pages.append({

                "document_name": page.get("document_name", ""),

                "page": page["page"],

                "paragraphs": cleaned,

                "total_paragraphs": len(cleaned)

            })

        return processed_pages