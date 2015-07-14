from .. import UnitTable

class angle(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is degrees
        self.base_unit = 'degree'

        # Radians
        self.to_base_unit['radian']        = lambda x: x / 0.0174532925
        self.from_base_unit['radian']      = lambda x: x * 0.0174532925
