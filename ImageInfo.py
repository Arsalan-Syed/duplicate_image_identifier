import imagehash
from PIL import Image


class ImageInfo:
    def __init__(self, image_name):
        self.image_name = image_name
        self.image_hash = imagehash.dhash(Image.open(image_name))
