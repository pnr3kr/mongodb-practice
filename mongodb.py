from pymongo import MongoClient

client = MongoClient("mongodb+srv://ds2022:sds_class27@cluster0.m3fek.mongodb.net/")

db = client["pnr3kr"]

collection = db["my_collection"]

documents = [
    {"name": "John", "age": 15, "hobby": "track"},
    {"name": "Gabe", "age": 30, "hobby": "swimming"},
    {"name": "Charlie", "age": 35, "hobby": "hiking"},
    {"name": "Claire", "age": 28, "hobby": "gaming"},
    {"name": "Penny", "age": 18, "hobby": "cooking"},
]
collection.insert_many(documents)

results = collection.find().limit(3)

print("Documents:")
for doc in results:
    print(doc)
