import unittest
import platform
import re
from pathlib import Path
from algorithm.classify import Classify

# generates a path for test data directory
TEST_DATA_DIR = Path(__file__).parent.joinpath("test_data")
SYSTEM = platform.system()

classify = Classify(TEST_DATA_DIR)

# categorize raw data
classify.categorize_data()

class ClassifyUnitTest(unittest.TestCase):
    # should successfully create a list of sets containing clean raw data from txt files on Windows OS
    @unittest.skipIf(SYSTEM == "Darwin", "OS != Windows")
    def test_read_data_windows(self):
        self.assertListEqual(
            classify.get_raw_data(),
        [
            {
                "2016-03-22",
                "blakebennett@example.org",
                "2001-11-25",
                "Paige Obrien",
                "+63-9529763557",
                "robertsmichelle@example.net",
                "michael09@example.org",
                "2007-09-08",
                "Kendra Taylor",
                "+63-9282873428",
                "Antonio Castillo",
                "Robert Mcintyre",
                "+63-9282873428",
                "2019-02-05",
                "carlmcintyre@example.org",
                "Michael Graham",
                "Amber Thomas",
                "ushelton@example.org",
                "1993-08-20",
                "2019-02-05",
                "Brooke Huang",
                "+63-9781474972",
                "David Wallace",
                "+63-9143480987",
                "mathewsjessica@example.net"
            },
            {
                "2009-03-28",
                "1991-07-08",
                "rjohnson@example.com",
                "Maria Thornton",
                "1997-07-12",
                "Destiny Stewart",
                "2012-01-18",
                "Kara Lee MD",
                "1975-04-23",
                "Stephanie Estrada",
                "Brandi Beasley",
                "1985-12-04",
                "brenda03@example.org",
                "Antonio Davila",
                "april93@example.org",
                "Stephanie Estrada",
                "jmendoza@example.com",
                "schmidtjillian@example.net",
                "jenniferfreeman@example.com",
                "estewart@example.com",
                "+63-9637653230",
                "+63-9869682919",
                "+63-9182232234",
                "+63-9906300018",
                "Destiny Stewart"
            }
        ])

    # should successfully create a list of sets containing clean raw data from txt files on macOS
    @unittest.skipIf(SYSTEM == "Windows", "OS != Darwin(macOS)")
    def test_read_data_macos(self):
        self.assertListEqual(
            classify.get_raw_data(),
        [
            {
                "2009-03-28",
                "1991-07-08",
                "rjohnson@example.com",
                "Maria Thornton",
                "1997-07-12",
                "Destiny Stewart",
                "2012-01-18",
                "Kara Lee MD",
                "1975-04-23",
                "Stephanie Estrada",
                "Brandi Beasley",
                "1985-12-04",
                "brenda03@example.org",
                "Antonio Davila",
                "april93@example.org",
                "Stephanie Estrada",
                "jmendoza@example.com",
                "schmidtjillian@example.net",
                "jenniferfreeman@example.com",
                "estewart@example.com",
                "+63-9637653230",
                "+63-9869682919",
                "+63-9182232234",
                "+63-9906300018",
                "Destiny Stewart"
            },
            {
                "2016-03-22",
                "blakebennett@example.org",
                "2001-11-25",
                "Paige Obrien",
                "+63-9529763557",
                "robertsmichelle@example.net",
                "michael09@example.org",
                "2007-09-08",
                "Kendra Taylor",
                "+63-9282873428",
                "Antonio Castillo",
                "Robert Mcintyre",
                "+63-9282873428",
                "2019-02-05",
                "carlmcintyre@example.org",
                "Michael Graham",
                "Amber Thomas",
                "ushelton@example.org",
                "1993-08-20",
                "2019-02-05",
                "Brooke Huang",
                "+63-9781474972",
                "David Wallace",
                "+63-9143480987",
                "mathewsjessica@example.net"
            }
        ])


    # should count the redundant data in txt file
    def test_redundant_data(self):
        self.assertDictEqual(classify.get_redundant_data(), {
            "+63-9282873428": 1,
            "2019-02-05": 1,
            "Stephanie Estrada": 1,
            "Destiny Stewart": 1
        })

    # should raise a ValueError when passing an invalid directory
    def test_dir_error(self):
        with self.assertRaises(ValueError):
            Classify(TEST_DATA_DIR.joinpath('/data_set_471.txt'))

    # should print out the categorized data
    # def test_print_categorized_data(self):
    #     print("Categorized Data:")
    #     classify.print_categorized_data()

    # should categorize data based on name, birthday, email, and cell_no
    def test_categorize_data(self):
        categorized_data = classify.get_categorized_data()

        for data_set in categorized_data.values():
            self.assertGreater(len(data_set), 0, 'Set is greater than zero')

    # should categorize raw data by user input category and regex
    def test_categorize_data_by(self):
        classify_by = Classify(TEST_DATA_DIR)
        classify_by.categorize_data_by({
            "name2": r'^[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*){1,2}$',
            "cell_no2": r'^\+63-\d{10}$',
            "birthday2": r'^\d{4}-\d{2}-\d{2}$',
            "email2": r'^.+@.+\..{2,}$',
            "test": None,
            "test2": 123
        })

        categorized_data = classify_by.get_categorized_data()
        classify_by.print_categorized_data()
        for data_set in categorized_data.values():
            self.assertGreater(len(data_set), 0, 'Set is greater than zero')

    # should have an empty set for invalid regex or no matching regex
    def test_categorize_data_by_error(self):
        classify_by = Classify(TEST_DATA_DIR)
        classify_by.categorize_data_by({
            "name2": r'^[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*){1,2}$',
            "cell_no2": r'^\+63-\d{10}$',
            "birthday2": r'^\d{4}-\d{2}-\d{2}$',
            "email2": r'^.+@.+\..{2,}$',
            "test3": 'asdgasdgs'
        })

        categorized_data = classify_by.get_categorized_data()
        self.assertEqual(len(categorized_data['test3']), 0)
    
if __name__ == '__main__':
    unittest.main()