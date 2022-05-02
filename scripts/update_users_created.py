# 2022-04-27 by @steve.c
# 유저의 created 값이 일정 기간동안 들어가지 않고 있었던 문제를 ObjectId 파싱을 통해 고침.
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
