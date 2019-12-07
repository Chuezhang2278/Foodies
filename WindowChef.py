# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chef.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from WindowMenuModification import Ui_WindowMenuModification


class Ui_WindowChef(object):
    def __init__(self):
        self.WindowChef = None;
        self.LoginWindow = None;

    def setupUi(self, WindowChef):
        WindowChef.setObjectName("WindowChef")
        WindowChef.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(WindowChef)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(0, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(654, 0, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.managesuppliesButton = QtWidgets.QPushButton(self.centralwidget)
        self.managesuppliesButton.setGeometry(QtCore.QRect(90, 280, 200, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.managesuppliesButton.setFont(font)
        self.managesuppliesButton.setObjectName("managesuppliesButton")
        self.managemenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.managemenuButton.setGeometry(QtCore.QRect(490, 280, 200, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.managemenuButton.setFont(font)
        self.managemenuButton.setObjectName("managemenuButton")
        WindowChef.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowChef)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        WindowChef.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowChef)
        self.statusbar.setObjectName("statusbar")
        WindowChef.setStatusBar(self.statusbar)

        self.retranslateUi(WindowChef)
        QtCore.QMetaObject.connectSlotsByName(WindowChef)

        # TODO: create a method to logout of account show sign in page
        self.logoutButton.clicked.connect(self.open_logoutConfirmation)
        # TODO: create a method to open the suppliesMenu.ui window
        # self.managesuppliesButton.clicked.connect(self.open_manageSupplies)
        # TODO: create a method to open the foodMenu.ui window
        self.managemenuButton.clicked.connect(self.open_manageMenu)

    def retranslateUi(self, WindowChef):
        _translate = QtCore.QCoreApplication.translate
        WindowChef.setWindowTitle(_translate("WindowChef", "MainWindow"))
        self.welcomeLabel.setText(_translate("WindowChef", "Welcome, chef"))
        self.logoutButton.setText(_translate("WindowChef", "Logout"))
        self.managesuppliesButton.setText(_translate("WindowChef", "Manage Restaurant Supplies"))
        self.managemenuButton.setText(_translate("WindowChef", "Manage Restaurant Food Menu"))

    def open_logoutConfirmation(self):
        msg = QMessageBox()
        msg.setWindowTitle("Logout")
        msg.setText("Are you sure you want to logout?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    def popup_button(self, i):
        if(i.text() == "&Yes"):
            print("Yes")
        else:
            print("No")

    #def open_manageSupplies(self):

    def open_manageMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMenuModification()
        self.ui.setupUi(self.window)
        WindowChef.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowChef = QtWidgets.QMainWindow()
    ui = Ui_WindowChef()
    ui.setupUi(WindowChef)
    WindowChef.show()
    sys.exit(app.exec_())
