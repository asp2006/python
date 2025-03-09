import tkinter as tk
import json

# فایل برای ذخیره‌سازی شماره‌ها
data_file = "numbers_data.json"

# دیکشنری متون مربوط به هر شماره
number_texts = {
    "40001": """
هدف - نمایش این عبارت (( به برنامه پایتون خوش آمدید ))

1- برنامه VS Code را باز کنید و یک پوشه جدید برای پروژه ایجاد کنید.
در داخل پوشه ایجاد شده، یک فایل جدید به نام welcome.py ایجاد کنید.

2- نوشتن کد:
کد زیر را در فایل welcome.py بنویسید:
# برنامه برای نمایش یک پیام خوش آمدید
("به برنامه پایتون خوش آمدید")print

3. اجرای برنامه:
در صفحه کدنویسی - کلیک راست کنید و گزینه های زیر را تایید کنید
run in interactive window
run current file in interactive window
سمت راست صفحه - می‌توانید خروجی برنامه - یعنی نمایش پیام را ببینید.
    """,
    # شماره‌های دیگر را اینجا اضافه کنید
}

# تابع برای بارگذاری شماره‌ها از فایل
def load_numbers():
    try:
        with open(data_file, "r") as f:
            data = json.load(f)
            return data["column_1"], data["column_2"]
    except (FileNotFoundError, json.JSONDecodeError):
        # اگر فایل وجود نداشته باشد یا خراب باشد، شماره‌های پیش‌فرض برمی‌گردد
        return [f"40{str(i).zfill(3)}" for i in range(1, 26)], [f"40{str(i+50).zfill(3)}" for i in range(1, 26)]

# تابع برای ذخیره شماره‌ها در فایل
def save_numbers():
    data = {
        "column_1": numbers_column_1,
        "column_2": numbers_column_2
    }
    with open(data_file, "w") as f:
        json.dump(data, f)

# تابع برای نشان دادن شماره‌ای که در مستطیل کلیک شده
def on_button_click(number, button_index, column):
    # نمایش متن مرتبط با شماره
    text_to_display = number_texts.get(number, "متن برای این شماره موجود نیست.")
    text_label.config(text=text_to_display)  # نمایش متن در لایه متن

# لیست‌های شماره‌ها برای دو ستون (25 شماره در هر ستون)
numbers_column_1, numbers_column_2 = load_numbers()

# فریم اصلی برای محتوا
root = tk.Tk()
root.title("Editable Exercise List")

# اضافه کردن عنوان در بالای صفحه
title_label = tk.Label(root, text="لیست تمرینات پایتون", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# ایجاد یک Canvas برای اضافه کردن اسکرول
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# ایجاد یک Scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

# تنظیم اسکرول برای Canvas
canvas.config(yscrollcommand=scrollbar.set)

# ایجاد یک فریم در داخل Canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# اضافه کردن یک تابع برای به‌روزرسانی نوار اسکرول هنگام تغییر اندازه محتوا
def on_frame_configure(event):
    canvas.config(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

# لیست دکمه‌ها
buttons_column_1 = []
buttons_column_2 = []

# پر کردن دکمه‌ها و شماره‌ها برای ستون اول
for i, num in enumerate(numbers_column_1):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num, i=i, col=0: on_button_click(num, i, col))
    button.grid(row=i+2, column=0, padx=5, pady=5)
    buttons_column_1.append(button)

# پر کردن دکمه‌ها و شماره‌ها برای ستون دوم
for i, num in enumerate(numbers_column_2):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num, i=i, col=1: on_button_click(num, i, col))
    button.grid(row=i+2, column=2, padx=5, pady=5)
    buttons_column_2.append(button)

# اضافه کردن یک لایه برای نمایش متن
text_label = tk.Label(root, text="", font=("Arial", 12), fg="green", justify="left")
text_label.pack(pady=20)

# نمایش پنجره
root.mainloop()
