from .. import UnitTable

class length(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        self._base_unit = 'm'

        self._to_base_unit['cm']    = lambda x: x / 100.0
        self._from_base_unit['cm']  = lambda x: x * 100.0

        self._to_base_unit['mm']    = lambda x: x / 1000.0
        self._from_base_unit['mm']  = lambda x: x * 1000.0
