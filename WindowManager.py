# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from DecidesCommissions import Ui_Form_Commissions
from EmployeeSalary import Ui_Form_Pay


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 568)
        MainWindow.setStyleSheet("background-image: url(C:/Users/alexl/Downloads/ab.jpg);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/newPrefix/mb.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 140, 153, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DecidesCommissionsB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DecidesCommissionsB.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 0);")
        self.DecidesCommissionsB.setObjectName("DecidesCommissions")
        self.verticalLayout.addWidget(self.DecidesCommissionsB)
        self.DecidesPayB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DecidesPayB.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.DecidesPayB.setObjectName("DecidesPay")
        self.verticalLayout.addWidget(self.DecidesPayB)
        self.HandlesComplaintsB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.HandlesComplaintsB.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.HandlesComplaintsB.setObjectName("HandlesComplaints")
        self.verticalLayout.addWidget(self.HandlesComplaintsB)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(455, 350, 91, 31))
        self.exitbutton.setObjectName("exitbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.DecidesCommissionsB.clicked.connect(self.DecidesCommissionsscr)
        self.DecidesPayB.clicked.connect(self.DecidesPayscr)
        self.exitbutton.clicked.connect(lambda: self.closescr(MainWindow))

    def DecidesCommissionsscr(self):
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form_Commissions()
            self.ui.setupUi(self.Form)
            self.Form.show()

    def DecidesPayscr(self):
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form_Pay()
            self.ui.setupUi(self.Form)
            self.Form.show()

    def closescr(self, MainWindow):
            MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#1423f4;\">Manager</span></p></body></html>"))
        self.DecidesCommissionsB.setText(_translate("MainWindow", "Decides commissions of salespeople "))
        self.DecidesPayB.setText(_translate("MainWindow", "Decides pay for stuffs"))
        self.HandlesComplaintsB.setText(_translate("MainWindow", "Handles complaints"))
        self.pushButton.setText(_translate("MainWindow", "Management stuff"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))
