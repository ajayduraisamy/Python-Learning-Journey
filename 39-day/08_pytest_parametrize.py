# 08_pytest_parametrize.py
# Pytest parameterized testing

import pytest

@pytest.mark.parametrize("x, expected", [(2,4), (3,9), (4,16)])
def test_square(x, expected):
    assert x * x == expected
