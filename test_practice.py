import unittest
from unittest.mock import patch

from practice import main
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

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "2", "3", "nē"])
    def test_main_selects_addition(self, mock_input, mock_print):
        main()
        mock_print.assert_called_with("Rezultāts: 5")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["2", "2", "3", "nē"])
    def test_main_selects_multiplication(self, mock_input, mock_print):
        main()
        mock_print.assert_called_with("Rezultāts: 6")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "2", "3", "jā", "2", "4", "5", "nē"])
    def test_main_repeats_calculation(self, mock_input, mock_print):
        main()
        self.assertIn(unittest.mock.call("Rezultāts: 5"), mock_print.call_args_list)
        self.assertIn(unittest.mock.call("Rezultāts: 20"), mock_print.call_args_list)

    @patch("builtins.input", side_effect=["abc", "4"])
    @patch("builtins.print")
    def test_read_integer_retries_invalid_input(self, mock_print, mock_input):
        self.assertEqual(read_integer("Skaitlis: "), 4)
        mock_print.assert_called_once_with("Lūdzu, ievadi veselu skaitli.")
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()
