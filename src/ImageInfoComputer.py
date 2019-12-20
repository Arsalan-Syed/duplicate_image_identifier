from src.ImageInfo import ImageInfo


def create_image_infos_from_names(image_names):
    return [ImageInfo(image_name) for image_name in image_names]
