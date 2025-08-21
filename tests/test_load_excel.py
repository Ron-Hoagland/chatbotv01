import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from document_loader import load_excel_file
from config import DATA_DIR

def test_load_excel():
    xlsx_path = os.path.join(DATA_DIR, "sample.xlsx")
    try:
        text = load_excel_file(xlsx_path)
        print("Excel file loaded successfully. First 500 characters:")
        print(text[:500])
    except Exception as e:
        print(f"Error loading Excel file: {e}")

if __name__ == "__main__":
    test_load_excel()
