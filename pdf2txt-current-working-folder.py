import os
import PyPDF2

# Step 1: Define the folder path
folder_path = os.path.dirname(os.path.abspath(__file__))

# Step 2: List all files in the folder
files = os.listdir(folder_path)

# 👉 Count the number of files and print
print("Number of files in folder:", len(files))

# Step 3: Loop through all files
for f in files:
    if f.lower().endswith(".pdf"):   # ✅ Only process PDF files
        pdf_path = os.path.join(folder_path, f)

        # Step 4: Open the PDF
        pdf_file = open(pdf_path, "rb")
        reader = PyPDF2.PdfReader(pdf_file)

        # Step 5: Create a txt file with the same name
        txt_path = pdf_path + ".txt"
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            # Step 6: Extract text from all pages
            for page in reader.pages:
                txt_file.write(page.extract_text() + "\n")

        # Step 7: Close the PDF
        pdf_file.close()

        print(f"Converted {f} → {txt_path}")
    else:
        # 👉 Skip non-PDF files
        print(f"Skipped {f} (not a PDF)")