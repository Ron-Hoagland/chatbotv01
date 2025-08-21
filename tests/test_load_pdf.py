
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from document_loader import load_pdf_file
from config import DATA_DIR

def test_load_pdf():
    pdf_path = os.path.join(DATA_DIR, "sample.pdf")  # Replace with your PDF filename
    try:
        text = load_pdf_file(pdf_path)
        print("PDF loaded successfully. First 500 characters:")
        print(text[:500])
    except Exception as e:
        print(f"Error loading PDF: {e}")

if __name__ == "__main__":
    test_load_pdf()
