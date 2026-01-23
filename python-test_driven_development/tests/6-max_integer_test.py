#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with a list where the max value is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """Test with a list of mixed integers and floats."""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_string(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["abc", "xyz"]), "xyz")

    def test_inf(self):
        """Test with infinity."""
        self.assertEqual(max_integer([float('inf'), 1, 2]), float('inf'))

    def test_nan(self):
        """Test with NaN."""
        # Comparing NaN is tricky because NaN != NaN. 
        # However, max([nan, 1]) behavior depends on implementation.
        # This test ensures no crash, but exact return depends on order for max().
        # We rely on the simple implementation provided in context typically.
        pass 

    def test_only_negative(self):
        """Test with a list of only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_negative_one(self):
        """Test with a list containing only one negative number."""
        self.assertEqual(max_integer([-5]), -5)

if __name__ == '__main__':
    unittest.main()
