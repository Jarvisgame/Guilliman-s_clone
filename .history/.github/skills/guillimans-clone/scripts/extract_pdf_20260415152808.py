"""
Extract text from Guilliman's biography PDF.
Usage: python extract_pdf.py
"""

import sys
from pathlib import Path

import fitz  # PyMuPDF

# Paths relative to this script's location
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[3]  # .github/skills/guillimans-clone/scripts -> project root
PDF_PATH = PROJECT_ROOT / "assets" / "assets.pdf"
OUTPUT_PATH = SCRIPT_DIR.parent / "assets" / "raw_extract.md"


def extract_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF file, page by page."""
    if not pdf_path.exists():
        print(f"Error: PDF not found at {pdf_path}", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open(str(pdf_path))
    pages = []
    total = doc.page_count

    for i, page in enumerate(doc):
        text = page.get_text("text")
        if text.strip():
            pages.append(f"<!-- Page {i + 1} / {total} -->\n\n{text.strip()}")
        print(f"\rExtracting page {i + 1}/{total}...", end="", flush=True)

    doc.close()
    print(f"\nDone. Extracted {len(pages)} pages with content out of {total} total.")
    return "\n\n---\n\n".join(pages)


def main():
    print(f"PDF path: {PDF_PATH}")
    print(f"Output path: {OUTPUT_PATH}")

    content = extract_pdf(PDF_PATH)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        f"# Raw PDF Extract: Roboute Guilliman Biography\n\n"
        f"Extracted from: `{PDF_PATH.name}`\n\n---\n\n{content}",
        encoding="utf-8",
    )
    print(f"Saved to {OUTPUT_PATH} ({len(content):,} chars)")


if __name__ == "__main__":
    main()
