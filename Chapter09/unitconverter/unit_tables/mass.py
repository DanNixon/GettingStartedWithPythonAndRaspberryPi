from .. import UnitTable

class mass(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is gram
        self._base_unit = 'g'

        #TODO
