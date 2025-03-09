import tkinter as tk
import json

# فایل برای ذخیره‌سازی شماره‌ها
data_file = "numbers_data.json"

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
    # دو بار کلیک روی شماره
    def open_entry_field(event):
        entry_field = tk.Entry(frame, width=10)
        entry_field.insert(0, number)  # قرار دادن شماره فعلی در Entry
        entry_field.grid(row=button_index+2, column=column, padx=5, pady=5)
        entry_field.focus()

        # تابع برای ثبت تغییرات
        def update_entry(event, entry_field, button, button_index):
            new_number = entry_field.get()
            if new_number.isdigit():  # اگر شماره عددی بود
                button.config(text=new_number)  # به‌روزرسانی دکمه با شماره جدید
                # به‌روزرسانی شماره‌ها در لیست
                if column == 0:
                    numbers_column_1[button_index] = new_number
                else:
                    numbers_column_2[button_index] = new_number
                save_numbers()  # ذخیره شماره‌ها پس از تغییر
            entry_field.destroy()  # حذف فیلد ورود شماره پس از تغییر
            click_counts[button_index] = 0  # ریست شمارنده کلیک‌ها پس از ثبت تغییر

        # افزودن شنونده برای زدن Enter
        entry_field.bind("<Return>", lambda event, entry_field=entry_field, button=(buttons_column_1 if column == 0 else buttons_column_2)[button_index], button_index=button_index: update_entry(event, entry_field, button, button_index))

    # زمانی که روی دکمه کلیک می‌شود، دو بار کلیک شمرده شود
    click_counts[button_index] += 1
    if click_counts[button_index] == 2:  # اگر دو بار کلیک شده باشد
        open_entry_field(None)

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

# شمارش کلیک‌ها برای هر دکمه
click_counts = []

# پر کردن دکمه‌ها و شماره‌ها برای ستون اول
for i, num in enumerate(numbers_column_1):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num, i=i, col=0: on_button_click(num, i, col))
    button.grid(row=i+2, column=0, padx=5, pady=5)
    buttons_column_1.append(button)

    # دکمه‌ها برای ویرایش شماره
    click_counts.append(0)

# پر کردن دکمه‌ها و شماره‌ها برای ستون دوم
for i, num in enumerate(numbers_column_2):
    button = tk.Button(frame, text=num, width=10, height=2, fg="blue", command=lambda num=num, i=i, col=1: on_button_click(num, i, col))
    button.grid(row=i+2, column=2, padx=5, pady=5)
    buttons_column_2.append(button)

    # دکمه‌ها برای ویرایش شماره
    click_counts.append(0)

# قابلیت اسکرول موس
def on_mouse_wheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# نمایش پنجره
root.mainloop()
