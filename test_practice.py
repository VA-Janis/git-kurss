import unittest

from practice import add_numbers


class AddNumbersTests(unittest.TestCase):
    def test_adds_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_adds_negative_number(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_adds_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
