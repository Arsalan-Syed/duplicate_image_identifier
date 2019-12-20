from src import FileNameLoader, ImageInfoDictionaryCreator, FileDeleter, ImageInfoComputer


def find_files_to_delete(folder_path):
    image_names = FileNameLoader.load_file_names(folder_path)
    image_infos = ImageInfoComputer.create_image_infos_from_names(image_names)

    image_hash_to_image_name_list = ImageInfoDictionaryCreator.map_image_hash_to_list_of_image_names(image_infos)
    filtered_hashes = ImageInfoDictionaryCreator.filter_hashes_with_duplicate_images(image_hash_to_image_name_list)

    files_to_delete = []
    for key in filtered_hashes.keys():
        image_name_list = image_hash_to_image_name_list[key]
        files_to_delete = files_to_delete + image_name_list[1:]

    return files_to_delete


def delete_duplicate_images(folder_path):
    files_to_delete = find_files_to_delete(folder_path)
    for file in files_to_delete:
        FileDeleter.delete_files(file)
