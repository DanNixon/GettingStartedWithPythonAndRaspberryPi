from .. import UnitTable

class temperature(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is Kelvin
        self.base_unit = 'k'

        # Degrees Celsius
        self.to_base_unit['c']     = lambda x: x + 273.15
        self.from_base_unit['c']   = lambda x: x - 273.15

        # Degrees Fahrenheit
        self.to_base_unit['f']     = lambda x: (x + 459.67) * (5.0 / 9.0)
        self.from_base_unit['f']   = lambda x: (x / (5.0 /9.0)) - 459.67
