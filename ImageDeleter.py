import os


def delete_duplicate_images(duplicate_image_list):
    for image_name in duplicate_image_list:
        os.remove(image_name)
