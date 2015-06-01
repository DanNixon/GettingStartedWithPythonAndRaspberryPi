#!/usr/bin/env python

from setuptools import setup

setup(
    name="calcpy",
    version="0.0.1",
    description="A basic calculator",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
    ],
    author="Dan Nixon",
    packages=["calcpy", "calcpy.calculator"],
    install_requires=[
        "numpy"
    ])
