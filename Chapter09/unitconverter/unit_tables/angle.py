from .. import UnitTable

class angle(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is degrees
        self._base_unit = 'degree'

        # Radians
        self._to_base_unit['radian']        = lambda x: x / 0.0174532925
        self._from_base_unit['radian']      = lambda x: x * 0.0174532925
