class Prompt:
    prompt: str = """Extract all visible information from the provided identity card or form image using OCR (Optical Character Recognition).
              Only use the information found visually on the card. Do not guess or infer missing fields.
              If you cannot find some information, or the information is unclear, or you face any other such blocker, respond null to that field.
              Again! Make sure the output is STRICTLY A JSON OBJECT"""