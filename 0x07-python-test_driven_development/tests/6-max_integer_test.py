#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__("6-max_integer").max_integer

class TestStringMethods(unittest.TestCase):
    def test_max_integer_values(self):
        self.assertIsInstance(max_integer([1, 2, 3, -9, 5]), int)
        self.assertIs(max_integer([]), None)

    def test_max_integer_equal(self):
        self.assertEqual(max_integer([1, 2, 3, 9, 5]), 9)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, -9, 5]), 5)
    
    def test_max_integer_error(self):
        self.assertRaises(TypeError, max_integer(["hello"]))

if __name__ == '__main__':
    unittest.main()
