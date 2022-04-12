from alloff_backoffice_server.settings import DEFAULT_CACHING_SETTINGS
from core.image import BackofficeImageCacher


def check_and_download_images_to_s3(data):
    """
    Check if images are external (i.e., not hosted on S3) and download them to S3,
    and update the data with the new image URLs.
    """

    def __cacher(__url) -> BackofficeImageCacher:
        return BackofficeImageCacher(
            __url,
            caching_settings=DEFAULT_CACHING_SETTINGS,
            not_filters=[lambda __x: not _should_cache(__x)],
        )

    new_images = [__cacher(img).resized_url for img in data.get("images", [])]

    new_description_images = [
        __cacher(img).resized_url for img in data.get("description_images", [])
    ]

    return {**data, "images": new_images, "description_images": new_description_images}


def _should_cache(url: str) -> bool:
    ext = url.split(".")[-1].split("?")[0]
    if ext.lower() != "webp":
        # If format is not webp, always cache.
        return True

    if DEFAULT_CACHING_SETTINGS["SUFFIX"] in url:
        # If the URL already has the caching suffix, don't cache.
        return False

    # Can cache if image is not self-hosted.
    # return S3_IMAGES_HOST not in url or CLOUDFRONT_HOST not in url

    return True
