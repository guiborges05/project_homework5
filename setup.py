from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflake",
    version="0.1",
    author="Guilherme Borges",
    author_email="gui.borges05@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)
