import pathlib
from setuptools import setup
from jsonstorage import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="jsonstorage",
    version=f"{__version__}",
    description="JSON Storage is a simple lightweight data storage using JSON format in Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/leopires/json_storage",
    author="Leonardo Pires",
    author_email="lbpires@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["jsonstorage"]
)
