import fitz

def extract_text(pdf_path="data/mikrodozing.pdf"):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()
