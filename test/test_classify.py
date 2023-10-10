import unittest
import platform
from pathlib import Path
from algorithm.classify import Classify

# generates a path for test data directory
TEST_DATA_DIR = Path(__file__).parent.joinpath("test_data")
SYSTEM = platform.system()
classify = Classify(TEST_DATA_DIR)

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
                "63-9282873428",
                "Antonio Castillo",
                "Robert Mcintyre",
                "63-9282873428",
                "2019-02-05",
                "carlmcintyre@example.org",
                "Michael Graham",
                "Amber Thomas",
                "ushelton@example.org",
                "1993-08-20",
                "2019-02-05",
                "Brooke Huang",
                "639781474972",
                "David Wallace",
                "09143480987",
                "mathewsjessica@example.net"
            },
            {
                "+63-9092271704",
                "derek17@example.com",
                "dustinwilcox@example.org",
                "23 June, 1988",
                "Maria Tran Marquez",
                "63-9385943899",
                "aimeelogan@example.org",
                "639246610416",
                "09624060793",
                "Stacy Morton Hurley",
                "+63-9084021344",
                "Denise Moss Allen",
                "11/15/1985",
                "paultaylor@example.net",
                "hernandezdylan@example.net",
                "09/30/1985",
                "mlucas@example.org",
                "Timothy Reese Gomez",
                "jessicabarnes@example.org",
                "12-05-1976",
                "13-06-1992",
                "amy88@example.org",
                "Kyle Carter Olson",
                "+63-9106021498",
                "brenda68@example.net"
            }
        ])

    # should successfully create a list of sets containing clean raw data from txt files on macOS
    @unittest.skipIf(SYSTEM == "Windows", "OS != Darwin(macOS)")
    def test_read_data_macos(self):
        self.assertListEqual(
            classify.get_raw_data(),
        [
            {
                "+63-9092271704",
                "derek17@example.com",
                "dustinwilcox@example.org",
                "23 June, 1988",
                "Maria Tran Marquez",
                "63-9385943899",
                "aimeelogan@example.org",
                "639246610416",
                "09624060793",
                "Stacy Morton Hurley",
                "+63-9084021344",
                "Denise Moss Allen",
                "11/15/1985",
                "paultaylor@example.net",
                "hernandezdylan@example.net",
                "09/30/1985",
                "mlucas@example.org",
                "Timothy Reese Gomez",
                "jessicabarnes@example.org",
                "12-05-1976",
                "13-06-1992",
                "amy88@example.org",
                "Kyle Carter Olson",
                "+63-9106021498",
                "brenda68@example.net"
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
                "63-9282873428",
                "Antonio Castillo",
                "Robert Mcintyre",
                "63-9282873428",
                "2019-02-05",
                "carlmcintyre@example.org",
                "Michael Graham",
                "Amber Thomas",
                "ushelton@example.org",
                "1993-08-20",
                "2019-02-05",
                "Brooke Huang",
                "639781474972",
                "David Wallace",
                "09143480987",
                "mathewsjessica@example.net"
            }
        ])


    # should count the redundant data in txt file
    def test_redundant_data(self):
        self.assertDictEqual(classify.get_redundant_data(), {
            "63-9282873428": 1,
            "2019-02-05": 1,
        })

    # should raise a ValueError when passing an invalid directory
    def test_dir_error(self):
        with self.assertRaises(ValueError):
            Classify(TEST_DATA_DIR.joinpath('/data_set_471.txt'))

    # should print out the categorized data
    def test_print_categorized_data(self):
        classify.categorize_data()
        print("Categorized Data:")
        classify.print_categorized_data()
    
if __name__ == '__main__':
    unittest.main()