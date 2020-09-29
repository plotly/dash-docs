import json
import os
from setuptools import setup

setup(
    name='dash_docs',
    packages=[
        'dash_docs',
        'dash_docs.tutorial',
    ],
    include_package_data=True,
    install_requires=[],
    version='0.4.1'
)
