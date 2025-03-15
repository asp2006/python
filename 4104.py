# هدف: ایجاد یک فرم ورود ساده با استفاده از Tkinter که پس از ورود موفقیت‌آمیز، پنجره داشبورد جدیدی را نمایش می‌دهد.

import tkinter as tk
from tkinter import messagebox

# تابعی برای باز کردن پنجره جدید پس از ورود موفقیت‌آمیز
def open_dashboard():
    dashboard = tk.Tk()  # ایجاد پنجره جدید داشبورد
    dashboard.title("Dashboard")  # عنوان پنجره
    dashboard.geometry("300x200")  # اندازه پنجره
    
    # ایجاد یک برچسب (Label) برای نمایش خوشامدگویی در داشبورد
    lbl = tk.Label(dashboard, text="Welcome to the Dashboard", font=("Arial", 14))
    lbl.pack(pady=20)  # نمایش برچسب در پنجره
    
    dashboard.mainloop()  # اجرای حلقه اصلی پنجره داشبورد

# تابع بررسی اطلاعات ورود
def login():
    username = entry_username.get()  # دریافت نام کاربری وارد شده
    password = entry_password.get()  # دریافت رمز عبور وارد شده
    
    # بررسی مقادیر نام کاربری و رمز عبور
    if username == "admin" and password == "1234":  # اگر نام کاربری و رمز عبور صحیح باشد
        messagebox.showinfo("Login Success", "Welcome!")  # نمایش پیغام خوشامدگویی
        root.destroy()  # بستن پنجره فعلی
        open_dashboard()  # باز کردن پنجره داشبورد
    else:  # اگر نام کاربری یا رمز عبور اشتباه باشد
        messagebox.showerror("Login Failed", "Invalid Username or Password")  # نمایش پیغام خطا

# تعریف پنجره اصلی
root = tk.Tk()
root.title("Login Form")  # عنوان پنجره ورود
root.geometry("300x200")  # اندازه پنجره

# لیبل‌ها و فیلدهای ورود
label_username = tk.Label(root, text="Username:")  # ایجاد برچسب نام کاربری
label_username.pack(pady=5)  # نمایش آن در پنجره

entry_username = tk.Entry(root)  # ایجاد فیلد ورودی برای نام کاربری
entry_username.pack(pady=5)  # نمایش آن در پنجره

label_password = tk.Label(root, text="Password:")  # ایجاد برچسب رمز عبور
label_password.pack(pady=5)  # نمایش آن در پنجره

entry_password = tk.Entry(root, show="*")  # ایجاد فیلد ورودی برای رمز عبور (با ستاره)
entry_password.pack(pady=5)  # نمایش آن در پنجره

# دکمه ورود
btn_login = tk.Button(root, text="Login", command=login)  # ایجاد دکمه ورود و اتصال آن به تابع login
btn_login.pack(pady=10)  # نمایش آن در پنجره

root.mainloop()  # اجرای حلقه اصلی پنجره
