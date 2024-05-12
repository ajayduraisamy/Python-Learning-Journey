# 08_test_core.py
# Basic tests for core functions

from .01_core import organize_files
import os

def test_folder_exists():
    assert os.path.exists(".")
