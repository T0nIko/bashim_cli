from setuptools import setup

setup(
    name='bashim_cli',
    version='0.1',
    license='MIT',
    author='Anton Kostryukov',
    author_email='anton97kos@gmail.com',
    description='bash.im CL client.',
    py_modules=['clc'],
    include_package_data=True,
    install_requires=[
        'Click',
        'beautifulsoup4',
        'requests',
        'lxml'
    ],
    entry_points='''
        [console_scripts]
        bashim=clc:bashim_clc
    ''',
)
