import imagehash
from PIL import Image


class ImageInfo:

    def __init__(self, image_name, image_hash=""):
        self.image_name = image_name

        if image_hash == "":
            self.image_hash = imagehash.dhash(Image.open(image_name))
        else:
            self.image_hash = image_hash
