# هدف: ایجاد یک فرم ورودی در Tkinter برای وارد کردن داده‌ها به یک جدول (Treeview) که شامل اطلاعات مانند نام شهر، شماره ملی، موبایل، سن و آدرس است.

import tkinter as tk
from tkinter import ttk

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("فرم ورود اطلاعات")
root.geometry("600x400")

# داده‌های اولیه (در صورت نیاز به شروع)
data = []

# ایجاد Table یا Treeview برای نمایش داده‌ها
columns = ("نام شهر", "شماره ملی", "موبایل", "سن", "آدرس")
tree = ttk.Treeview(root, columns=columns, show="headings")

# تعریف هدرها
tree.heading("نام شهر", text="نام شهر")
tree.heading("شماره ملی", text="شماره ملی")
tree.heading("موبایل", text="موبایل")
tree.heading("سن", text="سن")
tree.heading("آدرس", text="آدرس")

# قرار دادن جدول در پنجره
tree.pack(pady=20)

# فیلدهای ورودی برای دریافت اطلاعات
label_name = tk.Label(root, text="نام شهر:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_national_id = tk.Label(root, text="شماره ملی:")
label_national_id.pack(pady=5)
entry_national_id = tk.Entry(root)
entry_national_id.pack(pady=5)

label_mobile = tk.Label(root, text="موبایل:")
label_mobile.pack(pady=5)
entry_mobile = tk.Entry(root)
entry_mobile.pack(pady=5)

label_age = tk.Label(root, text="سن:")
label_age.pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

label_address = tk.Label(root, text="آدرس:")
label_address.pack(pady=5)
entry_address = tk.Entry(root)
entry_address.pack(pady=5)

# تابع برای اضافه کردن داده‌ها به دیتاگرید
def insert_data():
    # دریافت مقادیر از فیلدهای ورودی
    name = entry_name.get()
    national_id = entry_national_id.get()
    mobile = entry_mobile.get()
    age = entry_age.get()
    address = entry_address.get()

    # افزودن داده‌ها به دیتاگرید
    tree.insert("", "end", values=(name, national_id, mobile, age, address))

    # پاک کردن فیلدهای ورودی بعد از ثبت داده‌ها
    entry_name.delete(0, tk.END)
    entry_national_id.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# دکمه برای ثبت اطلاعات
btn_insert = tk.Button(root, text="ثبت اطلاعات", command=insert_data)
btn_insert.pack(pady=10)

# نمایش پنجره
root.mainloop()
