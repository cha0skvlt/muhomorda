import fitz  # PyMuPDF

def extract_text(pdf_path="data/mikrodozing.pdf"):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        return f"[Ошибка чтения PDF: {e}]"
