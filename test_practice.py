import unittest
from unittest.mock import patch

from practice import main
from utils import add_numbers, ask_to_repeat, multiply_numbers, read_integer, select_operation


class AddNumbersTests(unittest.TestCase):
    def test_adds_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_adds_negative_number(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_adds_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_multiplies_integers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)

    @patch("builtins.input", side_effect=["invalid", "2"])
    @patch("builtins.print")
    def test_select_operation_retries_invalid_choice(self, mock_print, mock_input):
        self.assertEqual(select_operation(), "2")
        self.assertIn(
            unittest.mock.call("Nederīga izvēle. Izvēlies 1 vai 2."),
            mock_print.call_args_list,
        )

    @patch("builtins.input", side_effect=["maybe", " JĀ "])
    @patch("builtins.print")
    def test_ask_to_repeat_retries_invalid_answer(self, mock_print, mock_input):
        self.assertTrue(ask_to_repeat())
        mock_print.assert_called_once_with("Lūdzu, atbildi ar jā vai nē.")

    @patch("builtins.input", return_value="nē")
    def test_ask_to_repeat_returns_false_for_no(self, mock_input):
        self.assertFalse(ask_to_repeat())

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
