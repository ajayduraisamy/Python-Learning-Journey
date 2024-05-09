# 06_pytest_basic.py
# Basic pytest example
# Run with: pytest -q

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
