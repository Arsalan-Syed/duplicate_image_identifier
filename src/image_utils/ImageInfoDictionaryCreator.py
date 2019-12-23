from src.helpers import ListUtils


def obtain_image_names_with_duplicate_hashes(images_names, image_hashes):
    dictionary = _create_mapping_from_image_hash_to_list_of_image_names(images_names, image_hashes)
    filtered_dictionary = _filter_hashes_with_duplicate_images(dictionary)
    image_hashes_with_duplicate_files = filtered_dictionary.keys()
    files_to_delete = [filtered_dictionary[image_hash][1:] for image_hash in image_hashes_with_duplicate_files]
    return ListUtils.flatten(files_to_delete)


def _create_mapping_from_image_hash_to_list_of_image_names(images_names, image_hashes):
    dictionary = _init_dict(image_hashes)

    for i in range(len(images_names)):
        image_hash = image_hashes[i]
        image_name = images_names[i]

        dictionary[image_hash].append(image_name)

    return dictionary


def _init_dict(image_hashes):
    dictionary = {}
    for image_hash in image_hashes:
        dictionary[image_hash] = []
    return dictionary


def _filter_hashes_with_duplicate_images(dictionary):
    return dict(filter(
        lambda dict_items: len(dict_items[1]) > 1,
        dictionary.items()
    ))
