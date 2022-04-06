from typing import Optional

from alloff_backoffice_server.settings import THUMBNAIL_SETTINGS
from functions.image.resize_and_cache_image import resize_and_cache


def check_and_make_thumbnail(data):
    """
    Check if provided thumbnail is actually a thumbnail,
    and makes a thumbnail if necessary.
    """
    if (url := _get_candidate_url(data)) is None:
        return data
    elif _is_thumbnail(url):
        return data
    else:
        return {**data, "thumbnail_image": _make_thumbnail(url)}


def _make_thumbnail(url: str) -> str:
    """
    Makes thumbnail from the given url
    and returns the url of the thumbnail.
    """
    return resize_and_cache(url, THUMBNAIL_SETTINGS["SIZE"], THUMBNAIL_SETTINGS["SUFFIX"])


def _is_thumbnail(url: str) -> bool:
    return THUMBNAIL_SETTINGS["SUFFIX"] in url

def _get_candidate_url(data) -> Optional[str]:
    if "thumbnail_image" in data:
        return data["thumbnail_image"]
    elif "images" in data and len(data["images"]) > 0:
        return data["images"][0]
    elif "description_images" in data and len(data["description_images"]) > 0:
        return data["description_images"][0]
    else:
        return None
