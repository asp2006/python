from pymongo import MongoClient


# اتصال به MongoDB :
client = MongoClient("mongodb://localhost:27017")
# دسترسی به پایگاه داده :
db = client['my_new_database']
# دسترسی به کالکشن :
collection = db['my_new_collection']
# درج سند در کالکشن :
document = {"name": "Sara", "age": 30, "city": "Tehran"}
collection.insert_one(document)
# نمایش لیست پایگاه داده‌ها :
print(client.list_database_names())
# نمایش لیست کالکشن‌ها در پایگاه داده :
print(db.list_collection_names())
# بستن اتصال :
client.close()