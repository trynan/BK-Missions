from PySide6 import QtWidgets, QtGui, QtCore

# window for listing missions
class listWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)
        self.setWindowTitle("List of Missions")
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QTextEdit()
        self.text.setReadOnly(True)
        self.mainLayout.addWidget(self.text)