from PyPDF2 import PdfReader


def extract_pdf_content(file_path):
    try:
        pdf_reader = PdfReader(file_path)
        content = " "
        for page in pdf_reader.pages:
            content += page.extract_text() or ""
        return content.strip() 
    except Exception as e:
        print(f"Error extracting PDF content: {e}")
        return None
