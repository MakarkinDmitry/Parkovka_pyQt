# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys, ui_Parkovka_pyQt

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = ui_Parkovka_pyQt.Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())