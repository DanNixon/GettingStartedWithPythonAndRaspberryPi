import os.path
from PyQt4 import uic
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import SIGNAL


ui_filename = os.path.splitext(__file__)[0] + '.ui'
ui_UnitConverter = uic.loadUiType(ui_filename)[0]


class UnitConverter(QMainWindow, ui_UnitConverter):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.action_Exit.triggered.connect(QApplication.exit)
