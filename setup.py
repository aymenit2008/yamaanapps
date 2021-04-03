# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in yamaanapps/__init__.py
from yamaanapps import __version__ as version

setup(
	name='yamaanapps',
	version=version,
	description='yamaan apps',
	author='yamaan apps',
	author_email='yamaanapp@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
