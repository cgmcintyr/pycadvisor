# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import sys

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('tools/pip-requires') as f:
    pip_requires = f.read().splitlines()

with open('tools/test-requires') as f:
    test_requires = f.read().splitlines()

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        # import here, as outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

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
    install_requires=pip_requires,
    tests_require=['tox',] + test_requires,
    cmdclass = {'test': Tox},
)
