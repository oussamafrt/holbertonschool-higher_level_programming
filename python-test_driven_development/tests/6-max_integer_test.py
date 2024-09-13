#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_MaxInteger(self):
        # Test the max integer
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([5, 2, 3, 4]), 5)
        self.assertAlmostEqual(max_integer([5, 6, 3, 4]), 6)
        self.assertAlmostEqual(max_integer([5, 6, -1, 4]), 6)
        self.assertAlmostEqual(max_integer([-5, -6, -3, -4]), -3)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)