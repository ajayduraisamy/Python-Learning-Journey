# 09_pytest_mock.py
# Mocking with pytest

from unittest.mock import patch

def get_user():
    return {"user": "Original"}

@patch("__main__.get_user", return_value={"user": "Mocked"})
def test_mocking(mock_fn):
    assert get_user()["user"] == "Mocked"
