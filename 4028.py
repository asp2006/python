# هدف: نمایش مثال‌هایی از تبدیل داده‌ها در پایتون با استفاده از توابع مختلف مانند int() و float() 


# مثال‌های تابع int() :

# تبدیل رشته به عدد صحیح مثبت :
num_str = "567"
num = int(num_str)
print(num)

# تبدیل رشته به عدد صحیح منفی :
num_str = "-99"
num = int(num_str)
print(num)

# تبدیل عدد اعشاری به عدد صحیح :
num_float = 84.98
num = int(num_float)
print(num)

# تبدیل رشته‌ای که شامل کاراکترهای غیر عددی است :
try:
    invalid_str = "123abc"
    num = int(invalid_str)
except ValueError:
    print("invalid_str")

# هگزادسیمال (پایه 16) :
hex_str = "2A"
num = int(hex_str, base=16)
print(num)

# تبدیل به boolean :
print(bool(0))
print(bool(42))

# تبدیل رشته به عدد اعشاری :
num_str = "42.5"
num = float(num_str)
print(num)

# تبدیل عدد صحیح به عدد اعشاری :
num_int = 10
num = float(num_int)
print(num)

# تبدیل به float صفر :
num = float()
print(num)


