from .. import UnitTable

class mass(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is gram
        self._base_unit = 'g'

        # Kilogram
        self._to_base_unit['kg']    = lambda x: x * 1000.0
        self._from_base_unit['kg']  = lambda x: x / 1000.0

        # Metric Ton
        self._to_base_unit['t']     = lambda x: x * 1000000.0
        self._from_base_unit['t']   = lambda x: x / 1000000.0

        # Pound
        self._to_base_unit['lb']    = lambda x: x / 0.0022046
        self._from_base_unit['lb']  = lambda x: x * 0.0022046

        # Stone
        self._to_base_unit['st']    = lambda x: x / 0.00015747
        self._from_base_unit['st']  = lambda x: x * 0.00015747

        # Ounce
        self._to_base_unit['oz']    = lambda x: x / 0.035274
        self._from_base_unit['oz']  = lambda x: x * 0.035274
