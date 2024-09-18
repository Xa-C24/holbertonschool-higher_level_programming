#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_regular_list(self):
        """Test with a regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -2, -8, -3]), -2)

    def test_mixed_numbers(self):
        """Test with a list containing a mix of positive and negative numbers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_max_at_beginning(self):
        """Test with a list where the maximum value is at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)

    def test_max_in_middle(self):
        """Test with a list where the maximum value is in the middle"""
        self.assertEqual(max_integer([1, 5, 2, 3, 4]), 5)

    def test_max_at_end(self):
        """Test with a list where the maximum value is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_list_of_strings(self):
        """Test with a list of strings (to check for type errors)"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

if __name__ == "__main__":
    unittest.main()
    