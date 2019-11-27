# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manager.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from WindowDecidesCommissions import Ui_Form_Commissions
from WindowEmployeeSalary import Ui_Form_Pay

class  ManagerWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 493)
        #MainWindow.setStyleSheet()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setStyleSheet()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(92, 120, 291, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DecidesCommissionsB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DecidesCommissionsB.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 0);")
        self.DecidesCommissionsB.setObjectName("DecidesCommissionsB")
        self.verticalLayout.addWidget(self.DecidesCommissionsB)
        self.DecidesPayB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DecidesPayB.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.DecidesPayB.setObjectName("DecidesPayB")
        self.verticalLayout.addWidget(self.DecidesPayB)
        self.HandlesComplaintsB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.HandlesComplaintsB.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.HandlesComplaintsB.setObjectName("HandlesComplaintsB")
        self.verticalLayout.addWidget(self.HandlesComplaintsB)
        self.ManagementStaffB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ManagementStaffB.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.ManagementStaffB.setObjectName("ManagementStaffB")
        self.verticalLayout.addWidget(self.ManagementStaffB)
        self.CustomerInforB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CustomerInforB.setObjectName("CustomerInforB")
        self.verticalLayout.addWidget(self.CustomerInforB)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(455, 350, 91, 31))
        self.exitbutton.setObjectName("exitbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 18))
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
        self.ManagementStaffB.setText(_translate("MainWindow", "Management stuff"))
        self.CustomerInforB.setText(_translate("MainWindow", "Customer Information Mangement"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QMainWindow()
    ui = ManagerWindow()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())
