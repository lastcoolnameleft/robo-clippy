# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='robo_clippy',
    version='0.1.0',
    description='Robo-Clippy.  Hopefully not as annoying this time.',
    long_description=readme,
    author='Tommy Falgout',
    author_email='tommy@lastcoolnameleft.com',
    url='https://github.com/lastcoolnameleft/robo-clippy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

