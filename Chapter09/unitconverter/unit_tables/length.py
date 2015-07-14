from .. import UnitTable

class length(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is meters
        self.base_unit = 'm'

        # Centimeters
        self.to_base_unit['cm']    = lambda x: x / 100.0
        self.from_base_unit['cm']  = lambda x: x * 100.0

        # Millimeters
        self.to_base_unit['mm']    = lambda x: x / 1000.0
        self.from_base_unit['mm']  = lambda x: x * 1000.0

        # Kilometers
        self.to_base_unit['mm']    = lambda x: x / 1000.0
        self.from_base_unit['mm']  = lambda x: x * 1000.0

        # Micrometers
        self.to_base_unit['um']    = lambda x: x / 1000000.0
        self.from_base_unit['um']  = lambda x: x * 1000000.0

        # Miles
        self.to_base_unit['mi']    = lambda x: x / 0.00062137
        self.from_base_unit['mi']  = lambda x: x * 0.00062137

        # Yards
        self.to_base_unit['yd']    = lambda x: x / 1.0936
        self.from_base_unit['yd']  = lambda x: x * 1.0936

        # Feet
        self.to_base_unit['ft']    = lambda x: x / 3.2808
        self.from_base_unit['ft']  = lambda x: x * 3.2808

        # Inches
        self.to_base_unit['in']    = lambda x: x / 39.370
        self.from_base_unit['in']  = lambda x: x * 39.370

        # Mils
        self.to_base_unit['mil']   = lambda x: x / 39370.078740158
        self.from_base_unit['mil'] = lambda x: x * 39370.078740158
