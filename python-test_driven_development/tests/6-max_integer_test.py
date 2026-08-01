#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for the max_integer function."""

    def test_ordered_list(self):
        """Test a list of ascending integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test a list of descending integers."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Test calling with no arguments returns None."""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test a list of mixed positive and negative integers."""
        self.assertEqual(max_integer([-5, 3, 0, -2, 9]), 9)

    def test_all_same(self):
        """Test a list where all elements are equal."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
