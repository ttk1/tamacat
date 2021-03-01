#!/bin/env python

from setuptools import setup

setup(
    name='tamacat',
    version='1.0.0',
    packages=['tamacat'],
    entry_points={
        'console_scripts': [
            'tamacat = tamacat.main:main'
        ]
    }
)
