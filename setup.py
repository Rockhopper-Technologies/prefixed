#!/usr/bin/env python
# Copyright 2020 - 2022 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Prefixed Library setup file
"""

import os

from setuptools import setup, find_packages

from setup_helpers import get_version, readme

setup(
    name='prefixed',
    version=get_version(os.path.join('prefixed', '__init__.py')),
    description="Prefixed alternative numeric library",
    long_description=readme('README.rst'),
    author='Avram Lubkin',
    author_email='avylove@rockhopper.net',
    maintainer='Avram Lubkin',
    maintainer_email='avylove@rockhopper.net',
    url='https://github.com/Rockhopper-Technologies/prefixed',
    project_urls={'Documentation': 'https://prefixed.readthedocs.io'},
    license='MPLv2.0',
    zip_safe=False,
    install_requires=[],
    tests_require=['unittest2; python_version < "2.7"'],
    packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    test_suite='tests',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals',
    ],
    keywords='si iec prefix nist',
)
