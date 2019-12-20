import unittest
from mockito import when, ANY
from src import ImageInfoComputer, DuplicateImageDeleter, FileNameLoader
from src.ImageInfo import ImageInfo


def init_image_infos():
    image_info1 = ImageInfo("file1", "hash1")
    image_info2 = ImageInfo("file2", "hash2")
    image_info3 = ImageInfo("file3", "hash1")
    return [image_info1, image_info2, image_info3]


class TestDuplicateImageDeleter(unittest.TestCase):

    def test_should_mark_file3_for_deletion_which_is_duplicate_of_file1(self):
        image_file_names = ["file1", "file2", "file3"]
        image_infos = init_image_infos()

        when(FileNameLoader).load_file_names(ANY) \
            .thenReturn(image_file_names)

        when(ImageInfoComputer).create_image_infos_from_names(image_file_names) \
            .thenReturn(image_infos)

        files_to_delete = DuplicateImageDeleter.find_files_to_delete("folder_name")

        self.assertTrue("file3" in files_to_delete)


if __name__ == '__main__':
    unittest.main()
