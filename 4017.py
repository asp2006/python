# هدف: معرفی نوع داده بولی (Boolean) در پایتون، استفاده در مقایسه‌ها، شرایط شرطی و تبدیل انواع داده‌ها به نوع بولی


x = True
y = False

print(x) 
print(y)  

# استفاده در مقایسه‌ها :
a = 5
b = 10
نتیجه = a > b
print(نتیجه)

# استفاده در شرایط شرطی :
بارش_باران = False
if بارش_باران:
    print("بارش باران در حال وقوع است")
else:
    print("بارش باران در حال وقوع نیست")

# تبدیل انواع داده‌ها به نوع بولی :
print(bool(''))  # تبدیل رشته خالی به بولین (False)
print(bool("hello"))  # تبدیل رشته غیرخالی به بولین (True)
print(bool([1, 2, 3]))  # تبدیل لیست غیرخالی به بولین (True)
