from setuptools import setup, find_packages

setup(
	name='eryk_bbs',
	version='0.1.0',
	description='My own BBS generator implementation (use only for educational purposes!)',
	author='Eryk Andrzejewski',
	author_email='erykandrzejewski@gmail.com',
	url='https://github.com/qwercik/eryk_bbs'
	packages=find_packages()
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.7',
)

