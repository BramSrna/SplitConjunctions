import logging
import unittest

from split_string_at_conjunctions import validate_string_part_selection

class TestValidateStringPartSelection(unittest.TestCase):
    def test_happy_path_case(self):
        string_to_split = "3D printer design and production"
        leading_descriptors = "3D printer"
        subject_1 = "design"
        subject_2 = "production"
        trailing_descriptors = ""
        self.assertTrue(validate_string_part_selection(string_to_split, leading_descriptors, subject_1, subject_2, trailing_descriptors))

    def test_subjects_can_be_out_of_order(self):
        string_to_split = "3D printer design and production"
        leading_descriptors = "3D printer"
        subject_1 = "production"
        subject_2 = "design"
        trailing_descriptors = ""
        self.assertTrue(validate_string_part_selection(string_to_split, leading_descriptors, subject_1, subject_2, trailing_descriptors))

    def test_incorrect_subject_1(self):
        string_to_split = "3D printer design and production"
        leading_descriptors = "3D"
        subject_1 = "printer design"
        subject_2 = "production"
        trailing_descriptors = ""
        self.assertFalse(validate_string_part_selection(string_to_split, leading_descriptors, subject_1, subject_2, trailing_descriptors))

    def test_incorrect_subject_1_extended(self):
        string_to_split = "3D printer design and production"
        leading_descriptors = ""
        subject_1 = "3D printer design"
        subject_2 = "production"
        trailing_descriptors = ""
        self.assertFalse(validate_string_part_selection(string_to_split, leading_descriptors, subject_1, subject_2, trailing_descriptors))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()