import requests
from bs4 import BeautifulSoup
import pymongo

# اتصال به MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # اتصال به سرور MongoDB
db = client["mydatabase"]  # دیتابیس مورد نظر
collection = db["python_versions"]  # کلکسیون مورد نظر برای ذخیره داده‌ها

# URL سایت پایتون که داده‌ها از آن استخراج می‌شود
url = "https://www.python.org/downloads/"  # صفحه دانلودها در سایت رسمی پایتون

# ارسال درخواست HTTP برای دریافت داده‌ها از سایت
response = requests.get(url)

# بررسی وضعیت درخواست
if response.status_code == 200:
    print("درخواست موفقیت‌آمیز بود!")
    
    # استخراج محتوای HTML صفحه
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # پیدا کردن نسخه‌های پایتون از صفحه (سایت پایتون معمولاً نسخه‌های مختلف را در این صفحه نمایش می‌دهد)
    versions = soup.find_all('span', class_='release-version')  # استخراج نسخه‌های موجود
    
    # استخراج و ذخیره داده‌ها در MongoDB
    for version in versions:
        version_text = version.get_text().strip()  # متن نسخه استخراج شده
        if version_text:  # اگر داده‌ای وجود داشت
            # ساخت یک دیکشنری از داده استخراج شده
            data_object = {
                "version": version_text,
                "url": url
            }
            
            # ذخیره داده‌ها در MongoDB
            collection.insert_one(data_object)
            print(f"داده‌ها ذخیره شدند: {data_object}")

    print("تمامی داده‌ها به MongoDB ذخیره شدند.")
else:
    print("خطا در دریافت داده‌ها از سایت. وضعیت:", response.status_code)
