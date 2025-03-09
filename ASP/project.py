import tkinter as tk
import subprocess
import os

# مسیر پوشه تمرینات
exercises_folder = "training_exercises"

# لیست شماره‌ها برای دو ستون
numbers_column_1 = [
    "4001", "4002", "4003", "4004", "4005", "4010", "4011", "4012", "4013", "4014", "4015", "4016", "4017", "4018", "4019", "4020", "4021", "4022", "4023", "4024", "4025", "4028", "4029"
]
numbers_column_2 = [
    "4031", "4032", "4033", "4035", "4040", "4041", "4042", "4043", "4044", "4045", "4046", "4091", "4092", "4093", "4094", "4095", "4097", "4098", "4099", "4104", "4105", "4106"
]

# تابع برای خواندن محتویات فایل تمرین
def read_exercise_code(exercise_number):
    file_path = os.path.join(exercises_folder, f"{exercise_number}.py")
    
    # بررسی اینکه آیا فایل وجود دارد یا خیر
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
        return code
    else:
        return f"فایل برای تمرین {exercise_number} پیدا نشد!"

# تابع برای نمایش کد در پنجره و اجرای آن
def show_and_run_exercise(exercise_number):
    code = read_exercise_code(exercise_number)
    
    # ایجاد پنجره جدید برای نمایش کد
    code_window = tk.Toplevel(root)
    code_window.title(f"کد تمرین {exercise_number}")
    
    # ایجاد ویجت Text برای نمایش کد
    code_text = tk.Text(code_window, wrap="word", width=60, height=20)
    code_text.insert(tk.END, code)
    code_text.pack(padx=10, pady=10)
    
    # اضافه کردن ویجت برای نمایش خروجی
    output_label = tk.Label(code_window, text="خروجی کد:")
    output_label.pack(pady=5)

    # دکمه برای اجرای کد
    def run_code():
        try:
            # ایجاد یک محیط محصور برای اجرای کد
            exec_globals = {}
            exec(code, exec_globals)
            result = exec_globals.get('result', 'هیچ خروجی‌ای وجود ندارد.')
            output_label.config(text=f"خروجی کد: {result}")
        except Exception as e:
            output_label.config(text=f"خطا در اجرای کد: {e}")
    
    run_button = tk.Button(code_window, text="اجرای کد", command=run_code)
    run_button.pack(pady=5)

# ساخت پنجره اصلی
root = tk.Tk()
root.title("تمرینات پایتون")

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

# لیست دکمه‌ها برای ستون اول
for i, num in enumerate(numbers_column_1):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num: show_and_run_exercise(num))
    button.grid(row=i+2, column=0, padx=5, pady=5)

# لیست دکمه‌ها برای ستون دوم
for i, num in enumerate(numbers_column_2):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num: show_and_run_exercise(num))
    button.grid(row=i+2, column=1, padx=5, pady=5)

# قابلیت اسکرول موس
def on_mouse_wheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# نمایش پنجره
root.mainloop()
