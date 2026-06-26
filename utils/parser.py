
import PyPDF2

def extract_text(pdf_file):
    text=""
    reader=PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        t=page.extract_text()
        if t:
            text += t
    return text
