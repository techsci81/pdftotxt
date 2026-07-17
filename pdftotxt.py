import PyPDF2

pdf_file = open(r"C:\Users\innot\OneDrive\Documents\careersearch\2026\Resume-Singaravelu-4.pdf", "rb")
reader = PyPDF2.PdfReader(pdf_file)

with open(r"C:\Users\innot\OneDrive\Documents\careersearch\2026\Resume-Singaravelu-4.pdf.txt", "w", encoding="utf-8") as txt_file:
    for page in reader.pages:
        txt_file.write(page.extract_text() + "\n")

pdf_file.close()