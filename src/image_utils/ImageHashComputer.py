import imagehash
from PIL import Image


def compute_image_hashes(image_names):
    return [imagehash.dhash(Image.open(image_name)) for image_name in image_names]
