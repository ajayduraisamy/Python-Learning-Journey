# 10_pytest_full_flow.py
# Real pytest workflow: function -> test -> assertion

def format_name(fname, lname):
    return f"{fname.strip().title()} {lname.strip().title()}"

def test_format_name():
    assert format_name("  ajay  ", "durai  ") == "Ajay Durai"
