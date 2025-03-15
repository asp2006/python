# هدف: معرفی و کار با مجموعه‌ها در پایتون، شامل افزودن، حذف عناصر، عملیات مختلف مانند اتحاد، اشتراک، تفاضل و تفاضل متقارن، همچنین بررسی زیرمجموعه و فوق‌مجموعه


# افزودن عناصر به مجموعه :
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)
my_set.add(6)
my_set.add(1)  # 1 قبلاً وجود داشت، مجموعه‌ها از عناصر تکراری جلوگیری می‌کنند
print(my_set)

# حذف عناصر از مجموعه :
my_set = {1, 2, 3, 3, 4}
my_set.remove(3)  # حذف عنصر 3
print(my_set)

# غیرقابل ترتیب بودن مجموعه‌ها :
my_set = {1, 2, 3, 4, 5}
try:
    print(my_set[0])  # تلاش برای دسترسی به عنصر با استفاده از ایندکس
except TypeError as e:
    print("خطا:", str(e))  # چاپ پیام خطا به فارسی

# توانایی پذیرش انواع مختلف داده‌ها :
my_set = {1, 2, 1.84, "hola", (1, 2, 3)}
print(my_set)

# عملیات روی مجموعه‌ها :
# اتحاد (Union) :
set_a = {1, 2, 3}
set_b = {4, 5, 6}
union_set = set_a | set_b  # اتحاد دو مجموعه
print("اتحاد:", union_set)

# اشتراک (Intersection) :
set_1 = {1, 2, 2, 3, 4}
set_2 = {2, 4, 5, 6}
intersection_set = set_1 & set_2  # اشتراک دو مجموعه
print("اشتراک:", intersection_set)

# تفاضل (Difference) :
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}
difference_set = set_a - set_b  # تفاضل دو مجموعه
print("تفاضل:", difference_set)

# تفاضل متقارن (Symmetric Difference) :
symmetric_difference_set = set_a ^ set_b  # تفاضل متقارن دو مجموعه
print("تفاضل متقارن:", symmetric_difference_set)

# زیرمجموعه و فوق‌مجموعه (Subset and Superset) :
sepid_python1 = {"sharifi", "salimi", "salemi", "yavari"}
sepid_python2 = {"salemi", "sharifi"}
is_subset = sepid_python2.issubset(sepid_python1)  # بررسی اینکه آیا sepid_python2 زیرمجموعه sepid_python1 است؟
is_superset = sepid_python1.issuperset(sepid_python2)  # بررسی اینکه آیا sepid_python1 فوق‌مجموعه sepid_python2 است؟
print("آیا sepid_python2 زیرمجموعه sepid_python1 است؟", is_subset)
print("آیا sepid_python1 فوق‌مجموعه sepid_python2 است؟", is_superset)
