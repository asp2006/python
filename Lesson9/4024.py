# پیمایش بر روی یک لیست
name = ["ali","sahar","sara"]
for name in name:
    print(name)
# استفاده از range() برای تولید اعداد
for i in range(5):
    print(i)
#  پیمایش بر روی دیکشنری
dict = {"name": "rose", "age": 19, "city": "New York"}
for key in dict:
    print(key, ":", dict[key])
# استفاده از enumerate() برای دریافت اندیس و مقدار
colors = ["red", "green","blue","black"]
for index, colors in enumerate(colors):
    print(index,colors)
# استفاده از break و continue
for i in range(10):
    if i == 5 :
        break
    print(i)
# continue
for i in range(17):
    if i % 2 ==1 :
        continue
    print(i)
word = "ananas"
for letter in word:
   if letter =="a":
       continue
   print(letter) 
# استفاده از continue در شرایط پیچیده‌تر
numbers = [2, 5, 12, 18, 9, 39, 11,  32, 21]
for num in numbers:
    if num < 10 or num % 2 == 0:
        continue
    print(num)
