import pymongo

from functions.image.download_image import download_image
from functions.image.image_to_bytes import image_to_bytes
from functions.image.processed_image_path import (image_path_to_s3_url,
                                                  processed_image_path)
from functions.image.resize_image import resize_image_by_max_width

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


def get_cursor(brand_keyname):
    return client.alloff_prod.products.find(
        {
            "removed": False,
            "productinfo.brand.keyname": brand_keyname,
        }
    )


def get_resized_image(url, basewidth):
    image = download_image(url)
    return image_to_bytes(resize_image_by_max_width(image, basewidth))


def make_new_path(url, size):
    path_nodes = url.split("/")
    original_filename = path_nodes[-1]
    nodes = original_filename.split(".")
    name = ".".join(nodes[:-1])
    ext = nodes[-1]
    filename = f"{name}__RESIZED-{size}.{ext}"
    s3_path = f"images/{filename}"
    return s3_path


def resize(url):
    image_bytes = get_resized_image(url, BASEWIDTH)
    new_path = processed_image_path(url, f"mw{BASEWIDTH}")
    with default_storage.open(new_path, "wb") as f:
        f.write(image_bytes)
    return image_path_to_s3_url(new_path)


def resize_document(doc):
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


def process_images(brand_keyname):
    start = time.time()
    cursor = get_cursor(brand_keyname)
    count = cursor.count()
    counter = 0
    for doc in get_docs(cursor):
        counter += 1
        resize_document(doc)
        print(f"{counter}/{count} DONE")
    end = time.time()
    print(f">>> 처리 총 소요 시간: {end - start}")
