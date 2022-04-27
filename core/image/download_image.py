from io import BytesIO

import requests
from PIL import Image, ImageOps


class CannotDownloadImageException(Exception):
    pass


def download_image(url: str, exif_transpose: bool = True) -> Image.Image:
    """
    Downloads image from url and returns the in-memory image.
    Raises CannotDownloadImageException on non-200 response.
    """
    res = requests.get(url)
    if res.status_code != 200:
        raise CannotDownloadImageException(f"Cannot download image from {url}")

    image = Image.open(BytesIO(res.content))
    if exif_transpose:
        image = ImageOps.exif_transpose(image)
    return image
