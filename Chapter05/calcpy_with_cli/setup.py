from setuptools import setup

setup(
    name='calcpy',
    version='0.0.2',
    description='A basic calculator',
    entry_points={
        'console_scripts': [
            'calcpy = calcpy.cli:run_cli'
        ]
    },
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    author='Dan Nixon',
    author_email='dan@dan-nixon.com',
    packages=['calcpy', 'calcpy.calculator'],
    install_requires=[
        'numpy'
    ])
