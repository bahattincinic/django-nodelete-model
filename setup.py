#!/usr/bin/env python

from setuptools import setup

setup(
    name="django-nodelete-model",
    version='0.1',
    url='http://github.com/django-nodelete-model',
    author='Bahattin Cinic',
    author_email='bahattincinic@gmail.com',
    description='No Delete Model for django',
    install_requires=[
        'django>=1.4',
    ],
    license='MIT',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ]
)
