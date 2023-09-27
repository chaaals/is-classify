import unittest

class ClassifyUnitTest(unittest.TestCase):
    def test_unitTest(self):
        self.assertEqual('hello world'.upper(), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()