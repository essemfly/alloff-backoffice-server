import shortuuid
from alloff_backoffice_server.settings import S3_IMAGES_HOST


def processed_image_path(
    resize_info: str,
    suffix: str = "__RESIZED",
    s3_folder: str = "images",
    ext=None,
) -> str:
    if ext is None:
        raise ValueError("ext must be explicitly specified.")

    filename = f"{shortuuid.random(16)}{suffix}-{resize_info}.{ext}"
    s3_path = f"{s3_folder}/{filename}"
    return s3_path


def image_path_to_s3_url(image_path: str) -> str:
    return f"{S3_IMAGES_HOST}/{image_path}"
