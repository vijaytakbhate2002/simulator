import io
import os
from pathlib import Path
from setuptools import find_packages, setup

NAME = 'simulator'
DESCRIPTION = """Compare each common columns from two csv's and return comparision of each column and comparison flag for each column which is TRUE or FALSE. This package has JsonOperations class which handles json path_based operations readPath: this function will read data from specified path, updatePath: this function will update data from specified path, createPath: this function will create path inside json and assign specified value to it changeByReference: this function can copy specified path from one json and can assign same value to destination json on specified destination path"""


URL = 'https://github.com/Vijay-Takbhate-incred/simulator.git'
EMAIL = 'vijay.takbhate@incred.com'
AUTHOR = 'Vijay Dipak Takbhate'
REQUIRES_PYTHON = '>=3.10'

pwd = os.path.abspath(os.path.dirname(__file__))

def list_reqs(fname='requirements.txt'):
    try:
        with io.open(os.path.join(pwd, fname), encoding='utf-8') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        pass

try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME

setup(
    name=NAME,
    version="1.1.2",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={NAME: ['VERSION']},
    extras_require={},
    include_package_data=True,
    license='MIT'
)
