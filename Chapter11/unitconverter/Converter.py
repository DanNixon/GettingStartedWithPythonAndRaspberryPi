import importlib


def get_table(table_name):
    """
    Returns an instance of a unit table given the name of the table.

    @param table_name Name of table to retrieve
    @return UnitTable instance
    """

    converter_module = importlib.import_module('unitconverter.unit_tables.%s' % table_name)
    converter_class = getattr(converter_module, table_name)()
    return converter_class


def convert_units(table_name, value, value_unit, targets):
    """
    Converts a given value in a unit to a set of target units.

    @param table_name Name of table units are contained in
    @param value Value to convert
    @param value_unit Unit value is currently in
    @param targets List of units to convert to
    @return List of conversions
    """

    table = get_table(table_name)

    results = list()
    for target in targets:
        result = {'dest_unit': target}
        try:
            result['converted_value'] = table.convert(value_unit, target, value)
        except ValueError:
            continue
        results.append(result)

    return results
