def add_image_info_to_map(map_of_image_hashes, image_info):
    image_hash = str(image_info.image_hash)
    image_name = image_info.image_name

    if image_hash not in map_of_image_hashes.keys():
        map_of_image_hashes[image_hash] = [image_name]
    else:
        map_of_image_hashes[image_hash].append(image_name)


def map_image_hash_to_list_of_image_names(image_infos):
    map_of_image_hashes = {}
    for image_info in image_infos:
        add_image_info_to_map(map_of_image_hashes, image_info)

    return map_of_image_hashes


# TODO rename
def filter_hashes_with_duplicate_images(dictionary):
    return dict(filter(
        lambda dict_items: len(dict_items[1]) > 1,
        dictionary.items()
    ))
