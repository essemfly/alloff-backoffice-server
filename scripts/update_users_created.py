import pymongo
from bson import ObjectId

client = pymongo.MongoClient("")  # Insert your MongoDB connection string here
collection = client["alloff_prod"]["users"]
cursor = collection.find({"created": {"$exists": False}})
count = cursor.count()
for index, user in enumerate(cursor):
    _id: ObjectId = user["_id"]
    print(f"[{index+1}/{count}]", _id, _id.generation_time)
    collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"created": _id.generation_time}},
    )
