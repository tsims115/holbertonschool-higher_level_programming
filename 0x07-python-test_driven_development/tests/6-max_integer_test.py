#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestStringMethods(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 9, 5]), 9)

    def test_max_integer1(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer2(self):
        self.assertEqual(max_integer([1, 2, 3, -9, 5]), 5)

if __name__ == '__main__':
    unittest.main()
