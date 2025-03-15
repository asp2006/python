# هدف: نمایش نحوه ویرایش رکوردها در MongoDB با استفاده از دستور update_many برای تغییر مقادیر در چندین رکورد مطابق با شرایط خاص.


from pymongo import MongoClient

# اتصال به MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['my_new_database']
collection = db['my_new_collection']

# ویرایش یک رکورد (براساس مقدار موجود در فیلد "name")
filter = {"name": "Fatemeh","city": "Abadan" }  # شرط برای پیدا کردن رکورد
update = {"$set": {"age": 43}}  # تغییرات جدید
filter1 = {"city": "Abadan"}
update1 = {"$set": {"country": "Iran"}}
# اجرا
result = collection.update_many(filter, update)
result = collection.update_many(filter1, update1)

# نمایش تعداد رکوردهای ویرایش شده
print("Modified count:", result.modified_count)
# بازیابی رکوردهای ویرایش شده
for record in collection.find():
    print(record)

# بستن اتصال
client.close()
