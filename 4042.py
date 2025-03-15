# کد استخراج متن از PDF

# باز کردن فایل PDF
import PyPDF2

# باز کردن فایل PDF
with open(r"C:\Users\kara\OneDrive\Desktop\python\ASP\stor.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # استخراج متن از هر صفحه
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        print(f"Page {page_num + 1}:\n{text}\n")

import PyPDF2

# باز کردن فایل PDF
reader = PyPDF2.PdfReader(r"C:\Users\kara\OneDrive\Desktop\python\ASP\leo.pdf")
writer = PyPDF2.PdfWriter()

# افزودن صفحه اول به فایل جدید
writer.add_page(reader.pages[0])

# ذخیره‌سازی فایل جدید
with open('output.pdf', 'wb') as output_file:
    writer.write(output_file)
