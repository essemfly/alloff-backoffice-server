import asyncio

import pymongo

client = pymongo.MongoClient(
    "mongodb://alloff:2morebutter@localhost:27019/?retryWrites=false"
)


import time
from io import BytesIO

import requests
from django.core.files.storage import default_storage
from PIL import Image, ImageOps

from alloff_backoffice_server.settings import S3_IMAGES_HOST

BASEWIDTH = 1280
# def get_cursor():
#     return client.alloff_prod.products.find(
#         {"removed": False, "images": {"$elemMatch": {"$regex": "https://alloff\.s3.*webp"}, "$not": {"$regex": ".*__RESIZED.*"}}}
#     )


def get_cursor():
    return client.alloff_prod.products.find(
        {
            "removed": False,
            "productinfo.brand.keyname": "TIME",
        }
    )


def get_resized_image(url, basewidth):
    res = requests.get(url)
    image = Image.open(BytesIO(res.content))
    image = ImageOps.exif_transpose(image).convert("RGB")
    wpercent = basewidth / float(image.size[0])
    hsize = int((float(image.size[1]) * float(wpercent)))
    resized_image = image.resize((basewidth, hsize), Image.LANCZOS)
    image_bytes = BytesIO()
    resized_image.save(fp=image_bytes, format="WEBP")
    image_bytes = image_bytes.getvalue()
    return image_bytes


def make_new_path(url, size):
    path_nodes = url.split("/")
    original_filename = path_nodes[-1]
    name, ext = original_filename.split(".")
    filename = f"{name}__RESIZED-{size}.{ext}"
    s3_path = f"images/{filename}"
    return s3_path


def resize(url):
    image_bytes = get_resized_image(url, BASEWIDTH)
    new_path = make_new_path(url, f"mw{BASEWIDTH}")
    with default_storage.open(new_path, "wb") as f:
        f.write(image_bytes)
    return f"{S3_IMAGES_HOST}/{new_path}"


async def resize_document(doc):
    if "images" not in doc:
        return
    images = doc["images"]
    if images is None:
        return
        
    should_resize = False
    for image in images:
        if "__RESIZED" not in image:
            should_resize = True
            break
    
    if not should_resize:
        return

    new_images = []
    for u in images:
        if "__RESIZED" in u:
            new_images.append(resize(u))
        else:
            result_url = resize(u)
            print(
                f"""{doc["productinfo"]["brand"]["keyname"]} {doc["alloffname"]} -> {result_url}"""
            )
            new_images.append(result_url)
    client.alloff_prod.products.update_one(
        {"_id": doc["_id"]}, {"$set": {"images": new_images, "isimagecached": True}}
    )
    return

def get_docs(cursor):
    return list(cursor)

async def process_async():
    start = time.time()
    cursor = get_cursor()
    print(cursor.count())
    await asyncio.wait([resize_document(doc) for doc in get_docs(cursor)])
    end = time.time()
    print(f">>> 비동기 처리 총 소요 시간: {end - start}")
