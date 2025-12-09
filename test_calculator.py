import unittest
from calculator import calculate_average


class TestCalculateAverage(unittest.TestCase):
    def test_average_of_three_numbers(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_average_of_single_number(self):
        self.assertEqual(calculate_average([50]), 50)

    def test_average_with_decimals(self):
        result = calculate_average([1, 2, 3, 4])
        self.assertEqual(result, 2.5)

    def test_average_of_negative_numbers(self):
        self.assertEqual(calculate_average([-10, 10]), 0)

    def test_empty_list_raises_error(self):
        with self.assertRaises(ValueError) as context:
            calculate_average([])
        self.assertIn("Cannot calculate average of empty list", str(context.exception))


if __name__ == "__main__":
    unittest.main()
