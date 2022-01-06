from PySide6 import QtWidgets, QtGui, QtCore
import sys
import richButton

## the structure is something like this:
# top buttons and settings (encased in topBox)
# seed stuff (encased in seedBox)
# bottom five buttons (encased in bottomBox)

# the secret to using groupboxes is you just make everything as normal (with boxlayouts),
# and then with the groupbox you make it, set its layout to the layout
# you want to be surrounded by the box, and then instead of adding the
# layout to the main layout, you add the group box instead.

# the advantage to groupboxes is that they're like layouts that
# act more like widgets. otherwise they don't really do anything.
# so far these ones are not doing anything.
class bkWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BK Missions")
        self.setWindowIcon(QtGui.QIcon("kazooie.ico"))
        self.setMinimumHeight(550)
        self.clip = QtGui.QClipboard()

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        # don't stretch horizontally
        self.maxHPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        # don't stretch vertically
        self.maxVPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        # take up space
        self.minPolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)


        ##
        # top buttons and settings
        self.topLayout = QtWidgets.QVBoxLayout()
        self.topLayout.setContentsMargins(0, 0, 0, 0)  # to remove margins added by QFrame
        self.topBox = QtWidgets.QFrame()
        self.topBox.setLayout(self.topLayout)
        self.topBox.setSizePolicy(self.maxVPolicy)
        self.settingsLayout = QtWidgets.QHBoxLayout()

        self.genMissionsBtn = QtWidgets.QPushButton("Generate Missions")
        self.listMissionsBtn = QtWidgets.QPushButton("Show List of Missions")

        self.shortCheck = QtWidgets.QCheckBox("Short")
        self.randCheck = QtWidgets.QCheckBox("Randomize")
        self.codesCheck = QtWidgets.QCheckBox("Show Codes")

        self.genMissionsBtn.clicked.connect(self.generateMissions)
        self.listMissionsBtn.clicked.connect(self.listMissions)
        self.randCheck.setChecked(True)

        self.settingsLayout.addWidget(self.shortCheck)
        self.settingsLayout.addWidget(self.randCheck)
        self.settingsLayout.addWidget(self.codesCheck)
        self.topLayout.addWidget(self.genMissionsBtn)
        self.topLayout.addWidget(self.listMissionsBtn)
        self.topLayout.addLayout(self.settingsLayout)


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
        self.currentSeedBox.setReadOnly(True)
        self.useSeedCheck.stateChanged.connect(lambda: self.customSeedBox.setEnabled(not self.customSeedBox.isEnabled()))
        self.copySeedBtn.clicked.connect(lambda: self.clip.setText(self.currentSeedBox.text()))

        self.seedGrid.addWidget(self.copySeedBtn, 0, 0)
        self.seedGrid.addWidget(self.currentSeedLabel, 0, 1)
        self.seedGrid.addWidget(self.currentSeedBox, 0, 2)
        self.seedGrid.addWidget(self.useSeedCheck, 1, 0, QtCore.Qt.AlignCenter)
        self.seedGrid.addWidget(self.useSeedLabel, 1, 1)
        self.seedGrid.addWidget(self.customSeedBox, 1, 2)


        ##
        # buttons and text boxes
        self.bottomLayout = QtWidgets.QVBoxLayout()
        self.bottomLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomBox = QtWidgets.QFrame()
        self.bottomBox.setLayout(self.bottomLayout)

        self.b1 = richButton.richButton("First Goal")
        self.b2 = richButton.richButton("Second Goal")
        self.b3 = richButton.richButton("Third Goal")
        self.b4 = richButton.richButton("Fourth Goal")
        self.b5 = richButton.richButton("Fifth Goal")
        self.buttons = [self.b1, self.b2, self.b3, self.b4, self.b5]


        # connect these explicitly because the lambda
        # doesn't work properly in a for loop for some reason
        self.b1.clicked.connect(lambda: self.changeColor(self.b1))
        self.b2.clicked.connect(lambda: self.changeColor(self.b2))
        self.b3.clicked.connect(lambda: self.changeColor(self.b3))
        self.b4.clicked.connect(lambda: self.changeColor(self.b4))
        self.b5.clicked.connect(lambda: self.changeColor(self.b5))
        for i in range(5):
            self.bottomLayout.addWidget(self.buttons[i])


        ##
        # connect everything up to main
        self.mainLayout.addWidget(self.topBox)
        self.mainLayout.addWidget(self.seedBox)
        self.mainLayout.addWidget(self.bottomBox)



    def generateMissions(self):
        print('generate missions')
    
    def listMissions(self):
        print('list')

    def changeColor(self, b):
        print("change color")



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = bkWindow()
    win.show()

    sys.exit(app.exec())