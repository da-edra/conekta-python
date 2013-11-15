#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from setuptools import setup, find_packages

version = "0.9"
author = "Julian Ceballos"

setup(
    name='conekta',
    version=version,
    author=author,
    author_email='julian@pikhub.com',
    url='https://github.com/conekta/conekta-python',
    description='Easy Conekta python wrapper',
    long_description=open('./README.txt', 'r').read(),
    download_url='https://github.com/conekta/conekta-python/tarball/master',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        ],
    packages=find_packages(),
    install_requires=[
        'httplib2',
        'simplejson',
        'nose'
    ],
    license='MIT License',
    keywords='conekta wrapper',
    include_package_data=True,
    zip_safe=True,
)
