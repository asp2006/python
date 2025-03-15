# هدف: نمایش نحوه درج یک رکورد واحد و چند رکورد در MongoDB با استفاده از insert_one و insert_many و همچنین مدیریت خطاها.


# درج یک رکورد با insert_one :

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['my_new_database']
collection = db['my_new_collection']

# تعریف یک رکورد (document) برای درج
record = {"name": "Ali", "age": 19, "city": "Abadan"}
# درج رکورد در کالکشن
result = collection.insert_one(record)
print("Inserted IDs:", result.inserted_id)
# تعریف چند رکورد به صورت لیست از دیکشنری‌ها
records = [
    {"name": "Fatemeh", "age": 44, "city": "Abadan"},
    {"name": "Sahar", "age": 11, "city": "Abadan"},
    {"name": "Sara", "age": 10, "city": "Abadan"}
]
# درج چندین رکورد در کالکشن
result = collection.insert_many(records)
# نمایش شناسه‌های رکوردهای درج شده
print("Inserted IDs:", result.inserted_ids)
# مشاهده رکوردهای موجود در کالکشن
for record in collection.find():
    print(record)
client.close()


# مدیریت خطاها هنگام درج رکورد

# برای جلوگیری از مشکلات هنگام درج رکورد و مدیریت خطاها، می‌توانید از بلوک‌های try-except استفاده کنید تا خطاهای احتمالی به‌طور مناسب مدیریت شوند.

#try:
    #record = {"name": "Ali", "age": 25, "city": "Tehran"}
    #collection.insert_one(record)
    #print("Record inserted successfully!")
#except Exception as e:
    #print("An error occurred:", str(e))
