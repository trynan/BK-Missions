from PySide6 import QtWidgets, QtGui, QtCore

# button with rich text (used here for multiline text)
# https://stackoverflow.com/questions/8960233/subclassing-qlabel-to-show-native-mouse-hover-button-indicator/8960548#8960548
class richButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__()
        self.bigFnt = QtGui.QFont()
        self.bigFnt.setPointSize(12)

        self.text = QtWidgets.QLabel(text)
        self.text.setFont(self.bigFnt)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.text.setMouseTracking(False)
        self.text.setWordWrap(True)
        self.lay = QtWidgets.QVBoxLayout()
        # self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.text)
        self.setLayout(self.lay)
        # make the button big enough to fit the text
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
    
    def setText(self, text):
        self.text.setText(text)