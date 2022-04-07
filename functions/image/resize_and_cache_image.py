from django.core.files.storage import default_storage
from functions.image.download_image import download_image
from functions.image.image_to_bytes import image_to_bytes
from functions.image.processed_image_path import (image_path_to_s3_url,
                                                  processed_image_path)
from functions.image.resize_image import resize_image_by_max_width


def resize_and_cache(url: str, size: int, suffix: str, resize_type: str = "mw") -> str:
    """
    Resizes and caches image from url.
    Returns the url to the cached image.
    """
    resized_image = resize_image_by_max_width(download_image(url), size)
    path = processed_image_path(url, f"{resize_type}{size}", suffix=suffix, ext="webp")
    with default_storage.open(path, "wb") as f:
        f.write(image_to_bytes(resized_image))
    return image_path_to_s3_url(path)