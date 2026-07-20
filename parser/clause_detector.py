class ClauseDetector:
    """
    Detects common legal clause types
    based on keywords.
    """

    CLAUSES = {
        "Termination": [
            "termination",
            "terminate",
            "expiry"
        ],

        "Confidentiality": [
            "confidential",
            "non-disclosure",
            "nda"
        ],

        "Liability": [
            "liability",
            "liable",
            "damages"
        ],

        "Indemnification": [
            "indemnify",
            "indemnification"
        ],

        "Governing Law": [
            "governing law",
            "jurisdiction",
            "court"
        ],

        "Payment": [
            "payment",
            "invoice",
            "fees"
        ],

        "Intellectual Property": [
            "intellectual property",
            "ip",
            "copyright",
            "patent"
        ],

        "Non Compete": [
            "non compete",
            "non-compete",
            "competition"
        ]
    }

    @staticmethod
    def detect(text):

        text = text.lower()

        for clause, keywords in ClauseDetector.CLAUSES.items():

            for keyword in keywords:

                if keyword in text:
                    return clause

        return "General"