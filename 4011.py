# لیست فصول سال
seasons = [1, 2, 3, 4, 5]
print(seasons[0])  # چاپ اولین فصل
print(seasons[3])  # چاپ چهارمین فصل

# لیست اعداد (با مقادیر ناقص)
numbers = [1, 2, 3, 4, ...]
print(numbers)  # چاپ لیست اعداد

# لیست نوشیدنی‌ها
drinks = ["hipe", "glory", "monster"]
print(drinks)  # چاپ لیست نوشیدنی‌ها

# لیست ترکیب اعداد و رشته‌ها
str_int = [1, "word", 2]
print(str_int)  # چاپ لیست شامل اعداد و رشته‌ها

# لیست تو در تو
three = [[1, 2], ["S", "N"], ["list"]]
print(three)  # چاپ لیست تو در تو

# لیست خالی
vacant = []
print(vacant)  # چاپ لیست خالی

# چاپ اولین و چهارمین عنصر لیست numbers
print(numbers[0])  # چاپ اولین عنصر
print(numbers[3])  # چاپ چهارمین عنصر

# برش دادن یک رشته
asus = ("vivobook"[5])  # استخراج حرف ششم از رشته "vivobook"
print(asus)  # چاپ نتیجه

# اضافه کردن عنصر به یک لیست
letters = ["a", "c"]
letters.insert(1, "b")  # اضافه کردن "b" در موقعیت 1
print(letters)  # چاپ لیست پس از اضافه کردن

# حذف یک عنصر از لیست
letter = ["a", "b", "b"]
letter.remove("b")  # حذف اولین "b"
print(letter)  # چاپ لیست پس از حذف

# بررسی طول لیست تو در تو
lenn = [[], [], [], [], []]
print(len(lenn))  # چاپ طول لیست تو در تو

# معکوس کردن ترتیب عناصر لیست
year = [6, 0, 0, 2]
year.reverse()  # معکوس کردن ترتیب
print(year)  # چاپ لیست معکوس شده

# مرتب کردن لیست
letters = ["d", "c", "z", "a", "b"]
letters.sort()  # مرتب کردن لیست حروف
print(letters)  # چاپ لیست مرتب شده

# حذف عنصر از لیست با استفاده از اندیس
a = [1, 2, 2, 3, 4]
del a[2]  # حذف عنصر سوم (با اندیس 2)
print(a)  # چاپ لیست پس از حذف
