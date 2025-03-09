import tkinter as tk
import requests
import io
import sys

# آدرس مخزن GitHub
GITHUB_RAW_URL = "https://raw.githubusercontent.com/asp2006/python/master/"

# لیست شماره‌ها با ترتیب جدید برای هر ستون
first_column_numbers = [
    "4001", "4002", "4003", "4004", "4005", "4010", "4011", "4012", "4013", "4014",
    "4015", "4016", "4017", "4018", "4019", "4020", "4021", "4022", "4023", "4024",
    "4025", "4028", "4029"
]

second_column_numbers = [
    "4031", "4032", "4033", "4035", "4040", "4041", "4042", "4043", "4044", "4045",
    "4046", "4091", "4092", "4093", "4094", "4095", "4097", "4098", "4099", "4104",
    "4105", "4106"
]

# تابع برای دریافت کد تمرین از GitHub
def get_exercise_code(exercise_number):
    url = f"{GITHUB_RAW_URL}{exercise_number}.py"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"خطا در بارگذاری تمرین {exercise_number}: {e}"

# تابع برای نمایش و اجرای کد
def show_and_run_exercise(exercise_number):
    code = get_exercise_code(exercise_number)

    # ایجاد پنجره جدید برای نمایش کد
    code_window = tk.Toplevel(root)
    code_window.title(f"کد تمرین {exercise_number}")
    code_window.geometry("650x600")  # اندازه پنجره جدید را بزرگ‌تر کردیم

    # ایجاد یک Canvas برای اضافه کردن اسکرول در پنجره کد
    code_canvas = tk.Canvas(code_window)
    code_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ایجاد یک Scrollbar برای پنجره کد
    scrollbar = tk.Scrollbar(code_window, orient="vertical", command=code_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    # تنظیم اسکرول برای Canvas پنجره کد
    code_canvas.config(yscrollcommand=scrollbar.set)

    # ایجاد ویجت Text برای نمایش کد
    code_text = tk.Text(code_canvas, wrap="word", width=80, height=20)  # افزایش عرض و ارتفاع
    code_text.insert(tk.END, code)
    code_text.pack(padx=10, pady=10)

    # اضافه کردن ویجت برای نمایش خروجی
    output_label = tk.Label(code_canvas, text="خروجی کد:")
    output_label.pack(pady=5)

    # دکمه برای اجرای کد
    def run_code():
        try:
            # استفاده از io.StringIO برای ذخیره خروجی‌های print
            old_stdout = sys.stdout  # ذخیره وضعیت فعلی خروجی
            new_stdout = io.StringIO()  # خروجی جدید به صورت رشته
            sys.stdout = new_stdout  # تغییر مسیر خروجی به رشته

            exec(code)  # اجرای کد

            # بازیابی خروجی‌ها
            result = new_stdout.getvalue()  # تمام متن خروجی
            sys.stdout = old_stdout  # بازگشت به وضعیت قبلی خروجی

            if result == "":
                output_text.delete(1.0, tk.END)  # حذف متن قبلی
                output_text.insert(tk.END, "هیچ خروجی‌ای از کد برنخاست.")
            else:
                output_text.delete(1.0, tk.END)  # حذف متن قبلی
                output_text.insert(tk.END, result)  # نمایش خروجی کد

        except Exception as e:
            output_text.delete(1.0, tk.END)  # حذف متن قبلی
            output_text.insert(tk.END, f"خطا در اجرای کد: {e}")  # نمایش خطا

    run_button = tk.Button(code_canvas, text="اجرای کد", command=run_code)
    run_button.pack(pady=5)

    # ایجاد ویجت Text برای نمایش خروجی به همراه اسکرول
    output_text = tk.Text(code_canvas, wrap="word", width=80, height=15)  # بزرگ‌تر کردن
    output_text.pack(padx=10, pady=10)

    output_scrollbar = tk.Scrollbar(code_window, orient="vertical", command=output_text.yview)
    output_scrollbar.pack(side=tk.RIGHT, fill="y")
    output_text.config(yscrollcommand=output_scrollbar.set)

# ساخت پنجره اصلی
root = tk.Tk()
root.title("تمرینات پایتون")
root.geometry("450x600")  # ابعاد پنجره اصلی را تنظیم می‌کنیم

# اضافه کردن عنوان در بالای صفحه
title_label = tk.Label(root, text="لیست تمرینات پایتون", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# ایجاد یک Canvas برای جدول بدون اسکرول در پنجره اصلی
canvas = tk.Canvas(root, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# رسم خطوط جدول
row_height = 32.2  # ارتفاع هر ردیف
column_width = 70  # عرض هر ستون

# رسم خطوط افقی
for i in range(max(len(first_column_numbers), len(second_column_numbers)) + 1):
    canvas.create_line(0, i * row_height, column_width * 2, i * row_height, fill="black", width=1)

# رسم خطوط عمودی
for j in range(3):
    canvas.create_line(j * column_width, 0, j * column_width, row_height * max(len(first_column_numbers), len(second_column_numbers)), fill="black", width=1)

# قرار دادن شماره‌ها در ستون اول
all_number_labels = []
for i, num in enumerate(first_column_numbers):
    x = column_width // 2  # برای ستون اول
    y = (i * row_height) + (row_height // 2)
    number_label = tk.Label(root, text=num, font=("Arial", 12, "bold"), fg="blue", cursor="hand2")
    number_label.bind("<Button-1>", lambda event, num=num, label=number_label: on_number_click(event, num, label))
    canvas.create_window(x, y, window=number_label)
    all_number_labels.append(number_label)

# قرار دادن شماره‌ها در ستون دوم
for i, num in enumerate(second_column_numbers):
    x = column_width + (column_width // 2)  # برای ستون دوم
    y = (i * row_height) + (row_height // 2)
    number_label = tk.Label(root, text=num, font=("Arial", 12, "bold"), fg="blue", cursor="hand2")
    number_label.bind("<Button-1>", lambda event, num=num, label=number_label: on_number_click(event, num, label))
    canvas.create_window(x, y, window=number_label)
    all_number_labels.append(number_label)

# تابع برای کلیک روی شماره ها
def on_number_click(event, number, label):
    # بازگشت رنگ شماره‌های قبلی به حالت اولیه
    for lbl in all_number_labels:
        lbl.config(fg="blue")
    
    # تغییر رنگ شماره به قرمز هنگام کلیک
    label.config(fg="red")
    show_and_run_exercise(number)

# نمایش پنجره
root.mainloop()
