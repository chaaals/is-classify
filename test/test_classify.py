import unittest
import os
from algorithm.classify import Classify


class ClassifyUnitTest(unittest.TestCase):
    def test_read_data(self):
        # generates a path for test data directory
        TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

        classify = Classify(TEST_DATA_DIR)
        
        self.assertListEqual(
            classify.get_raw_data(),
        [
            [
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
                "Emily Lawson",
                "Julia Craig",
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
            ],
            [
                "2009-03-28",
                "1991-07-08",
                "rjohnson@example.com",
                "Maria Thornton",
                "1997-07-12",
                "+63-9491079775",
                "2012-01-18",
                "Kara Lee MD",
                "1975-04-23",
                "+63-9969256771",
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
            ]
        ])

if __name__ == '__main__':
    unittest.main()