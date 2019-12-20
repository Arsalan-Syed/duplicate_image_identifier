from src import FileNameLoader, ImageInfoDictionaryCreator, FileDeleter
from src.ImageInfo import ImageInfo

folder_path = "photos_for_project/*"


def delete_duplicate_images(folder_path):
    image_names = FileNameLoader.load_file_names(folder_path)
    image_infos = compute_image_infos(image_names)

    image_hash_to_image_name_list = ImageInfoDictionaryCreator.map_image_hash_to_list_of_image_names(image_infos)
    filtered_hashes = ImageInfoDictionaryCreator.filter_hashes_with_duplicate_images(image_hash_to_image_name_list)

    for key in filtered_hashes.keys():
        image_name_list = image_hash_to_image_name_list[key]
        FileDeleter.delete_files(image_name_list[1:])


def compute_image_infos(image_names):
    return [ImageInfo(image_name) for image_name in image_names]
