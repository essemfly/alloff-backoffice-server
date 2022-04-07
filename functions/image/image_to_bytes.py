from io import BytesIO
from PIL import Image

def image_to_bytes(image: Image, format: str = "WEBP") -> bytes:
    image_bytes = BytesIO()
    image.save(fp=image_bytes, format=format)
    return image_bytes.getvalue()