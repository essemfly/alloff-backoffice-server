from PIL import Image

def resize_image_by_max_width(image: Image, max_width: int):
    wpercent = max_width / float(image.size[0])
    hsize = int((float(image.size[1]) * float(wpercent)))
    return image.resize((max_width, hsize), Image.LANCZOS)