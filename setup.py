from setuptools import setup

setup(
    name='bashim',
    version='0.1',
    license='MIT',
    author='Anton Kostryukov',
    author_email='anton97kos@gmail.com',
    description='bash.im CL client.',
    py_modules=['bashim_cl', 'core'],
    include_package_data=True,
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'requests',
        'lxml'
    ],
    entry_points={
        'console_scripts': ['bashim=bashim_cl.clc:main_f'],
    }
)
