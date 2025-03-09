import tkinter as tk
import subprocess
import os

# مسیر پوشه تمرینات
exercises_folder = "training_exercises"

# لیست شماره‌ها برای دکمه‌ها
exercise_numbers = [4001, 4002, 4003, 4004, 4005, 4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4018, 4019, 4020, 4021, 4022, 4023, 4024, 4025, 4028, 4029, 4031, 4032, 4033, 4035, 4040, 4041, 4042, 4043, 4044, 4045, 4046, 4091, 4092, 4093, 4094, 4095, 4097, 4098, 4099, 4104, 4105, 4106]

# تابع برای اجرای فایل تمرین
def run_exercise(exercise_number):
    file_path = os.path.join(exercises_folder, f"{exercise_number}.py")
    
    # بررسی اینکه آیا فایل وجود دارد یا خیر
    if os.path.isfile(file_path):
        # اجرای فایل پایتون
        subprocess.run(["python", file_path])
    else:
        print(f"فایل برای تمرین {exercise_number} پیدا نشد!")

# ساخت پنجره اصلی
root = tk.Tk()
root.title("تمرینات پایتون")

# ساخت دکمه‌ها برای هر شماره تمرین
for exercise_number in exercise_numbers:
    button = tk.Button(root, text=f"تمرین {exercise_number}", command=lambda num=exercise_number: run_exercise(num))
    button.pack(pady=5)

# شروع برنامه گرافیکی
root.mainloop()
