import unittest
from random import randint
from faker import Faker

from constants.user_info import UserInfo
from constants.date_formats import DATE_FORMATS

f = Faker()

class DateFormatUnitTest(unittest.TestCase):
    def test_date_validation(self):
        index = randint(0, len(DATE_FORMATS) - 1)
        rand_date = f.date_time().strftime(DATE_FORMATS[index])
        self.assertEqual(UserInfo.is_valid_birthday(rand_date), True)

    def test_date_validation_err(self):
        self.assertEqual(UserInfo.is_valid_birthday('Maw 12, 2023'), None)
        

        