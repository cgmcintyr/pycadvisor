# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pycadvisor',
    version='0.0.1',
    description='Wrapper for google cadvisor api',
    long_description=readme,
    author='Christopher McIntyre',
    author_email='me@cgmcintyre.com',
    url='https://github.com/cgmcintyr/pycadvisor',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='nose.collector',
    tests_require=['nose'],
)
