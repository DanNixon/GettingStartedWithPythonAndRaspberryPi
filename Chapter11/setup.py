from setuptools import setup

setup(
    name='unitconverter',
    version='0.1.0',
    entry_points = {
        'console_scripts': ['unitconvert=unitconverter.CLI:run_cli'],
        'gui_scripts': ['unitconverter-ui=unitconverter.gui:run_gui']
    },
    description='Command line tool for unit conversion',
    classifiers=[
	'Natural Language :: English',
	'Programming Language :: Python :: 2.7',
    ],
    author='Dan Nixon',
    packages=['unitconverter', 'unitconverter.unit_tables', 'unitconverter.gui'],
    include_package_data=True,
    zip_safe=False,
    package_data = {
        '': ['*.ui']
    })
