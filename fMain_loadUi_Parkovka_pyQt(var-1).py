# -*- coding: utf-8 -*-

#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('D:/MyProjects/MyWorkInPython/Parkovka_pyQt/Parkovka_pyQt.git/Parkovka_pyQt(form).ui')
window.show()
sys.exit(app.exec_())



