import requests
import shortuuid
from alloff_backoffice_server.settings import S3_IMAGES_HOST
from django.core.files.storage import default_storage


def download_image_to_s3(image_url: str) -> str:
    """
    Download image from url and save it to S3.
    Returns the original image url if image is not properly downloaded.
    """
    try:
        res = requests.get(image_url, timeout=3)
        if res.status_code != 200:
            return image_url

        random_key = shortuuid.random(length=24)
        original_filename_nodes = image_url.split("/")[-1].split(".")
        ext = original_filename_nodes[-1].split("?")[0]
        filename = f"{random_key}.{ext}"
        s3_path = f"html_product_images/{filename}"

        with default_storage.open(s3_path, "wb") as f:
            f.write(res.content)

        return f"{S3_IMAGES_HOST}/{s3_path}"
    except:
        return image_url
