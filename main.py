import os
from PyPDF2 import PdfReader
def read_pdf_titles(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            with open (file_path, "rb") as file:
                pdf = PdfReader(file)
                title = pdf.metadata.title
                print(f"PDF Başlığı: {title}")

folder_path = "/Users/ilayda/Desktop/PDF"
read_pdf_titles(folder_path)