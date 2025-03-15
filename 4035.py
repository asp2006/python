# هدف: نمایش نحوه استفاده از کتابخانه‌ی NumPy برای ایجاد آرایه‌ها، انجام عملیات‌های ریاضیاتی و دسترسی به عناصر آرایه.


# نحوه استفاده از NumPy برای ایجاد و کار با آرایه‌ها
# ایجاد آرایه‌ها :
import numpy as np
array = np.array([1,2,3,4,5])
print("Array:", array)

# انجام عملیات‌های ریاضیاتی :
sum_of_element = np.sum(array)
print("Sum of elements:", sum_of_element)

mean_of_elements = np.mean(array)
print("Mean of elements:", mean_of_elements)

# دسترسی به عناصر آرایه :
print("First element:", array[2])
