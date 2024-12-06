import logging
import unittest

from split_string_at_conjunctions import split_string_at_conjunctions

class TestSplitStringAtConjunctions(unittest.TestCase):
    def test_split_empty_str(self):
        string_to_split = ""
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("", split_string[0])

    def test_split_one_word_string_without_and(self):
        string_to_split = "BANANAS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("BANANAS", split_string[0])

    def test_split_multiword_string_without_and(self):
        string_to_split = "GRAND PIANOS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("GRAND PIANOS", split_string[0])

    def test_simple_split(self):
        string_to_split = "APPLES AND BANANAS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("APPLES", split_string[0])
        self.assertEqual("BANANAS", split_string[1])

    def test_split_with_single_trailing_descriptor(self):
        string_to_split = "APPLE AND BANANA HOLDERS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("APPLE HOLDERS", split_string[0])
        self.assertEqual("BANANA HOLDERS", split_string[1])

    def test_split_with_multiple_trailing_descriptors(self):
        string_to_split = "APPLES AND BANANAS IN CANADA"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("APPLES IN CANADA", split_string[0])
        self.assertEqual("BANANAS IN CANADA", split_string[1])

    def test_split_with_single_leading_descriptor(self):
        string_to_split = "3D POSITIONING AND NAVIGATION"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("3D POSITIONING", split_string[0])
        self.assertEqual("3D NAVIGATION", split_string[1])

    def test_split_with_multiple_leading_descriptors(self):
        string_to_split = "TREATMENT OF CANCERS AND DISEASES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TREATMENT OF CANCERS", split_string[0])
        self.assertEqual("TREATMENT OF DISEASES", split_string[1])

    def test_split_with_multiple_leading_and_trailing_descriptors(self):
        string_to_split = "TREATMENT OF DISEASES AND CANCERS IN CANADA"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TREATMENT OF DISEASES IN CANADA", split_string[0])
        self.assertEqual("TREATMENT OF CANCERS IN CANADA", split_string[1])

    def test_identifying_trailing_multi_word_subjects(self):
        string_to_split = "TREATMENT OF CANCERS AND SERIOUS DISEASES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TREATMENT OF CANCERS", split_string[0])
        self.assertEqual("TREATMENT OF SERIOUS DISEASES", split_string[1])

    def test_identifying_leading_multi_word_subjects(self):
        string_to_split = "TREATMENT OF SERIOUS DISEASES AND CANCERS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TREATMENT OF SERIOUS DISEASES", split_string[0])
        self.assertEqual("TREATMENT OF CANCERS", split_string[1])

    def test_complex_string_to_split(self):
        string_to_split = "TREATMENT OF SERIOUS DISEASES AND BONE CANCERS IN CANADA"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TREATMENT OF SERIOUS DISEASES IN CANADA", split_string[0])
        self.assertEqual("TREATMENT OF BONE CANCERS IN CANADA", split_string[1])

    def test_splitting_string_with_multiple_conjunctions(self):
        string_to_split = "TREATMENT AND PREVENTION OF CANCERS AND SERIOUS DISEASES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TREATMENT OF CANCERS", split_string[0])
        self.assertEqual("TREATMENT OF SERIOUS DISEASES", split_string[1])
        self.assertEqual("PREVENTION OF CANCERS", split_string[2])
        self.assertEqual("PREVENTION OF SERIOUS DISEASES", split_string[3])

    def test_splitting_around_leading_plurals(self):
        string_to_split = "APPLES AND BANANA HOLDERS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("APPLES", split_string[0])
        self.assertEqual("BANANA HOLDERS", split_string[1])

    def test_splitting_around_trailing_plurals(self):
        string_to_split = "BANANA HOLDERS AND APPLES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("BANANA HOLDERS", split_string[0])
        self.assertEqual("APPLES", split_string[1])

    def test_case_does_not_matter(self):
        string_to_split = "apples and bananas"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("apples", split_string[0])
        self.assertEqual("bananas", split_string[1])

    def test_split_with_quotes(self):        
        string_to_split = "WOMEN'S AND MEN'S APPAREL"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("WOMEN'S APPAREL", split_string[0])
        self.assertEqual("MEN'S APPAREL", split_string[1])


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()