# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkshopProgram.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.phraseLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.phraseLabel.setFont(font)
        self.phraseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.phraseLabel.setObjectName("phraseLabel")
        self.horizontalLayout.addWidget(self.phraseLabel)
        self.phraseInputField = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.phraseInputField.setFont(font)
        self.phraseInputField.setObjectName("phraseInputField")
        self.horizontalLayout.addWidget(self.phraseInputField)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioWsName = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioWsName.setFont(font)
        self.radioWsName.setAutoExclusive(False)
        self.radioWsName.setObjectName("radioWsName")
        self.verticalLayout_3.addWidget(self.radioWsName)
        self.radioWsID = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioWsID.setFont(font)
        self.radioWsID.setAutoExclusive(False)
        self.radioWsID.setObjectName("radioWsID")
        self.verticalLayout_3.addWidget(self.radioWsID)
        self.radioWsURLs = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioWsURLs.setFont(font)
        self.radioWsURLs.setAutoExclusive(False)
        self.radioWsURLs.setObjectName("radioWsURLs")
        self.verticalLayout_3.addWidget(self.radioWsURLs)
        self.radioPartNumbers = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioPartNumbers.setFont(font)
        self.radioPartNumbers.setAutoExclusive(False)
        self.radioPartNumbers.setObjectName("radioPartNumbers")
        self.verticalLayout_3.addWidget(self.radioPartNumbers)
        self.radioWsStartDate = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioWsStartDate.setFont(font)
        self.radioWsStartDate.setAutoExclusive(False)
        self.radioWsStartDate.setObjectName("radioWsStartDate")
        self.verticalLayout_3.addWidget(self.radioWsStartDate)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.participantLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.participantLabel.setFont(font)
        self.participantLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.participantLabel.setObjectName("participantLabel")
        self.verticalLayout_4.addWidget(self.participantLabel)
        self.radioNames = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioNames.setFont(font)
        self.radioNames.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioNames.setAutoExclusive(False)
        self.radioNames.setObjectName("radioNames")
        self.verticalLayout_4.addWidget(self.radioNames)
        self.radioEmails = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioEmails.setFont(font)
        self.radioEmails.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioEmails.setAutoExclusive(False)
        self.radioEmails.setObjectName("radioEmails")
        self.verticalLayout_4.addWidget(self.radioEmails)
        self.radioSchool = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioSchool.setFont(font)
        self.radioSchool.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioSchool.setAutoExclusive(False)
        self.radioSchool.setObjectName("radioSchool")
        self.verticalLayout_4.addWidget(self.radioSchool)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.buttonGetWorkshops = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.buttonGetWorkshops.setFont(font)
        self.buttonGetWorkshops.setObjectName("buttonGetWorkshops")
        self.verticalLayout_5.addWidget(self.buttonGetWorkshops)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 831, 183))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textOutputField = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textOutputField.setObjectName("textOutputField")
        self.verticalLayout_2.addWidget(self.textOutputField)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 21))
        self.menubar.setObjectName("menubar")
        self.menuFont = QtWidgets.QMenu(self.menubar)
        self.menuFont.setObjectName("menuFont")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIncrease_CTRL = QtWidgets.QAction(MainWindow)
        self.actionIncrease_CTRL.setObjectName("actionIncrease_CTRL")
        self.actionDecrease_CTRL = QtWidgets.QAction(MainWindow)
        self.actionDecrease_CTRL.setObjectName("actionDecrease_CTRL")
        self.actionUpdate_Credentials = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Credentials.setObjectName("actionUpdate_Credentials")
        self.menuFont.addAction(self.actionIncrease_CTRL)
        self.menuFont.addAction(self.actionDecrease_CTRL)
        self.menuLogin.addAction(self.actionUpdate_Credentials)
        self.menubar.addAction(self.menuFont.menuAction())
        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workshop App"))
        self.phraseLabel.setText(_translate("MainWindow", "Search Phrase:"))
        self.radioWsName.setText(_translate("MainWindow", "Workshop Name"))
        self.radioWsID.setText(_translate("MainWindow", "Workshop ID"))
        self.radioWsURLs.setText(_translate("MainWindow", "Workshop URLs"))
        self.radioPartNumbers.setText(_translate("MainWindow", "Participant Numbers"))
        self.radioWsStartDate.setText(_translate("MainWindow", "Start Date"))
        self.participantLabel.setText(_translate("MainWindow", "Participant Info:"))
        self.radioNames.setText(_translate("MainWindow", "Names"))
        self.radioEmails.setText(_translate("MainWindow", "Emails"))
        self.radioSchool.setText(_translate("MainWindow", "School"))
        self.buttonGetWorkshops.setText(_translate("MainWindow", "Get Workshops"))
        self.menuFont.setTitle(_translate("MainWindow", "Font"))
        self.menuLogin.setTitle(_translate("MainWindow", "Login"))
        self.actionIncrease_CTRL.setText(_translate("MainWindow", "Increase CTRL + ="))
        self.actionIncrease_CTRL.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionDecrease_CTRL.setText(_translate("MainWindow", "Decrease CTRL + -"))
        self.actionDecrease_CTRL.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionUpdate_Credentials.setText(_translate("MainWindow", "Update Credentials"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
