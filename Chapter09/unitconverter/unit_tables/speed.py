from .. import UnitTable

class speed(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is ms-1
        self._base_unit = 'ms-1'

        # Miles per hour
        self._to_base_unit['mph']       = lambda x: x * 2.2369
        self._from_base_unit['mph']     = lambda x: x / 2.2369

        # Kilometers per hour
        self._to_base_unit['kph']       = lambda x: x * 3.6
        self._from_base_unit['kph']     = lambda x: x / 3.6

        # Mach (20C at sea level)
        self._to_base_unit['mach']      = lambda x: x / 0.0029387
        self._from_base_unit['mach']    = lambda x: x * 0.0029387

        # Knots
        self._to_base_unit['knot']      = lambda x: x * 1.94384449
        self._from_base_unit['knot']    = lambda x: x / 1.94384449

        # Light speed
        self._to_base_unit['c']         = lambda x: x / 3.3356e-9
        self._from_base_unit['c']       = lambda x: x * 3.3356e-9
