# -*- coding: utf8 -*-

"""
"""

from __future__ import print_function
import os
import re
import setuptools
import shutil

setuptools.setup(
    name="ldsc",
    version='1.0.1',
    url="https://github.com/bulik/ldsc",
    author="Brendan Bulik-Sullivan and Hilary Finucane",
    author_email="",
    description="",
    packages=setuptools.find_packages(),
    py_modules=[
    ],
    requires=[
    ],
    entry_points={
        'console_scripts': ['ldsc = ldsc.ldsc:main',
                            'ldsc_munge_sumstats = ldsc.munge_sumstats:main',
                        ]
    },
)

