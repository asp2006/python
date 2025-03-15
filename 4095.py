# هدف: حذف کامل یک کالکشن از MongoDB و بستن اتصال پس از انجام عملیات.

# نکته: دستور `drop()` برای حذف کامل یک کالکشن از پایگاه داده MongoDB استفاده می‌شود.


from pymongo import MongoClient

# اتصال به MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['my_new_database']

# حذف کامل کالکشن
db['my_new_collection'].drop()

# بستن اتصال
client.close()


#from pymongo import MongoClient

# اتصال به MongoDB
#client = MongoClient("mongodb://localhost:27017")
#db = client['my_database']

# حذف کامل کالکشن
#db['my_collection'].drop()

# بررسی رکوردهای موجود در کالکشن (نباید هیچ رکوردی باشد)
#collection = db['my_collection']
#for record in collection.find():
 #   print(record)

# بستن اتصال
#client.close()
