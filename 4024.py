# هدف: معرفی روش‌های مختلف برای پیمایش در پایتون، شامل پیمایش لیست‌ها، دیکشنری‌ها و استفاده از توابع range، enumerate، break و continue


# پیمایش بر روی یک لیست
name = ["علی", "سحر", "سارا"]
for name in name:
    print(name)

# استفاده از range() برای تولید اعداد
for i in range(5):
    print(i)

# پیمایش بر روی دیکشنری
dict = {"نام": "رز", "سن": 19, "شهر": "نیویورک"}
for key in dict:
    print(key, ":", dict[key])

# استفاده از enumerate() برای دریافت اندیس و مقدار
colors = ["قرمز", "سبز", "آبی", "مشکی"]
for index, color in enumerate(colors):
    print(index, color)

# استفاده از break برای خروج از حلقه
for i in range(10):
    if i == 5:
        break
    print(i)

# استفاده از continue برای پرش به مرحله بعدی
for i in range(17):
    if i % 2 == 1:
        continue
    print(i)

word = "آناناس"
for letter in word:
    if letter == "ا":
        continue
    print(letter)

# استفاده از continue در شرایط پیچیده‌تر
numbers = [2, 5, 12, 18, 9, 39, 11, 32, 21]
for num in numbers:
    if num < 10 or num % 2 == 0:
        continue
    print(num)
