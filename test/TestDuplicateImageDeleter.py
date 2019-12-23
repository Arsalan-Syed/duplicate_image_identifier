import unittest
from mockito import when, ANY
from src import DuplicateImageDeleter
from src.file_utils import FileNameLoader
from src.image_utils import ImageHashComputer


class TestDuplicateImageDeleter(unittest.TestCase):

    def test_should_mark_file3_for_deletion_which_is_duplicate_of_file1(self):
        image_file_names = ["file1", "file2", "file3"]
        image_hashes = ["hash1", "hash2", "hash1"]

        when(FileNameLoader).load_file_names(ANY) \
            .thenReturn(image_file_names)

        when(ImageHashComputer).compute_image_hashes(image_file_names) \
            .thenReturn(image_hashes)

        files_to_delete = DuplicateImageDeleter._find_images_to_delete("folder_name")

        self.assertTrue("file3" in files_to_delete)


if __name__ == '__main__':
    unittest.main()
