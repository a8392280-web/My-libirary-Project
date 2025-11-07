import sys

from PySide6 import QtWidgets
from app.controllers.main_widget import Widget

app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show() 

app.exec()


