import re
from parser.clause_detector import ClauseDetector


class MetadataGenerator:
    """
    Generates metadata for every paragraph
    extracted from a document.
    """

    @staticmethod
    def detect_section(text):

        """
        Detect simple section headings.
        """

        if re.match(r"^\d+\.", text):
            return text

        return "Unknown"

    @staticmethod
    def generate(document):

        metadata = []

        paragraph_id = 1

        current_section = "Unknown"

        for page in document:

            for paragraph in page["paragraphs"]:

                detected = MetadataGenerator.detect_section(
                    paragraph
                )

                if detected != "Unknown":
                    current_section = detected

                metadata.append({

                    "paragraph_id": paragraph_id,

                    "document_name": page["document_name"],

                    "page": page["page"],

                    "section": current_section,

                    "clause_type": ClauseDetector.detect(paragraph),

                    "text": paragraph

                })

                paragraph_id += 1

        return metadata