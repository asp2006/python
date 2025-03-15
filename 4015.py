# تعریف یک تاپل
my_tuple = (1, 2, "علی", 4, 6, 2006)

# دسترسی به عناصر تاپل
print(my_tuple[2])  # چاپ سومین عنصر (علی)
print(my_tuple[5])  # چاپ ششمین عنصر (2006)

# طول تاپل
print(len(my_tuple))  # چاپ طول تاپل

# پیمایش بر روی تاپل
for item in my_tuple:
    print(item)  # چاپ هر یک از عناصر تاپل

# بررسی وجود یک عنصر در تاپل
print(4 in my_tuple)  # آیا 4 در تاپل وجود دارد؟
print("world" in my_tuple)  # آیا "world" در تاپل وجود دارد؟

# تعریف تاپل تک‌عنصری
single_item_tuple = (1,)
print(type(single_item_tuple))  # نوع داده تاپل تک‌عنصری

# تعریف یک تاپل برای ذخیره اطلاعات یک مکان
location_info = ("نیویورک", 10001, "آمریکا")

# دسترسی به اطلاعات
city = location_info[0]  # نام شهر
postal_code = location_info[1]  # کد پستی
country = location_info[2]  # کشور

print("شهر:", city)
print("کد پستی:", postal_code)
print("کشور:", country)

# تلاش برای تغییر داده‌های تاپل (باعث خطا می‌شود)
try:
    location_info[1] = 20002  # تلاش برای تغییر کد پستی
except TypeError as e:
    print("خطا:", e)  # چاپ خطا در صورت تغییر ندادن داده

# تابع برای محاسبه مساحت و محیط یک مستطیل
def calculate_area_perimeter(length, width):
    area = length * width  # محاسبه مساحت
    perimeter = 2 * (length + width)  # محاسبه محیط

    # بازگشت مساحت و محیط در یک تاپل
    return area, perimeter

# فراخوانی تابع
area, perimeter = calculate_area_perimeter(5, 10)

# نمایش نتایج
print("مساحت:", area)
print("محیط:", perimeter)
