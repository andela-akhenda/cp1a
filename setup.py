# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup_requires = [
    'pytest-runner'
    ]

tests_require = [
    'pytest-cov',
    'pytest'
    ]

setup(
    name='amity',
    version='0.0.1',
    description='Amity Room Allocation System',
    long_description=readme,
    author='Joseph Akhenda',
    author_email='joseph.akhenda@andela.com',
    url='https://github.com/andela-akhenda/cp1a',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=setup_requires,
    tests_require=tests_require,
)
