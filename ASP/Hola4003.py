from tkinter import Tk, Canvas, PhotoImage
from tkinter import ttk
import tkinter as tk
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import subprocess
import os

# ایجاد پنجره اصلی
root = Tk()
root.title("مدیریت تمرینات پایتون")
root.geometry("800x600")


# استایل دکمه
style = ttk.Style()
style.configure("TButton", font=("Fira Code", 12), foreground="white", background="#007acc")

# تعریف لیست تمرین‌ها
numbers_column_1 = [
    "4001", "4002", "4003", "4004", "4005", "4010", "4011", "4012", "4013", "4014", "4015", "4016", "4017", "4018", "4019", "4020", "4021", "4022", "4023", "4024", "4025", "4028", "4029"
]
numbers_column_2 = [
    "4031", "4032", "4033", "4035", "4040", "4041", "4042", "4043", "4044", "4045", "4046", "4091", "4092", "4093", "4094", "4095", "4097", "4098", "4099", "4104", "4105", "4106"
]

# ایجاد دکمه‌های تمرینات
def create_buttons():
    row_num = 1
    for num in numbers_column_1:
        button = ttk.Button(root, text=num, style="TButton", command=lambda num=num: show_code(num))
        button.place(x=50, y=50 + row_num * 40)
        row_num += 1
    for num in numbers_column_2:
        button = ttk.Button(root, text=num, style="TButton", command=lambda num=num: show_code(num))
        button.place(x=200, y=50 + row_num * 40)
        row_num += 1

create_buttons()

# نمایش کد تمرین با رنگ‌بندی سینتکس
def show_code(exercise_number):
    file_path = os.path.join("training_exercises", f"{exercise_number}.py")  # مسیر فایل تمرین
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()
    except FileNotFoundError:
        code = f"فایل تمرین {exercise_number} پیدا نشد!"
    
    # نمایش کد در پنجره جدید با رنگ‌بندی سینتکس
    code_window = tk.Toplevel(root)
    code_window.title(f"کد تمرین {exercise_number}")
    
    text_widget = tk.Text(code_window, wrap="word", font=("Fira Code", 12), width=80, height=20)
    text_widget.pack(padx=20, pady=20)
    
    # استفاده از HtmlFormatter برای رنگ‌بندی کد
    formatter = HtmlFormatter(style='colorful', full=True, linenos=True)
    highlighted_code = highlight(code, PythonLexer(), formatter)
    
    text_widget.insert(tk.END, highlighted_code)

    run_button = ttk.Button(code_window, text="اجرای کد", command=lambda: run_code(file_path, code_window))
    run_button.pack(pady=10)

# اجرای کد و نمایش خروجی
def run_code(file_path, code_window):
    try:
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        show_output_window(result.stdout, code_window)
    except Exception as e:
        show_output_window(f"خطا در اجرا: {e}", code_window)

# نمایش خروجی در پنجره جدید
def show_output_window(output, parent_window):
    output_window = tk.Toplevel(parent_window)
    output_window.title("خروجی کد")
    output_text = tk.Text(output_window, wrap="word", font=("Fira Code", 12), height=10, width=80)
    output_text.insert(tk.END, output)
    output_text.pack(padx=20, pady=20)

# جستجو در لیست تمرین‌ها
search_entry = tk.Entry(root, font=("Fira Code", 12))
search_entry.pack(pady=10)

def search():
    query = search_entry.get().strip()
    if query:
        filtered_exercises = [num for num in numbers_column_1 + numbers_column_2 if query in num]
        print("تمرین‌های مرتبط:", filtered_exercises)

search_button = ttk.Button(root, text="جستجو", style="TButton", command=search)
search_button.pack(pady=10)

# اجرای برنامه
root.mainloop()
