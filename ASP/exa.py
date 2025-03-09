import tkinter as tk
import json

# فایل برای ذخیره‌سازی شماره‌ها و متن‌ها
data_file = "numbers_data.json"

# تابع برای بارگذاری شماره‌ها و متن‌ها از فایل
def load_data():
    try:
        with open(data_file, "r") as f:
            data = json.load(f)
            # اگر کلید "texts" وجود نداشت، یک دیکشنری خالی را برمی‌گردانیم
            return data.get("column_1", []), data.get("column_2", []), data.get("texts", {})
    except (FileNotFoundError, json.JSONDecodeError):
        # اگر فایل وجود نداشته باشد یا خراب باشد، شماره‌ها و متن‌های پیش‌فرض برمی‌گردد
        return [f"40{str(i).zfill(3)}" for i in range(1, 26)], [f"40{str(i+50).zfill(3)}" for i in range(1, 26)], {}

# تابع برای ذخیره شماره‌ها و متن‌ها در فایل
def save_data():
    data = {
        "column_1": numbers_column_1,
        "column_2": numbers_column_2,
        "texts": texts
    }
    with open(data_file, "w") as f:
        json.dump(data, f)

# تابع برای نشان دادن متن برای شماره انتخابی
def show_text_for_number(number, column):
    if number in texts:
        text_display.config(state=tk.NORMAL)  # فعال کردن فیلد متنی برای ویرایش
        text_display.delete(1.0, tk.END)  # حذف متن قبلی
        text_display.insert(tk.END, texts[number])  # نمایش متن مربوطه
        text_display.config(state=tk.NORMAL)  # حالت ویرایش فعال باشد
        current_number.set(number)  # ذخیره شماره فعلی که روی آن کلیک شده

# تابع برای ثبت و ذخیره متن جدید
def save_text(event):
    new_text = text_display.get(1.0, tk.END).strip()
    if new_text:  # اگر متن وارد شده خالی نباشد
        number = current_number.get()
        texts[number] = new_text
        save_data()
        show_text_for_number(number, None)  # نمایش متن جدید در فیلد متنی

# لیست‌های شماره‌ها و دیکشنری برای نگهداری متن‌ها
numbers_column_1, numbers_column_2, texts = load_data()

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

# ایجاد فیلد متنی برای وارد کردن و نمایش متن
text_display = tk.Text(root, height=10, width=50, wrap=tk.WORD)  # حالت ویرایش فعال است
text_display.pack(pady=10)

# متغیر برای ذخیره شماره فعلی که روی آن کلیک شده
current_number = tk.StringVar()

# پر کردن دکمه‌ها و شماره‌ها برای ستون اول
for i, num in enumerate(numbers_column_1):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num, col=0: show_text_for_number(num, col))
    button.grid(row=i+2, column=0, padx=5, pady=5)
    buttons_column_1.append(button)

# پر کردن دکمه‌ها و شماره‌ها برای ستون دوم
for i, num in enumerate(numbers_column_2):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num, col=1: show_text_for_number(num, col))
    button.grid(row=i+2, column=2, padx=5, pady=5)
    buttons_column_2.append(button)

# افزودن شنونده برای ثبت متن هنگام زدن Enter
text_display.bind("<Return>", save_text)

# قابلیت اسکرول موس
def on_mouse_wheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# نمایش پنجره
root.mainloop()
