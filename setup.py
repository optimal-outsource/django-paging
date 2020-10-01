#!/usr/bin/env python

from setuptools import setup, find_packages

tests_require = [
    'unittest2',
    'django',
]

setup(
    name='django-paging',
    version='0.4',
    author='David Cramer, Adam Stein',
    author_email='adam@csh.rit.edu',
    url='http://github.com/optimal-outsource/django-paging',
    install_requires=[
        'django-templatetag-sugar>=1.1',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='unittest2.collector',
    description='An efficient paginator that works.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
