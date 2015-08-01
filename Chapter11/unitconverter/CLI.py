import argparse
import inspect
from Converter import get_table, convert_units


def run_cli():
    parser = argparse.ArgumentParser(description='Tool for converting units')

    parser.add_argument(
        'table',
        metavar='TABLE',
        action='store',
        type=str,
        help='Unit table to use in conversion'
    )

    subparsers = parser.add_subparsers(help='operation to be performed')

    list_table_parser = subparsers.add_parser('list')
    list_table_parser.set_defaults(which='list')

    list_table_parser.add_argument(
        '-m', '--method',
        action='store_true',
        help='Also output the conversion method from the base unit'
    )

    conversion_parser = subparsers.add_parser('convert')
    conversion_parser.set_defaults(which='convert')

    conversion_parser.add_argument(
        'value',
        metavar='VALUE',
        type=float,
        action='store',
        help='The value to convert'
    )

    conversion_parser.add_argument(
        'from_unit',
        metavar='FROM',
        action='store',
        type=str,
        help='Unit to convert from'
    )

    conversion_parser.add_argument(
        'to_units',
        metavar='TO',
        action='store',
        nargs='+',
        type=str,
        help='Unit(s) to convert to'
    )

    props = parser.parse_args()

    if props.which == 'list':
        _run_unit_list(props)
    elif props.which == 'convert':
        _run_conversion(props)


def _run_unit_list(props):
    """
    Runs the command line interface for unit listing mode.

    @param props Properties parsed by argparse
    """

    table = get_table(props.table)
    print 'Unit table %s can convert between the units:'
    for unit in table.get_units():
        if props.method:
            if unit == table.base_unit:
                formula = 'base unit'
            else:
                conversion = inspect.getsource(table.from_base_unit[unit])
                formula = conversion[conversion.index(':')+1:conversion.index('\n')].strip()
            print '%s (%s)' % (unit, formula)
        else:
            print unit


def _run_conversion(props):
    """
    Runs the command line interface for unit conversion mode.

    @param props Properties parsed by argparse
    """

    results = convert_units(table_name=props.table,
                            value=props.value,
                            value_unit=props.from_unit,
                            targets=props.to_units)

    for result in results:
        print '%f %s = %f %s' % (props.value, props.from_unit,
                                 result['converted_value'],
                                 result['dest_unit'])
