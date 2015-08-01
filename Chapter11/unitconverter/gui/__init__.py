import sys
from PyQt4.QtGui import QApplication

from UnitConverter import UnitConverter

def run_gui():
    app = QApplication(sys.argv)
    ui_window = UnitConverter(None)
    ui_window.show()
    app.exec_()
