import os
from PyPDF2 import PdfReader, PdfWriter

def list_pdf_titles(folder_path, output_file):
    output_pdf = PdfWriter()

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            pdf = PdfReader(file_path)
            title = pdf.metadata.title

            output_pdf.add_page(pdf.pages[0])
            output_pdf.add_metadata({'/Title': str(title)})

    with open(output_file, 'wb') as f:
        output_pdf.write(f)

folder_path = '/Users/ilayda/Desktop/PDF'
output_file = '/Users/ilayda/Desktop/basliklar.pdf'

list_pdf_titles(folder_path, output_file)