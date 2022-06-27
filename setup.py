# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in idelta_website/__init__.py
from idelta_website import __version__ as version

setup(
	name='idelta_website',
	version=version,
	description='Idelta Website',
	author='Taiwo Akinosho',
	author_email='tiwiex@yahoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
