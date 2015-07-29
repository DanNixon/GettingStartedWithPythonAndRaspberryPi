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
        self.cbSourceUnit.currentIndexChanged[str].connect(self.calculate)
        self.cbDestUnit.currentIndexChanged[str].connect(self.calculate)
        self.sbSourceValue.valueChanged.connect(self.calculate)

        self.unit_table_selected(self.cbUnitTable.currentText())


    def unit_table_selected(self, table_name):
        table = get_table(str(table_name))
        units = table.get_units()

        self.cbSourceUnit.blockSignals(True)
        self.cbDestUnit.blockSignals(True)

        self.cbSourceUnit.clear()
        self.cbDestUnit.clear()

        for unit in units:
            self.cbSourceUnit.addItem(unit)
            self.cbDestUnit.addItem(unit)

        self.cbSourceUnit.blockSignals(False)
        self.cbDestUnit.blockSignals(False)


    def calculate(self):
        table = get_table(str(self.cbUnitTable.currentText()))
        source_value = self.sbSourceValue.value()
        source_unit = str(self.cbSourceUnit.currentText())
        dest_unit = str(self.cbDestUnit.currentText())

        result_value = table.convert(source_unit, dest_unit, source_value)
        self.leDestValue.setText(str(result_value))
