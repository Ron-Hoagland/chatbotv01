import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from document_loader import load_word_file
from config import DATA_DIR

def test_load_word():
    docx_path = os.path.join(DATA_DIR, "sample.docx")  # Replace with your Word filename
    try:
        text = load_word_file(docx_path)
        print("Word document loaded successfully. First 500 characters:")
        print(text[:500])
    except Exception as e:
        print(f"Error loading Word document: {e}")

if __name__ == "__main__":
    test_load_word()
