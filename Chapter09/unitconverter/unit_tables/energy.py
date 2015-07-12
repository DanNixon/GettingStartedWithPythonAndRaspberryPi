from .. import UnitTable

class energy(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is Joule
        self._base_unit = 'j'

        # Electron volt
        self._to_base_unit['ev']        = lambda x: x / 6241506480000000000.0
        self._from_base_unit['ev']      = lambda x: x * 6241506480000000000.0

        # Calorie (chemical)
        self._to_base_unit['cal']       = lambda x: x / 0.23900573614
        self._from_base_unit['cal']     = lambda x: x * 0.23900573614

        # Calorie (nutritional)
        self._to_base_unit['kcal']      = lambda x: x / 0.00023884589663
        self._from_base_unit['kcal']    = lambda x: x * 0.00023884589663

        # Horsepower hour
        self._to_base_unit['hph']       = lambda x: x / 3.7250614123e-7
        self._from_base_unit['hph']     = lambda x: x * 3.7250614123e-7

        # Watt hour
        self._to_base_unit['wh']        = lambda x: x / 0.00027777777778
        self._from_base_unit['wh']      = lambda x: x * 0.00027777777778

        # BTU
        self._to_base_unit['btu']       = lambda x: x / 0.00094781707775
        self._from_base_unit['btu']     = lambda x: x * 0.00094781707775
