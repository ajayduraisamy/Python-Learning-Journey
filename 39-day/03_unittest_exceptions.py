# 03_unittest_exceptions.py
# Testing exceptions

import unittest

def divide(a, b):
    return a / b

class TestDivide(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()
