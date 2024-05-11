# 08_test_password.py
# Basic tests (run with pytest)

from .01_password_gen import generate_password

def test_length_default():
    p = generate_password()
    assert isinstance(p, str)
    assert len(p) == 12

def test_custom_length():
    p = generate_password(length=20)
    assert len(p) == 20
