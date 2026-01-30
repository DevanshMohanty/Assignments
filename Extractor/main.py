from dotenv import load_dotenv
load_dotenv()

import json
from pathlib import Path

from invoice_extractor.pdf_loader import load_pdf_text
from invoice_extractor.chain import build_chain


DATA_DIR = Path("data")       
OUTPUT_DIR = Path("outputs") 
MAX_FILES = 5                

pdf_files = []

for f in DATA_DIR.iterdir():
    if f.is_file() and f.suffix.lower() == ".pdf":
        pdf_files.append(f)



pdf_files = pdf_files[:MAX_FILES]

print(f"Found {len(pdf_files)} PDF file(s) to process")


chain = build_chain()

for pdf_path in pdf_files:

    try:
        # Extract text from PDF
        invoice_text = load_pdf_text(str(pdf_path))

        if not invoice_text.strip():
            print("No text extracted")
            continue

        # Run LLM extraction
        result = chain.invoke({"invoice_text": invoice_text})

        # Convert Pydantic object into Python dict
        json_data = result.model_dump()

        # Create output JSON path
        output_path = OUTPUT_DIR / f"{pdf_path.stem}.json"

        # Save JSON file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Failed to process {pdf_path.name}")
        print(f"Error: {e}")

print("\nProcessing completed.")
