# هدف: اتصال به MongoDB و درج داده‌ها در کالکشن‌های مختلف با استفاده از insert_many و مدیریت داده‌ها در دو کالکشن مجزا.

from pymongo import MongoClient
from datetime import datetime

# اتصال به MongoDB
client = MongoClient('mongodb://localhost:27017/')

# ایجاد یا اتصال به دیتابیس
db = client['my_new_database']

# ایجاد یا اتصال به کالکشن اول
collection1 = db['mongo4097']

# لیست داده‌ها برای کالکشن اول
complex_data_list = [
    {
        "نام": "علی", 
        "سن": 19, 
        "ایمیل": "proud.boy2006@gmail.com", 
        "تاریخ ثبت نام": datetime(2023, 5, 10), 
    },
    {
        "نام": "فاطمه", 
        "سن": 44, 
        "ایمیل": "ندارد", 
        "تاریخ ثبت نام": datetime(2022, 7, 22), 
    },
    {
        "نام": "سحر", 
        "سن": 11, 
        "ایمیل": "ندارد", 
        "تاریخ ثبت نام": datetime(2021, 9, 14),
    }
]

# درج داده‌ها در کالکشن اول
result1 = collection1.insert_many(complex_data_list)

# چاپ شناسه‌های درج شده در کالکشن اول
print("داده‌ها در mongo4097 با موفقیت درج شدند. شناسه‌ها:")
print(result1.inserted_ids)

# نمایش داده‌های ذخیره‌شده در کالکشن اول
print("داده‌های موجود در mongo4097:")
for doc in collection1.find():
    print(doc)

# ایجاد یا اتصال به کالکشن دوم
collection2 = db['ex2']

# لیست داده‌ها برای کالکشن دوم (اطلاعات گروه سپید پایتون)
project_list = [
    {
        "نام گروه": "سپید پایتون",
        # استفاده از تاریخ به صورت یکپارچه برای تاریخ‌ها
        "تاریخ شروع به کار گروه سپید پایتون": datetime(1403, 11, 25),  # به صورت یک تاریخ کامل
        "تاریخ به پایان رسیدن دوره های آموزشی مقدماتی": datetime(1403, 12, 9),  # به صورت یک تاریخ کامل
        "اعضای گروه سپید پایتون": [
            {"نام و نام خانوادگی": "ابوالفضل فرحانی"},
            {"نام و نام خانوادگی": "سحر خلاقی"},
            {"نام و نام خانوادگی": "جنان حمدی"},
            {"نام و نام خانوادگی": "مهدی نجفی"}
        ]
    }
]

# درج داده‌ها در کالکشن دوم (اطلاعات گروه سپید پایتون)
result2 = collection2.insert_many(project_list)

# چاپ شناسه‌های درج شده در کالکشن دوم
print("داده‌ها در ex2 با موفقیت درج شدند. شناسه‌ها:")
print(result2.inserted_ids)

# نمایش داده‌های ذخیره‌شده در کالکشن دوم
print("داده‌های موجود در ex2:")
for doc in collection2.find():
    print(doc)

# حالا می‌خواهیم داده‌های مربوط به شهر، تاریخ تولد و شغل را به کالکشن دوم اضافه کنیم
# این بخش مربوط به کالکشن دوم است.
job_data_list = [
    {
        "شهر": "آبادان", 
        "تاریخ تولد": datetime(2006, 3, 21),  # تاریخ میلادی (برای مثال)
        "شغل": "درحال تحصیل"
    },
    {
        "شهر": "اهواز", 
        "تاریخ تولد": datetime(2002, 3, 21),  # تاریخ میلادی (برای مثال)
        "شغل": "درحال تحصیل"
    },
    {
        "شهر": "خرمشهر", 
        "تاریخ تولد": datetime(1999, 3, 21),  # تاریخ میلادی (برای مثال)
        "شغل": "درحال تحصیل"
    },
    {
        "شهر": "شیراز", 
        "تاریخ تولد": datetime(2006, 3, 21),  # تاریخ میلادی (برای مثال)
        "شغل": "درحال تحصیل"
    }
]

# درج داده‌ها در کالکشن دوم (اطلاعات شغل و شهر)
result3 = collection2.insert_many(job_data_list)

# چاپ شناسه‌های درج شده در کالکشن دوم
print("داده‌ها در ex2 (شهر، تاریخ تولد و شغل) با موفقیت درج شدند. شناسه‌ها:")
print(result3.inserted_ids)

# نمایش داده‌های ذخیره‌شده در کالکشن دوم (شهر، تاریخ تولد و شغل)
print("داده‌های موجود در ex2 (شهر، تاریخ تولد و شغل):")
for doc in collection2.find():
    print(doc)

# بستن ارتباط با MongoDB
client.close()
