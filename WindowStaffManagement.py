# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowStaffManagement.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *

class Ui_Form_StaffManagement(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1064, 623)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(24, 19, 131, 31))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 351, 351))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 171, 31))
        self.label_2.setObjectName("label_2")
        self.FireButton = QtWidgets.QPushButton(Form)
        self.FireButton.setGeometry(QtCore.QRect(410, 230, 61, 21))
        self.FireButton.setObjectName("FireButton")
        self.exitbutton = QtWidgets.QPushButton(Form)
        self.exitbutton.setGeometry(QtCore.QRect(655, 466, 71, 31))
        self.exitbutton.setObjectName("exitbutton")
        self.ShowFire = QtWidgets.QLabel(Form)
        self.ShowFire.setGeometry(QtCore.QRect(520, 180, 571, 231))
        self.ShowFire.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.exitbutton.clicked.connect(lambda: self.closescr(Form))
        self.FireButton.clicked.connect(self.Fire)

        for i in range(len(DeliveryPeople)):
            self.listWidget.addItem(
                'Delivery People :' + DeliveryPeople[i].getFirst() + " " + DeliveryPeople[i].getUser())
        for i in range(len(Sales)):
            self.listWidget.addItem('Sale People: ' + Sales[i].getFirst() + " " + Sales[i].getUser())
        for i in range(len(Cooks)):
            self.listWidget.addItem('Cooks: ' + Cooks[i].getFirst() + " " + Cooks[i].getUser())

    def closescr(self, Form):
        Form.hide()

    def Fire(self):
        Items = self.listWidget.selectedItems()
        if not Items: return
        for item in Items:
            Q = str(item.text())
            if Q[0] == 'D':
                name1 = Q[17:]
                if len(DeliveryPeople) <= 1:
                    self.ShowFire.setText("You can not fire any one of Deliver people because at least 1 Delivery guy!")
                    return
                for i in range(len(DeliveryPeople)):
                    if name1 == str(DeliveryPeople[i].getFirst() + " " + DeliveryPeople[i].getUser()):
                        DeliveryPeople.pop(i)
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.ShowFire.setText(name1+" was fired successful!")
            elif Q[0] == 'S':
                name1 = Q[13:]
                if len(Sales) <= 2:
                    self.ShowFire.setText("You can not fire any one of Sales people because at least 2 Sales people.")
                    return
                for i in range(len(Sales)):
                    if name1 == str(Sales[i].getFirst() + " " + Sales[i].getUser()):
                        Sales.pop(i)
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.ShowFire.setText(name1 + name1+" was fired successful!")
            elif Q[0] == 'C':
                name1 = Q[7:]
                if len(Cooks) <= 2:
                    self.ShowFire.setText("You can not fire any one of Cooks because at least 2 Cooks.")
                    return
                for i in range(len(Cooks)):
                    if name1 == str(Cooks[i].getFirst() + " " + Cooks[i].getUser()):
                        Cooks.pop(i)
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.ShowFire.setText(name1 + name1+" was fired successful!")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Staff Management</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Staff List (Please select one):</span></p></body></html>"))
        #self.ShowFire.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.FireButton.setText(_translate("Form", "Fire"))
        self.exitbutton.setText(_translate("Form", "Exit"))

