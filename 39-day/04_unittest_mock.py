# 04_unittest_mock.py
# Mocking with unittest.mock

import unittest
from unittest.mock import patch

def fetch_user():
    return {"name": "RealUser"}

class TestMock(unittest.TestCase):
    @patch("__main__.fetch_user", return_value={"name": "MockUser"})
    def test_mock_user(self, mock_fn):
        self.assertEqual(fetch_user()["name"], "MockUser")

if __name__ == "__main__":
    unittest.main()
