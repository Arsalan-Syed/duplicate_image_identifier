from src.image_utils import ImageHashComputer, ImageInfoDictionaryCreator
from src.file_utils import FileNameLoader, FileDeleter


def delete_duplicate_images(folder_path):
    images_to_delete = _find_images_to_delete(folder_path)
    FileDeleter.delete_files(images_to_delete)


def _find_images_to_delete(folder_path):
    image_names = FileNameLoader.load_file_names(folder_path)
    images_hashes = ImageHashComputer.compute_image_hashes(image_names)
    return ImageInfoDictionaryCreator.obtain_image_names_with_duplicate_hashes(image_names, images_hashes)
