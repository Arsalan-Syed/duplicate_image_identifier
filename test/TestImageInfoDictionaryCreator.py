import unittest
from src import ImageInfoDictionaryCreator


class TestImageInfoDictionaryCreator(unittest.TestCase):

    def test_correctly_filter_values_where_list_length_greater_than_one(self):
        dictionary = {
            "valuesTooShort": [],
            "valuesTooShort2": ["element1"],
            "valuesWillBeFiltered": ["element1", "element2", "element3"]
        }
        filtered_dictionary = ImageInfoDictionaryCreator.filter_hashes_with_duplicate_images(dictionary)
        self.assertTrue("valuesWillBeFiltered" in filtered_dictionary)


if __name__ == '__main__':
    unittest.main()
