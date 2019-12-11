# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowEmployeeSignUp.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *
from Employee import *

class Ui_Form_EmployeeSignUp(object):
    def __init__(self):
        self.CurrentWindow = None
    def setupUi(self, CurrentWindow):
        self.CurrentWindow=CurrentWindow
        CurrentWindow.setObjectName("Currentwindow")
        CurrentWindow.resize(650, 550)
        self.title = QtWidgets.QLabel(CurrentWindow)
        self.title.setGeometry(QtCore.QRect(20, 15, 200, 41))
        self.title.setObjectName("title")
        self.comboBox = QtWidgets.QComboBox(CurrentWindow)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 171, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.type = QtWidgets.QLabel(CurrentWindow)
        self.type.setGeometry(QtCore.QRect(20, 56, 191, 31))
        self.type.setObjectName("type")
        self.First = QtWidgets.QLabel(CurrentWindow)
        self.First.setGeometry(QtCore.QRect(40, 150, 120, 31))
        self.First.setObjectName("First")
        self.FirstEdit = QtWidgets.QLineEdit(CurrentWindow)
        self.FirstEdit.setGeometry(QtCore.QRect(200, 160, 171, 30))
        self.FirstEdit.setObjectName("FirstEdit")
        self.UserEdit = QtWidgets.QLineEdit(CurrentWindow)
        self.UserEdit.setGeometry(QtCore.QRect(200, 210, 171, 30))
        self.UserEdit.setObjectName("UserEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(CurrentWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 270, 171, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.User = QtWidgets.QLabel(CurrentWindow)
        self.User.setGeometry(QtCore.QRect(40, 210, 120, 30))
        self.User.setObjectName("User")
        self.PassWord = QtWidgets.QLabel(CurrentWindow)
        self.PassWord.setGeometry(QtCore.QRect(40, 270, 120, 30))
        self.PassWord.setObjectName("PassWord")
        self.SignupB = QtWidgets.QPushButton(CurrentWindow)
        self.SignupB.setGeometry(QtCore.QRect(180, 350, 90, 30))
        self.SignupB.setObjectName("SignupB")

        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)
        self.SignupB.clicked.connect(self.EmpSignup)



    def EmpSignup(self):
        try:
            temp1 = self.FirstEdit.text()
            temp2 = self.UserEdit.text()
            temp3 = self.lineEdit_3.text()
            type=str(self.comboBox.currentText())
            if type[0]=='D':
                Deli=Delivery(temp1,temp2,temp3,'t')
                DeliveryPeople.append(Deli)
            elif type[0] == 'S':
                Sa=Sales(temp1,temp2,temp3)
                Sales.append(Sa)
            elif type[0] == 'C':
                Co = Cooks(temp1, temp2, temp3)
                Cooks.append(Co)

            self.CurrentWindow.hide()

        except Exception as e:
            import traceback
            traceback.print_exc()




    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Employee SignUP</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "Delivery People"))
        self.comboBox.setItemText(1, _translate("Form", "Sales People"))
        self.comboBox.setItemText(2, _translate("Form", "Cooks"))
        self.type.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Signup Type:</span></p></body></html>"))
        self.First.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">First Name:</span></p></body></html>"))
        self.User.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">User Nmae:</span></p></body></html>"))
        self.PassWord.setText(_translate("Form", "<B>Pass Word:"))
        self.SignupB.setText(_translate("Form", "Sign Up"))

