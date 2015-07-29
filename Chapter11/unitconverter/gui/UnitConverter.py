import os.path
from PyQt4 import uic
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import SIGNAL

from ..Converter import get_table

ui_filename = os.path.splitext(__file__)[0] + '.ui'
ui_UnitConverter = uic.loadUiType(ui_filename)[0]


class UnitConverter(QMainWindow, ui_UnitConverter):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.action_Exit.triggered.connect(QApplication.exit)
        self.cbUnitTable.currentIndexChanged[str].connect(self.unit_table_selected)
        self.cbSourceUnit.currentIndexChanged[str].connect(self.source_unit_selected)
        self.cbDestUnit.currentIndexChanged[str].connect(self.dest_unit_selected)
        self.sbSourceValue.valueChanged.connect(self.source_value_changed)

    def unit_table_selected(self, table_name):
        table = get_table(str(table_name))
        print table.get_units()

    def source_unit_selected(self, unit_name):
        print unit_name

    def dest_unit_selected(self, unit_name):
        print unit_name

    def source_value_changed(self, value):
        print value
