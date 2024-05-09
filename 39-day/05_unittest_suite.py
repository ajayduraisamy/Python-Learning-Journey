# 05_unittest_suite.py
# Running multiple test cases in a suite

import unittest

class TestA(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)

class TestB(unittest.TestCase):
    def test_two(self):
        self.assertEqual("hi".upper(), "HI")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestA("test_one"))
    suite.addTest(TestB("test_two"))
    unittest.TextTestRunner().run(suite)
