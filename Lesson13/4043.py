# استخراج متن از فایل PDF با pdfplumber :
import pdfplumber

# باز کردن فایل PDF
with pdfplumber.open(r"C:\Users\kara\OneDrive\Desktop\python\ASP\leo.pdf") as pdf:
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        text = page.extract_text()
        print(f"Page {page_num + 1}:\n{text}\n")