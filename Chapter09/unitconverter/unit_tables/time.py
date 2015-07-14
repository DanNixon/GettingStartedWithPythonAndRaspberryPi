from .. import UnitTable

class time(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is second
        self.base_unit = 's'

        # Minute
        self.to_base_unit['m']     = lambda x: x * 60.0
        self.from_base_unit['m']   = lambda x: x / 60.0

        # Hour
        self.to_base_unit['h']     = lambda x: x * 3600.0
        self.from_base_unit['h']   = lambda x: x / 3600.0

        # Day
        self.to_base_unit['d']     = lambda x: x * 86400.0
        self.from_base_unit['d']   = lambda x: x / 86400.0

        # Year
        self.to_base_unit['y']     = lambda x: x * 3.15569e7
        self.from_base_unit['y']   = lambda x: x / 3.15569e7

        # Millisecond
        self.to_base_unit['ms']    = lambda x: x / 1000.0
        self.from_base_unit['ms']  = lambda x: x * 1000.0

        # Microsecond
        self.to_base_unit['us']    = lambda x: x / 1000000.0
        self.from_base_unit['us']  = lambda x: x * 1000000.0

        # Nanosecond
        self.to_base_unit['ns']    = lambda x: x / 1000000000.0
        self.from_base_unit['ns']  = lambda x: x * 1000000000.0
