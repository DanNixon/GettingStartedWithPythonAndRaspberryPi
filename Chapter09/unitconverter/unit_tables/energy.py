from .. import UnitTable

class energy(UnitTable.UnitTable):

    def __init__(self):
        UnitTable.UnitTable.__init__(self)

        # Base unit is Joule
        self._base_unit = 'j'

        # TODO
