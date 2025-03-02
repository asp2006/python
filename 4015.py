my_tuple = (1, 2, "ali", 4, 6, 2006)
print(my_tuple[2])
print(my_tuple[5])

print(len(my_tuple))

# پیمایش بر روی تاپل :
for item in my_tuple:
    print(item)

# بررسی وجود عنصر در تاپل :
print(4 in my_tuple)
print("world" in my_tuple)

#  عریف تاپل تکی :
single_item_tuple = (1,)
print(type(single_item_tuple))

# تعریف یک تاپل برای ذخیره اطلاعات یک مکان :
location_info = ("New york", 10001, "USA")

# دسترسی به اطلاعات :
city = location_info[0]
postal_code = location_info[1]
country = location_info[2]

print("city:", city)
print("postal_code", postal_code)
print("country:", country)

try:
    location_info[1] = 20002
except TypeError as e:
    print("Error:", e)

# تابع برای محاسبه مساحت و محیط یک مستطیل :


def calculate_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)

    # بازگشت مساحت و محیط در یک تاپل :
    return area, perimeter


# فراخوانی تابع :
area, perimeter = calculate_area_perimeter(5, 10)


# نمایش نتایج :
print("Area:", area)
print("Perimeter:", perimeter)
