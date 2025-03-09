#  مثال برای استفاده از ماژول math و تابع sqrt :
import math
result = math.sqrt(16)
print(result)

# تولید عدد تصادفی با ماژول random :
import random 
random_number = random.randint(1, 10)
print(random_number)

sample_list = ['apple', 'banana', 'chery']
random_fruit = random.choice(sample_list)
print(random_fruit)

# استفاده از ماژول datetime برای کار با تاریخ و زمان :
# دریافت تاریخ و زمان فعلی
import datetime
now = datetime.datetime.now()
print(now)
#  ایجاد یک تاریخ خاص :
sepcific_date = datetime.date(2023,10,10)
print(sepcific_date)
 
 # استفاده از ماژول os برای تعامل با سیستم فایل :
import os
files = os.listdir('.')
print(files)

#  استفاده از ماژول sys برای نمایش نسخه پایتون و آرگومان‌های خط فرمان :
import sys
print(sys.version)
print(sys.argv)

# تبدیل داده‌ها با ماژول json :
import json
data = {"name": "ali", "age": 19, "city":"Abadan"}
json_data = json.dumps(data)
print(json_data)
load_data = json.loads(json_data)
print(load_data)

# استفاده از ماژول re برای کار با عبارات منظم :
import re
pattern = r'\d+'
text = "There are 12 apples and 34 oranges."
matches = re.findall(pattern, text)
print(matches)

# استفاده از ماژول requests برای ارسال درخواست HTTP :
import requests
reseponse = requests.get('https://chatgpt.com/')
print(reseponse.status_code)