import fitz  # PyMuPDF
import pdfplumber
import os

from backend.services.ocr import run_ocr


def parse_pdf(path: str) -> str:
    text = ""

    try:
        doc = fitz.open(path)

        for page in doc:
            text += page.get_text()

        if text.strip():
            return text
    except Exception:
        pass

    # Fallback: OCR
    return run_ocr(path)


def parse_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def parse_document(path: str) -> str:
    ext = os.path.splitext(path)[-1].lower()

    if ext == ".pdf":
        return parse_pdf(path)

    if ext == ".txt":
        return parse_text_file(path)

    raise ValueError("Unsupported file format")
