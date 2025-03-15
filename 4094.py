# هدف: نمایش نحوه حذف رکوردها از MongoDB با استفاده از دستورات delete_one و delete_many بر اساس شرایط خاص.


from pymongo import MongoClient

# اتصال به MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['my_new_database']
collection = db['my_new_collection']

# حذف یک رکورد با شرط
filter = {"name": "Ali"}
result = collection.delete_one(filter)

# نمایش تعداد رکوردهایی که حذف شدند
print("Deleted count:", result.deleted_count)
filter = {"city": "Abadan"}
result = collection.delete_many(filter)

# نمایش تعداد رکوردهایی که حذف شدند
print("Deleted count:", result.deleted_count)
# بستن اتصال
client.close()
