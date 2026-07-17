import PyPDF2

pdf_file = open(r"rootdrive:\folder\subfolder\filename.pdf", "rb")
reader = PyPDF2.PdfReader(pdf_file)

with open(r"rootdrive:\folder\subfolder\filename.txt", "w", encoding="utf-8") as txt_file:
    for page in reader.pages:
        txt_file.write(page.extract_text() + "\n")

pdf_file.close()
