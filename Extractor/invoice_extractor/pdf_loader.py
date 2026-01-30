import pdfplumber

def load_pdf_text(pdf_path: str) -> str:
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()

            if page_text:
                text += f"\n--- Page {page_number} ---\n"
                text += page_text

    return text
