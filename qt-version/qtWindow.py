# Original version by Trynan and Wedarobi
# Maintained by Trynan
# BK Missions idea by CrozB
# Mission generation logic and missions by CrozB
# 8/11/2020 - 1/5/2022

from PySide6 import QtWidgets, QtGui, QtCore
import sys

## the structure is something like this:
# top buttons (encased in topBox)
# seed stuff (encased in seedBox)
# bottom five buttons are encased in buttonBox
# bottom five text boxes are encased in textBox
# those boxes are encased together in bottomBox


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
        # self.text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        # self.text.setMouseTracking(False)
        self.text.setWordWrap(True)
        self.lay = QtWidgets.QVBoxLayout()
        # self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.text)
        self.setLayout(self.lay)
        # make the button big enough to fit the text
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
    
    def setText(self, text):
        self.text.setText(text)

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

# the secret to using groupboxes is you just make everything as normal (with boxlayouts),
# and then with the groupbox you make it, set its layout to the layout
# you want to be surrounded by the box, and then instead of adding the
# layout to the main layout, you add the group box instead.
class bkWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BK Missions")
        self.setMinimumHeight(550)
        self.smallFnt = QtGui.QFont()
        self.smallFnt.setPointSize(14)

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        # don't stretch horizontally
        self.maxHPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        # don't stretch vertically
        self.maxVPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        # take up space
        self.minPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)


        ##
        # top buttons
        self.topLayout = QtWidgets.QVBoxLayout()
        self.topLayout.setContentsMargins(0, 0, 0, 0)  # to remove margins added by QFrame
        self.topBox = QtWidgets.QFrame()
        self.topBox.setLayout(self.topLayout)
        self.topBox.setSizePolicy(self.maxVPolicy)

        self.genMissionsBtn = QtWidgets.QPushButton("Generate Missions")
        self.listMissionsBtn = QtWidgets.QPushButton("Show List of Missions")
        self.settingsBtn = QtWidgets.QPushButton("Settings")

        self.genMissionsBtn.clicked.connect(self.generateMissions)
        self.listMissionsBtn.clicked.connect(self.listMissions)
        self.settingsBtn.clicked.connect(self.showSettings)

        self.topLayout.addWidget(self.genMissionsBtn)
        self.topLayout.addWidget(self.listMissionsBtn)
        self.topLayout.addWidget(self.settingsBtn)


        ##
        # seed
        self.seedGrid = QtWidgets.QGridLayout()
        self.seedGrid.setContentsMargins(0, 0, 0, 0)
        self.seedBox = QtWidgets.QFrame()
        self.seedBox.setLayout(self.seedGrid)
        self.seedBox.setSizePolicy(self.maxVPolicy)

        self.copySeedBtn = QtWidgets.QPushButton("Copy")
        self.currentSeedLabel = QtWidgets.QLabel("Current Seed:")
        self.currentSeedBox = QtWidgets.QLineEdit()
        self.useSeedCheck = QtWidgets.QCheckBox()
        self.useSeedLabel = QtWidgets.QLabel("Custom Seed:")
        self.customSeedBox = QtWidgets.QLineEdit()

        self.customSeedBox.setEnabled(False)
        self.currentSeedBox.setEnabled(False)
        self.useSeedCheck.stateChanged.connect(self.enableCustomSeed)
        self.copySeedBtn.clicked.connect(self.copySeed)

        self.seedGrid.addWidget(self.copySeedBtn, 0, 0)
        self.seedGrid.addWidget(self.currentSeedLabel, 0, 1)
        self.seedGrid.addWidget(self.currentSeedBox, 0, 2)
        self.seedGrid.addWidget(self.useSeedCheck, 1, 0, QtCore.Qt.AlignCenter)
        self.seedGrid.addWidget(self.useSeedLabel, 1, 1)
        self.seedGrid.addWidget(self.customSeedBox, 1, 2)


        ##
        # buttons and text boxes
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.textLayout = QtWidgets.QVBoxLayout()
        self.bottomLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.textLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomBox = QtWidgets.QFrame()
        self.buttonBox = QtWidgets.QFrame()
        self.textBox = QtWidgets.QFrame()
        self.textBox.hide()
        self.bottomBox.setLayout(self.bottomLayout)
        self.buttonBox.setLayout(self.buttonLayout)
        self.textBox.setLayout(self.textLayout)

        self.b1 = richButton("First Goal")
        self.b2 = richButton("Second Goal")
        self.b3 = richButton("Third Goal")
        self.b4 = richButton("Fourth Goal")
        self.b5 = richButton("Fifth Goal")
        self.buttons = [self.b1, self.b2, self.b3, self.b4, self.b5]

        self.t1 = QtWidgets.QTextEdit()
        self.t2 = QtWidgets.QTextEdit()
        self.t3 = QtWidgets.QTextEdit()
        self.t4 = QtWidgets.QTextEdit()
        self.t5 = QtWidgets.QTextEdit()
        self.text = [self.t1, self.t2, self.t3, self.t4, self.t5]


        # connect these explicitly because the lambda
        # doesn't work properly in a for loop for some reason
        self.b1.clicked.connect(lambda: self.changeColor(self.b1))
        self.b2.clicked.connect(lambda: self.changeColor(self.b2))
        self.b3.clicked.connect(lambda: self.changeColor(self.b3))
        self.b4.clicked.connect(lambda: self.changeColor(self.b4))
        self.b5.clicked.connect(lambda: self.changeColor(self.b5))
        for i in range(5):
            # self.buttons[i].setSizePolicy(self.minPolicy)
            # self.text[i].setSizePolicy(self.maxVPolicy)
            self.buttonLayout.addWidget(self.buttons[i])
            self.textLayout.addWidget(self.text[i])

        self.bottomLayout.addWidget(self.buttonBox)
        self.bottomLayout.addWidget(self.textBox)
        


        self.mainLayout.addWidget(self.topBox)
        self.mainLayout.addWidget(self.seedBox)
        self.mainLayout.addWidget(self.bottomBox)



    def generateMissions(self):
        print('generate missions')
    
    def listMissions(self):
        print('list')

    def showSettings(self):
        print('settings')

    def copySeed(self):
        print('copy')
    
    def enableCustomSeed(self):
        print("enable custom seed")

    def changeColor(self, b):
        print("change color")



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = bkWindow()
    win.show()

    sys.exit(app.exec())