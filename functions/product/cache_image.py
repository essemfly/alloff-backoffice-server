

from alloff_backoffice_server.settings import (DO_NOT_CACHE_IMAGES_TO_S3_HOSTS,
                                               IMAGE_CACHING_SETTINGS)
from functions.image.resize_and_cache_image import resize_and_cache


def check_and_download_images_to_s3(data):
    """
    Check if images are external (i.e., not hosted on S3) and download them to S3,
    and update the data with the new image URLs.
    """
    new_images = [
        _resize_and_cache(img) if _should_cache(img) else img
        for img in data.get("images", [])
        ]

    new_description_images = [
        _resize_and_cache(img)  if _should_cache(img) else img
        for img in data.get("description_images", [])
        ]
    
    return {**data, "images": new_images, "description_images": new_description_images}

def _resize_and_cache(url: str) -> str:
    """
    Resizes and chaches the image to S3,
    and returns the new URL.
    """
    return resize_and_cache(url, IMAGE_CACHING_SETTINGS["SIZE"], IMAGE_CACHING_SETTINGS["SUFFIX"])

def _should_cache(url: str) -> bool:
    for host in DO_NOT_CACHE_IMAGES_TO_S3_HOSTS:
        if host in url:
            # If host is a no-go, return False.
            return False

    ext = url.split(".")[-1].split("?")[0]
    if ext.lower() != "webp":
        # If format is not webp, always cache.
        return True

    if IMAGE_CACHING_SETTINGS["SUFFIX"] in url:
        # If the URL already has the caching suffix, don't cache.
        return False
        
    # Can cache if image is not self-hosted.
    # return S3_IMAGES_HOST not in url or CLOUDFRONT_HOST not in url

    return True
