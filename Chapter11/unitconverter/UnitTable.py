class UnitTable(object):
    """
    A class to manage conversion of units for the same quantity (e.g. length,
    volume, mass)
    """

    def __init__(self):
        self.base_unit = None
        self.to_base_unit = {}
        self.from_base_unit = {}


    def convert(self, source, dest, value):
        """
        Converts a value in one unit to another.

        @param source The source unit
        @param dest The destination unit
        @param value The value to convert
        @return The value in the destination unit
        """

        if not (self.can_convert(source) and self.can_convert(dest)):
            raise ValueError('Cannot convert given units')

        if source != self.base_unit:
            value = self.to_base_unit[source](value)

        if dest != self.base_unit:
            value = self.from_base_unit[dest](value)

        return value


    def get_units(self):
        """
        Returns a list of units that this table can convert.

        @return List of valid units
        """

        convertable_units = set(self.to_base_unit.keys()) & set(self.from_base_unit.keys())
        convertable_units.add(self.base_unit)
        return convertable_units


    def can_convert(self, unit):
        """
        Checks to see if this table can convert a given unit.

        @param unit Name of unit to check
        @return Boolean indicating if this unit can be converted
        """

        return unit.lower() in self.get_units()
