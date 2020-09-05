#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'SPOClient'
DESCRIPTION = 'A simple python Sharepoint Online client to query Sharepoint API'
URL = 'https://github.com/lalondesteve/SPOClient'
EMAIL = 'lalondesteve@gmail.com'
AUTHOR = 'Steve Lalonde'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

REQUIRED = [
    'requests', 'wheel', 'python-dotenv'
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['SPOClient'],
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
)
