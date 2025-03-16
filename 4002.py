# هدف: نمایش مثال‌هایی از استفاده‌های مختلف تابع print() در پایتون:

    # Objects: نمایش یک عبارت ساده.
   # Sep: استفاده از پارامتر sep برای تعیین جداکننده بین اجزای چاپ شده.
    # End: تغییر رفتار انتهای خط با استفاده از پارامتر end.
    # Flush: چاپ فوری و بدون تأخیر با استفاده از پارامتر flush.
     # File: چاپ محتوا در یک فایل به جای صفحه نمایش.
    # چاپ مقادیر متغیرها همراه با متن ثابت برای نمایش اطلاعات.

# پارامترها

# Objects :
print("hello world 2023")

# Sep :
print("hello", "world", sep="-")

# End :
print("hello,", end="")
print("world")

# flush :
print("immediate Output", flush=True)

# file :
with open('Output.txt', 'w') as f:
    print("Hello, File!", file=f)

name = "Alice"
age = 30
print("Name:", name, " Age:", age)
