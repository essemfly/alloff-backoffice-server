# 2022-04-27 by @steve.c
# filename, extension이 제대로 url에서 파싱되지 않는 경우가 있었음
# 예: https://ak-media.theory.com/i/theory/TO_J019601R_001_0?$TO-pdp-large-desktop$
# 이때 https://alloff.s3.ap-northeast-2.amazonaws.com/images/__RESIZE-mw1280.webp로만 캐싱되고 있었음.
# cache할 때 파일 이름의 원본을 보존하지 않고 random string으로만 넣도록 개선하였고,
# 이전에 문제가 되었던 데이터를 복구하는 script.

import pymongo
from bson import ObjectId
from pymongo.database import Database

PROBLEMATIC_IMAGE = (
    "https://alloff.s3.ap-northeast-2.amazonaws.com/images/__RESIZE-mw1280.webp"
)
PROBLEMATIC_THUMBNAIL = (
    "https://alloff.s3.ap-northeast-2.amazonaws.com/images/__THUMB-mw300.webp"
)


def fix_product_infos(db: Database):
    print("fix_product_infos")
    collection = db["product_infos"]
    cursor = collection.find({"images": PROBLEMATIC_IMAGE})
    count = cursor.count()
    for index, doc in enumerate(cursor):
        new_images = [x for x in doc["images"] if x != PROBLEMATIC_IMAGE]
        collection.update_one({"_id": doc["_id"]}, {"$set": {"images": new_images}})
        print(f"[{index+1}/{count}]", doc["_id"], "DONE")


def fix_nested_product_infos(db: Database):
    print("fix_nested_product_infos")
    collection = db["products"]
    cursor = collection.find({"productinfo.images": PROBLEMATIC_IMAGE})
    count = cursor.count()
    for index, doc in enumerate(cursor):
        new_images = [x for x in doc["images"] if x != PROBLEMATIC_IMAGE]
        collection.update_one(
            {"_id": doc["_id"]}, {"$set": {"productinfo.images": new_images}}
        )
        print(f"[{index+1}/{count}]", doc["_id"], "DONE")


def fix_nested_products(db: Database):
    print("fix_nested_products")
    collection = db["products"]
    cursor = collection.find({"images": PROBLEMATIC_IMAGE})
    count = cursor.count()
    for index, doc in enumerate(cursor):
        ok_images = [x for x in doc["images"] if x != PROBLEMATIC_IMAGE]
        new_images = doc.get("productinfo", {}).get("images", []) + ok_images
        collection.update_one({"_id": doc["_id"]}, {"$set": {"images": new_images}})
        print(f"[{index+1}/{count}]", doc["_id"], "DONE")


# 위까지 돌리고 나니 이미지가 빈 친구들이 생겨서 fix.
def fix_empty_images(db: Database):
    print("fix_empty_images")
    collection = db["products"]
    cursor = collection.find({"images": []})
    count = cursor.count()

    for index, doc in enumerate(cursor):
        product_info_images = doc.get("productinfo", {}).get("images", [])
        product_info_is_empty = len(product_info_images) == 0
        if product_info_is_empty:
            original_info = db["product_infos"].find_one(
                {"_id": doc["productinfo"]["_id"]}
            )
            product_info_images = original_info.get("images", [])
        res = collection.update_one(
            {"_id": doc["_id"]}, {"$set": {"images": product_info_images}}
        )
        print(f"[{index+1}/{count}]", doc["_id"], "DONE")


# 요 바로 위에껄 돌리고 나니 product_info가 비어있는 부분을 안 채워준 게 생각나서 fix.


def fix_empty_product_info_images(db: Database):
    print("fix_empty_product_info_images")
    collection = db["products"]
    cursor = collection.find({"productinfo.images": []})
    count = cursor.count()

    for index, doc in enumerate(cursor):
        original_info = db["product_infos"].find_one({"_id": doc["productinfo"]["_id"]})
        product_info_images = original_info.get("images", [])
        res = collection.update_one(
            {"_id": doc["_id"]}, {"$set": {"productinfo.images": product_info_images}}
        )
        print(f"[{index+1}/{count}]", doc["_id"], "DONE")


# Description images도 고장나있음.
def fix_description_images(db: Database):
    print("fix_description_images")
    collection = db["products"]
    cursor = collection.find({"salesinstruction.description.images": PROBLEMATIC_IMAGE})
    count = cursor.count()

    for index, doc in enumerate(cursor):
        product_info_images = doc.get("productinfo", {}).get("images", [])
        ok_images = [
            x
            for x in doc["salesinstruction"]["description"]["images"]
            if x != PROBLEMATIC_IMAGE
        ]
        collection.update_one(
            {"_id": doc["_id"]},
            {
                "$set": {
                    "salesinstruction.description.images": product_info_images
                    + ok_images
                }
            },
        )
        print(f"[{index+1}/{count}]", doc["_id"], "DONE")


# Thumbnail image도 고장남
def fix_thumbnail_images(db: Database):
    print("fix_thumbnail_images")
    collection = db["products"]
    cursor = collection.find({"thumbnailimage": PROBLEMATIC_THUMBNAIL})
    count = cursor.count()

    for index, doc in enumerate(cursor):
        collection.update_one({"_id": doc["_id"]}, {"$unset": {"thumbnailimage": ""}})
        print(f"[{index+1}/{count}]", doc["_id"], "DONE")


def run(mongo_uri):
    client = pymongo.MongoClient(mongo_uri)
    db = client["alloff_prod"]
    # fix_product_infos(db)
    # fix_nested_product_infos(db)
    # fix_nested_products(db)
    # fix_empty_images(db)
    # fix_empty_product_info_images(db)
    fix_description_images(db)
    fix_thumbnail_images(db)
