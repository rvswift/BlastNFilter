#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "biopython"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='BlastNFilter',
    version='0.1.0',
    description="Blast N filter processes pre-releases from wwpdb for weekly cross-docking exercises.",
    long_description=readme + '\n\n' + history,
    author="Rob Swift",
    author_email='robvswift@gmail.com',
    url='https://github.com/rvswift/BlastNFilter',
    packages=[
        'BlastNFilter', 'BlastNFilter.Blast', 'BlastNFilter.PreRelease', 'BlastNFilter.Utilities'
    ],
    package_dir={'BlastNFilter':
                 'BlastNFilter'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='BlastNFilter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    scripts=[ 'BlastNFilter/blastnfilter.py' ],
    test_suite='tests',
    tests_require=test_requirements
)
