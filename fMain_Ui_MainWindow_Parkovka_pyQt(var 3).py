# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import ui_Parkovka_pyQt

class MyWindow(QtWidgets.QWidget, ui_Parkovka_pyQt.Ui_MainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())