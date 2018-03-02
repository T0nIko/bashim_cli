from setuptools import setup, find_packages

setup(
    name='bashim',
    version='0.1.0',
    license='MIT',
    author='Anton Kostryukov',
    author_email='anton97kos@gmail.com',
    description='bash.im terminal client',
    long_description='Quite simple command line tool for reading bash.im.',
    py_modules=['clc', 'core'],
    packages=find_packages(),
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'requests',
        'lxml'
    ],
    entry_points={
        'console_scripts': ['bashim=clc:main'],
    }
)
