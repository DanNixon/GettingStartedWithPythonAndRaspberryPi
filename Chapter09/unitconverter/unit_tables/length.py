from .. import UnitTable

class length(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is meters
        self._base_unit = 'm'

        # Centimeters
        self._to_base_unit['cm']    = lambda x: x / 100.0
        self._from_base_unit['cm']  = lambda x: x * 100.0

        # Millimeters
        self._to_base_unit['mm']    = lambda x: x / 1000.0
        self._from_base_unit['mm']  = lambda x: x * 1000.0

        # Kilometers
        self._to_base_unit['mm']    = lambda x: x / 1000.0
        self._from_base_unit['mm']  = lambda x: x * 1000.0

        # Micrometers
        self._to_base_unit['um']    = lambda x: x / 1000000.0
        self._from_base_unit['um']  = lambda x: x * 1000000.0

        # Miles
        self._to_base_unit['mi']    = lambda x: x / 0.00062137
        self._from_base_unit['mi']  = lambda x: x * 0.00062137

        # Yards
        self._to_base_unit['yd']    = lambda x: x / 1.0936
        self._from_base_unit['yd']  = lambda x: x * 1.0936

        # Feet
        self._to_base_unit['ft']    = lambda x: x / 3.2808
        self._from_base_unit['ft']  = lambda x: x * 3.2808

        # Inches
        self._to_base_unit['in']    = lambda x: x / 39.370
        self._from_base_unit['in']  = lambda x: x * 39.370

        # Mils
        self._to_base_unit['mil']   = lambda x: x / 39370.078740158
        self._from_base_unit['mil'] = lambda x: x * 39370.078740158
