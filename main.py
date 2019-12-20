import HashMapCreator
import ImageDeleter
import FileNameLoader
from ImageInfo import ImageInfo

folder_path = "photos_for_project/*"


def delete_duplicate_images(folder_path):
    image_names = FileNameLoader.load_file_names(folder_path)
    image_infos = compute_image_infos(image_names)
    map_of_image_hashes = HashMapCreator.map_image_hash_to_list_of_image_names(image_infos)
    filtered_map = HashMapCreator.filter_hashes_with_duplicate_images(map_of_image_hashes)

    for key in filtered_map.keys():
        image_name_list = map_of_image_hashes[key]
        ImageDeleter.delete_duplicate_images(image_name_list[1:])


def compute_image_infos(image_names):
    return [ImageInfo(image_name) for image_name in image_names]
