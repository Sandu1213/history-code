# -*- coding: utf-8 -*-
import io
from setuptools import find_packages, setup

install_requires = open("requirements.txt").readlines()

setup(
    name='Autotest',
    version='v0.1.0',
    description='test the website which is keepwork',
    author='Duke',
    author_email='dslhmily@163.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['test.*', 'test']),
    keywords='UI test, Web test',
    install_requires=install_requires    
)
