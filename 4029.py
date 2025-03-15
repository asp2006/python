# 1. استفاده از ماژول math و تابع sqrt:
import math
# محاسبه ریشه دوم عدد 16
result = math.sqrt(16)
print(result)  # خروجی: 4.0

# 2. تولید عدد تصادفی با ماژول random:
import random
# تولید یک عدد تصادفی بین 1 و 10
random_number = random.randint(1, 10)
print(random_number)

# انتخاب تصادفی یک میوه از لیست
fruit_list = ['سیب', 'موز', 'گیلاس']
random_fruit = random.choice(fruit_list)
print(random_fruit)

# 3. استفاده از ماژول datetime برای کار با تاریخ و زمان:
import datetime
# دریافت تاریخ و زمان فعلی
current_time = datetime.datetime.now()
print(current_time)  # خروجی: تاریخ و زمان فعلی

# ایجاد یک تاریخ خاص
specific_date = datetime.date(2023, 10, 10)
print(specific_date)  # خروجی: 2023-10-10

# 4. استفاده از ماژول os برای تعامل با سیستم فایل:
import os
# دریافت لیست فایل‌ها و دایرکتوری‌ها در دایرکتوری فعلی
files = os.listdir('.')
print(files)

# 5. استفاده از ماژول sys برای نمایش نسخه پایتون و آرگومان‌های خط فرمان:
import sys
# نمایش نسخه پایتون
print(sys.version)

# نمایش آرگومان‌های خط فرمان
print(sys.argv)

# 6. تبدیل داده‌ها با ماژول json:
import json
# ایجاد داده‌ها به صورت دیکشنری
data = {"name": "Ali", "age": 19, "city": "Abadan"}
# تبدیل دیکشنری به رشته JSON
json_data = json.dumps(data)
print(json_data)  # خروجی: {"name": "Ali", "age": 19, "city": "Abadan"}

# تبدیل رشته JSON به دیکشنری
loaded_data = json.loads(json_data)
print(loaded_data)  # خروجی: {'name': 'Ali', 'age': 19, 'city': 'Abadan'}

# 7. استفاده از ماژول re برای کار با عبارات منظم:
import re
# الگوی جستجو برای اعداد
pattern = r'\d+'  # جستجو برای اعداد
text = "There are 12 apples and 34 oranges."
matches = re.findall(pattern, text)
print(matches)  # خروجی: ['12', '34']

# 8. استفاده از ماژول requests برای ارسال درخواست HTTP:
import requests

# URL برای دریافت اطلاعات از CoinGecko
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

# ارسال درخواست GET به API CoinGecko
response = requests.get(url)

# بررسی وضعیت درخواست
if response.status_code == 200:
    print("درخواست موفقیت‌آمیز بود!")
    
    # دریافت داده‌ها به صورت JSON
    data = response.json()
    
    # استخراج قیمت بیت کوین از پاسخ
    bitcoin_price = data['bitcoin']['usd']
    print(f"قیمت بیت کوین: {bitcoin_price} USD")
else:
    print(f"خطا در دریافت داده: {response.status_code}")
