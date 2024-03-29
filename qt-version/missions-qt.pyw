# Original version by Trynan and Wedarobi
# Maintained by Trynan
# BK Missions idea by CrozB
# Mission generation logic and missions by CrozB
# 8/11/2020 - 1/6/2022


from PySide6 import QtWidgets, QtGui, QtCore
import sys
import random

import mainWindow
import listWindow
import generation

class missionsWin(mainWindow.bkWindow):
    def __init__(self):
        super().__init__()
        self.listWin = None
        self.seedValue = "0"


    ###
    # helper functions
    def getSeed(self):
        """ returns seed (either custom or new random one) """
        if self.useSeedCheck.isChecked():  # use custom seed
            self.seedValue = self.customSeedBox.text()
            self.currentSeedBox.clear()
            self.currentSeedBox.setText(self.seedValue)
            return self.seedValue
        random.seed()  # randomize current seed based on system time
        rn = str(random.randrange(100000, 1000000))
        self.seedValue = rn
        self.currentSeedBox.clear()
        self.currentSeedBox.setText(rn)
        self.customSeedBox.clear()
        self.customSeedBox.setText(rn)
        return rn


    def getMissionsLists(self):
        longMain = generation.getLongMain()
        longSide = generation.getLongSide()
        shortMain = generation.getShortMain()
        levels = generation.getLevels()
        if not self.shortCheck.isChecked():
            missions = [
                [longMain],  # main objective
                [longSide],  # side quest
                [  # early game
                    levels['mm'],
                    levels['ttc'],
                    levels['cc'],
                    levels['fp']
                ],
                [  # mid game
                    levels['mmm'],
                    levels['gv'],
                    levels['rbb']
                ],
                [  # late game
                    levels['bgs'],
                    levels['ccw']
                ]
            ]
        else:
            missions = [
                [shortMain],  # main objective
                [  # early game
                    levels['mm'],
                    levels['ttc'],
                    levels['cc'],
                    levels['fp'],
                    levels['mmm']
                ],
                [  # late game
                    levels['gv'],
                    levels['rbb'],
                    levels['bgs'],
                    levels['ccw']
                ]
            ]
        return missions


    ###
    # button-activated functions
    def generateMissions(self):
        # return current button backgrounds to default
        for b in self.buttons:
            b.setStyleSheet("")
        # set seed
        random.seed(self.getSeed())
        # get lists of missions (done every time for random results)
        missions = self.getMissionsLists()
        if self.shortCheck.isChecked():
            self.b4.setText("-----")
            self.b5.setText("-----")
            self.b4.setEnabled(False)
            self.b5.setEnabled(False)
        else:
            self.b4.setEnabled(True)
            self.b5.setEnabled(True)
        goals = generation.generateGoals(missions, self.shortCheck.isChecked(), not self.randCheck.isChecked())
        for m,b in zip(goals, self.buttons):
            if self.codesCheck.isChecked():
                b.setText(m.name + ' -- ' + ', '.join(m.codes))
            else:
                b.setText(m.name)


    def listMissions(self):
        if self.listWin != None:
            self.listWin.close()
        self.listWin = listWindow.listWindow()
        self.listWin.show()
        random.seed(self.getSeed())
        missions = self.getMissionsLists()
        longLabels = [
            "1. Main Objective",
            "2. Side Quest",
            "3. Early Game",
            "4. Mid Game",
            "5. Late Game"
        ]
        shortLabels = [
            "1. Main Objective",
            "2. Early Game",
            "3. Late Game"
        ]
        labelList = [longLabels, shortLabels]
        if self.shortCheck.isChecked():
            self.listWin.text.insertPlainText("LIST OF SHORT MISSIONS:\n\n")
        else:
            self.listWin.text.insertPlainText("LIST OF LONG MISSIONS:\n\n")
        for labelNum, category in enumerate(missions):
            self.listWin.text.insertPlainText(labelList[int(self.shortCheck.isChecked())][labelNum] + '\n')
            for lst in category:  # category is a list of lists
                for goal in lst:  # go through each goal in the sub-lists
                    if not self.randCheck.isChecked():
                        if goal.rand == 1:
                            continue  # don't use random goals
                    else:
                        if goal.rand == 2:
                            continue  # don't use nonrandom variants of random goals
                    self.listWin.text.insertPlainText('- ' + goal.name)
                    if self.codesCheck.isChecked():
                        self.listWin.text.insertPlainText(' -- ' + ', '.join(goal.codes))
                    self.listWin.text.insertPlainText('\n')
                # end of category
                self.listWin.text.insertPlainText('\n')


    def changeColor(self, b):
        style = b.styleSheet()
        style = style.replace(' ','')
        style = style.split(':')
        if style[0]:
            if style[1] == 'green':
                b.setStyleSheet("background-color : red")
            else:
                b.setStyleSheet("")  # reset to default
        else:
            b.setStyleSheet("background-color : green")



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = missionsWin()
    win.show()

    sys.exit(app.exec())