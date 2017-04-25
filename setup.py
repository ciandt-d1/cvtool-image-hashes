# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "image_hash"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Kingpick ImageMatch API",
    author_email="",
    url="",
    keywords=["Swagger", "Kingpick ImageMatch API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    Image Perceptual Hash services. Search for images that look similar to each other.
    """
)

