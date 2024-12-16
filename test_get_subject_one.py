import logging
import unittest

from split_string_at_conjunctions import get_subject_one

class TestGetSubjectOne(unittest.TestCase):
    def test_split_empty_str_get_subject_one(self):
        string_to_split = ""
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("", subject_one)

    def test_split_one_word_string_without_and_get_subject_one(self):
        string_to_split = "BANANAS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("BANANAS", subject_one)

    def test_split_multiword_string_without_and_get_subject_one(self):
        string_to_split = "GRAND PIANOS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("GRAND PIANOS", subject_one)

    def test_simple_split_get_subject_one(self):
        string_to_split = "APPLES AND BANANAS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("APPLES", subject_one)

    def test_split_with_single_trailing_descriptor_get_subject_one(self):
        string_to_split = "APPLE AND BANANA HOLDERS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("APPLE", subject_one)

    def test_split_with_multiple_trailing_descriptors_get_subject_one(self):
        string_to_split = "APPLES AND BANANAS IN CANADA"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("APPLES", subject_one)

    def test_split_with_single_leading_descriptor_get_subject_one(self):
        string_to_split = "3D POSITIONING AND NAVIGATION"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("POSITIONING", subject_one)

    def test_split_with_multiple_leading_descriptors_get_subject_one(self):
        string_to_split = "TREATMENT OF CANCERS AND DISEASES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("CANCERS", subject_one)

    def test_split_with_multiple_leading_and_trailing_descriptors_get_subject_one(self):
        string_to_split = "TREATMENT OF DISEASES AND CANCERS IN CANADA"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("DISEASES", subject_one)

    def test_identifying_trailing_multi_word_subjects_get_subject_one(self):
        string_to_split = "TREATMENT OF CANCERS AND SERIOUS DISEASES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("CANCERS", subject_one)

    def test_identifying_leading_multi_word_subjects_get_subject_one(self):
        string_to_split = "TREATMENT OF SERIOUS DISEASES AND CANCERS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("SERIOUS DISEASES", subject_one)

    def test_complex_string_to_split_get_subject_one(self):
        string_to_split = "TREATMENT OF SERIOUS DISEASES AND BONE CANCERS IN CANADA"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("SERIOUS DISEASES", subject_one)

    def test_splitting_string_with_multiple_conjunctions_get_subject_one(self):
        string_to_split = "TREATMENT AND PREVENTION OF CANCERS AND SERIOUS DISEASES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("TREATMENT", subject_one)

    def test_splitting_around_leading_plurals_get_subject_one(self):
        string_to_split = "APPLES AND BANANA HOLDERS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("APPLES", subject_one)

    def test_splitting_around_trailing_plurals_get_subject_one(self):
        string_to_split = "BANANA HOLDERS AND APPLES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("BANANA HOLDERS", subject_one)

    def test_case_does_not_matter_get_subject_one(self):
        string_to_split = "apples and bananas"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("apples", subject_one)

    def test_split_with_quotes_get_subject_one(self):
        string_to_split = "WOMEN'S AND MEN'S APPAREL"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("WOMEN'S", subject_one)

    def test_hyphenated_string_get_subject_one(self):
        string_to_split = "CPAP AND BI-PAP EQUIPMENT"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("CPAP", subject_one)

    def test_duplicate_substring_on_both_sides_of_conjunction_get_subject_one(self):
        string_to_split = "BLACKBAUD MERCHANT SERVICES AND BLACKBAUD PURCHASE CARDS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("MERCHANT SERVICES", subject_one)

    def test_truck_and_rail_loading_unloading_facilities_get_subject_one(self):
        string_to_split = "TRUCK- AND RAIL-LOADING UNLOADING FACILITIES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("TRUCK-", subject_one)

    def test_sector_and_market_capitilization_weighted_index_production_get_subject_one(self):
        string_to_split = "SECTOR AND MARKET-CAPITALIZATION WEIGHTED INDEX PRODUCTION"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("SECTOR", subject_one)

    def test_sensor_and_sensor_based_product_development_get_subject_one(self):
        string_to_split = "SENSOR AND SENSOR-BASED PRODUCT DEVELOPMENT"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("SENSOR", subject_one)

    def test_single_and_multi_tenant_industrial_facilities_get_subject_one(self):
        string_to_split = "SINGLE- AND MULTI-TENANT INDUSTRIAL FACILITIES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("SINGLE-", subject_one)

    def test_small_and_medium_capitilization_companies_get_subject_one(self):
        string_to_split = "SMALL- AND MEDIUM-CAPITALIZATION COMPANIES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("SMALL-", subject_one)

    def test_2d_and_3d_inspection_capabilities_get_subject_one(self):
        string_to_split = "2D AND 3D INSPECTION CAPABILITIES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("2D", subject_one)

    def test_3d_printer_design_and_production_get_subject_one(self):
        string_to_split = "3D PRINTER DESIGN AND PRODUCTION"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("DESIGN", subject_one)

    def test_accessories_creation_and_distribution_get_subject_one(self):
        string_to_split = "ACCESSORIES CREATION AND DISTRIBUTION"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("CREATION", subject_one)

    def test_accomodation_reviews_and_ratings_get_subject_one(self):
        string_to_split = "ACCOMMODATION REVIEWS AND RATINGS"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("REVIEWS", subject_one)

    def test_defense_system_research_and_development_get_subject_one(self):
        string_to_split = "DEFENSE SYSTEM RESEARCH AND DEVELOPMENT"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("RESEARCH", subject_one)

    def test_head_and_neck_cancer_study_get_subject_one(self):
        string_to_split = "HEAD AND NECK CANCER STUDY"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("HEAD", subject_one)

    def test_index_tracking_and_reporting_get_subject_one(self):
        string_to_split = "INDEX TRACKING AND REPORTING"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("TRACKING", subject_one)

    def test_manufacturing_of_drone_parts_and_accessories_get_subject_one(self):
        string_to_split = "MANUFACTURING OF DRONE PARTS AND ACCESSORIES"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("DRONE PARTS", subject_one)

    def test_spinal_impant_and_fixation_system_manufacturing_get_subject_one(self):
        string_to_split = "SPINAL IMPLANT AND FIXATION SYSTEM MANUFACTURING"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("IMPLANT", subject_one)

    def test_tech_support_trust_and_safety_get_subject_one(self):
        string_to_split = "TECH SUPPORT TRUST AND SAFETY"
        subject_one = get_subject_one(string_to_split)
        self.assertEqual("TRUST", subject_one)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()