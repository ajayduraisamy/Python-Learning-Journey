# 05_setup.py
# Classic Python packaging using setup.py

from setuptools import setup, find_packages

setup(
    name="my-awesome-package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Ajay",
    description="A simple demo Python package"
)
