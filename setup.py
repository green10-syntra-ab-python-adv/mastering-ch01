# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='examples',
    version='0.1.0',
    description='Python Advanced D01',
    long_description=readme,
    author='Hans Vandenbogaerde',
    author_email='Hans Vandenbogaerde',
    url='https://github.com/HansVdb/pythonavd-d01.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

