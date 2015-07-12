from setuptools import setup

setup(
    name='unitconverter',
    version='0.1.0',
    entry_points = {
        'console_scripts': ['unitconvert=unitconverter.CLI:run_cli'],
    },
    description='Command line tool for unit conversion',
    classifiers=[
	'Natural Language :: English',
	'Programming Language :: Python :: 2.7',
    ],
    author='Dan Nixon',
    packages=['unitconverter', 'unitconverter.unit_tables'],
    include_package_data=True,
    zip_safe=False)
