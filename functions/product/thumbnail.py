from typing import Optional

from alloff_backoffice_server.settings import THUMBNAIL_SETTINGS
from core.image import BackofficeImageCacher


def check_and_make_thumbnail(data):
    """
    Check if provided thumbnail is actually a thumbnail,
    and makes a thumbnail if necessary.
    """
    if (url := _get_candidate_url(data)) is None:
        return data
    else:
        cacher = BackofficeImageCacher(
            url,
            caching_settings=THUMBNAIL_SETTINGS,
            not_filters=[_is_thumbnail],
        )

        return {**data, "thumbnail_image": cacher.resized_url}


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
