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

    def test_hyphenated_string(self):
        string_to_split = "CPAP AND BI-PAP EQUIPMENT"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("CPAP EQUIPMENT", split_string[0])
        self.assertEqual("BI-PAP EQUIPMENT", split_string[1])

    def test_duplicate_substring_on_both_sides_of_conjunction(self):
        string_to_split = "BLACKBAUD MERCHANT SERVICES AND BLACKBAUD PURCHASE CARDS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("BLACKBAUD MERCHANT SERVICES", split_string[0])
        self.assertEqual("BLACKBAUD PURCHASE CARDS", split_string[1])

    def test_truck_and_rail_loading_unloading_facilities(self):
        string_to_split = "TRUCK- AND RAIL-LOADING UNLOADING FACILITIES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TRUCK-LOADING UNLOADING FACILITIES", split_string[0])
        self.assertEqual("RAIL-LOADING UNLOADING FACILITIES", split_string[1])

    def test_sector_and_market_capitilization_weighted_index_production(self):
        string_to_split = "SECTOR AND MARKET-CAPITALIZATION WEIGHTED INDEX PRODUCTION"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("SECTOR WEIGHTED INDEX PRODUCTION", split_string[0])
        self.assertEqual("MARKET-CAPITALIZATION WEIGHTED INDEX PRODUCTION", split_string[1])

    def test_sensor_and_sensor_based_product_development(self):
        string_to_split = "SENSOR AND SENSOR-BASED PRODUCT DEVELOPMENT"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("SENSOR PRODUCT DEVELOPMENT", split_string[0])
        self.assertEqual("SENSOR-BASED PRODUCT DEVELOPMENT", split_string[1])

    def test_single_and_multi_tenant_industrial_facilities(self):
        string_to_split = "SINGLE- AND MULTI-TENANT INDUSTRIAL FACILITIES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("SINGLE-TENANT INDUSTRIAL FACILITIES", split_string[0])
        self.assertEqual("MULTI-TENANT INDUSTRIAL FACILITIES", split_string[1])

    def test_small_and_medium_capitilization_companies(self):
        string_to_split = "SMALL- AND MEDIUM-CAPITALIZATION COMPANIES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("SMALL-CAPITALIZATION COMPANIES", split_string[0])
        self.assertEqual("MEDIUM-CAPITALIZATION COMPANIES", split_string[1])

    def test_2d_and_3d_inspection_capabilities(self):
        string_to_split = "2D AND 3D INSPECTION CAPABILITIES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("2D INSPECTION CAPABILITIES", split_string[0])
        self.assertEqual("3D INSPECTION CAPABILITIES", split_string[1])

    def test_3d_printer_design_and_production(self):
        string_to_split = "3D PRINTER DESIGN AND PRODUCTION"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("3D PRINTER DESIGN", split_string[0])
        self.assertEqual("3D PRINTER PRODUCTION", split_string[1])

    def test_accessories_creation_and_distribution(self):
        string_to_split = "ACCESSORIES CREATION AND DISTRIBUTION"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("ACCESSORIES CREATION", split_string[0])
        self.assertEqual("ACCESSORIES DISTRIBUTION", split_string[1])

    def test_accomodation_reviews_and_ratings(self):
        string_to_split = "ACCOMMODATION REVIEWS AND RATINGS"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("ACCOMMODATION REVIEWS", split_string[0])
        self.assertEqual("ACCOMMODATION RATINGS", split_string[1])

    def test_defense_system_research_and_development(self):
        string_to_split = "DEFENSE SYSTEM RESEARCH AND DEVELOPMENT"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("DEFENSE SYSTEM RESEARCH", split_string[0])
        self.assertEqual("DEFENSE SYSTEM DEVELOPMENT", split_string[1])

    def test_head_and_neck_cancer_study(self):
        string_to_split = "HEAD AND NECK CANCER STUDY"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("HEAD CANCER STUDY", split_string[0])
        self.assertEqual("NECK CANCER STUDY", split_string[1])

    def test_index_tracking_and_reporting(self):
        string_to_split = "INDEX TRACKING AND REPORTING"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("INDEX TRACKING", split_string[0])
        self.assertEqual("INDEX REPORTING", split_string[1])

    def test_manufacturing_of_drone_parts_and_accessories(self):
        string_to_split = "MANUFACTURING OF DRONE PARTS AND ACCESSORIES"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("MANUFACTURING OF DRONE PARTS", split_string[0])
        self.assertEqual("MANUFACTURING OF DRONE ACCESSORIES", split_string[1])

    def test_spinal_impant_and_fixation_system_manufacturing(self):
        string_to_split = "SPINAL IMPLANT AND FIXATION SYSTEM MANUFACTURING"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("SPINAL IMPLANT MANUFACTURING", split_string[0])
        self.assertEqual("SPINAL FIXATION SYSTEM MANUFACTURING", split_string[1])

    def test_tech_support_trust_and_safety(self):
        string_to_split = "TECH SUPPORT TRUST AND SAFETY"
        split_string = split_string_at_conjunctions(string_to_split)
        self.assertEqual("TECH SUPPORT TRUST", split_string[0])
        self.assertEqual("TECH SUPPORT SAFETY", split_string[1])


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()