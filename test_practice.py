import unittest
from unittest.mock import patch

from utils import add_numbers, multiply_numbers, read_integer


class AddNumbersTests(unittest.TestCase):
    def test_adds_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_adds_negative_number(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_adds_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_multiplies_integers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)

    @patch("builtins.input", side_effect=["abc", "4"])
    @patch("builtins.print")
    def test_read_integer_retries_invalid_input(self, mock_print, mock_input):
        self.assertEqual(read_integer("Skaitlis: "), 4)
        mock_print.assert_called_once_with("Lūdzu, ievadi veselu skaitli.")
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()
