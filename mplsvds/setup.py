#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mplsvds',
    version='0.1.7',
    author='Daniel Margala, Jonathan Whitmore',
    author_email='daniel@svds.com, jonathan@svds.com',
    packages=['mplsvds', 'mplsvds.test'],
    include_package_data=True,
    # license='LICENSE.txt',
    description='matplotlib styling for svds',
    long_description='matplotlib styling for svds!',
    install_requires=[
          'numpy',
          'scipy',
          'matplotlib',
          'pandas',
          'seaborn',
      ],
)
