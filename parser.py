#!/usr/bin/env python3

import fitz  # PyMuPDF
import random

def extract_random_text(pdf_path="data/mikrodozing.pdf"):
    """Возвращает случайный абзац из PDF"""
    try:
        doc = fitz.open(pdf_path)
        paragraphs = []
        for page in doc:
            text = page.get_text()
            for part in text.split("\n\n"):
                clean = part.strip()
                if len(clean) > 100:
                    paragraphs.append(clean)
        doc.close()
        return random.choice(paragraphs) if paragraphs else "[PDF пуст]"
    except Exception as e:
        return f"[Ошибка чтения PDF: {e}]"
