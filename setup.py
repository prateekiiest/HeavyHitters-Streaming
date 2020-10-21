# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
  name='heavyHitters',
  version='1.0.0',
  long_description='Find top K Heavy Hitters',
  author='Prateek Chanda',
  author_email='prateekkol21@gmail.com',
  license='BSD',
  description=('Find top K Heavy Hitters'),
  packages=['heavyHitters'],
  install_requires=['numpy'],
  platforms='any',
)