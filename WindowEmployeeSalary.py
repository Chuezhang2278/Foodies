# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowEmployeeSalary.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *

class Ui_Form_Pay(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(928, 905)
        self.ExitButton = QtWidgets.QPushButton(Form)
        self.ExitButton.setGeometry(QtCore.QRect(835, 836, 61, 31))
        self.ExitButton.setObjectName("ExitButton")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(20, 10, 211, 41))
        self.Title.setObjectName("Title")
        self.Choose = QtWidgets.QLabel(Form)
        self.Choose.setGeometry(QtCore.QRect(50, 60, 311, 41))
        self.Choose.setObjectName("Choose")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(650, 260, 121, 19))
        self.lineEdit.setObjectName("lineEdit")
        self.DS = QtWidgets.QLabel(Form)
        self.DS.setGeometry(QtCore.QRect(620, 260, 20, 20))
        self.DS.setObjectName("DS")
        self.ShowStuff = QtWidgets.QLabel(Form)
        self.ShowStuff.setGeometry(QtCore.QRect(650, 220, 231, 31))
        self.ShowStuff.setText("")
        self.ShowStuff.setObjectName("ShowStuff")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(630, 340, 501, 51))
        self.label.setText("")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(45, 111, 321, 351))
        self.listWidget.setObjectName("listWidget")
        self.SelectB = QtWidgets.QPushButton(Form)
        self.SelectB.setGeometry(QtCore.QRect(385, 256, 71, 21))
        self.SelectB.setObjectName("pushButton")
        self.ComfSalary = QtWidgets.QPushButton(Form)
        self.ComfSalary.setGeometry(QtCore.QRect(720, 300, 81, 25))
        self.ComfSalary.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.ExitButton.clicked.connect(lambda: self.closescr(Form))
        self.ComfSalary.clicked.connect(self.DecidesSalary)
        self.SelectB.clicked.connect(self.SelectPerson)
        for i in range(len(DeliveryPeople)):
            self.listWidget.addItem('Delivery People: ' + DeliveryPeople[i].getFirst())
        for i in range(len(Sales)):
            self.listWidget.addItem('Sale People: ' + Sales[i].getFirst())
        for i in range(len(Cooks)):
            self.listWidget.addItem('Cooks: ' + Cooks[i].getFirst())

    def SelectPerson(self):
        person = self.listWidget.selectedItems()
        if not person: return
        for i in person:
            self.ShowStuff.setText('Please enter ' + i.text() + ' salary')

    def closescr(self, Form):
        Form.hide()

    def DecidesSalary(self):
        Items = self.listWidget.selectedItems()
        if not Items: return
        for item in Items:
            Q=str(item.text())
            if Q[0] == 'D':
                name1 = Q[17:]
                for i in range(len(DeliveryPeople)):
                   if name1 == DeliveryPeople[i].getFirst():

                        Sa = int(self.lineEdit.text())
                        DeliveryPeople[i].salary = Sa
                        self.label.setText(name1+" Salary $:" + self.lineEdit.text())
            elif Q[0] == 'S':
                name1 = Q[13:]
                for i in range(len(Sales)):
                    if name1 == Sales[i].getFirst():

                        Sa = int(self.lineEdit.text())
                        Sales[i].salary = Sa
                        self.label.setText(name1+ " salary $ " + self.lineEdit.text())
            elif Q[0] == 'C':
                name1 = Q[7:]
                for i in range(len(Cooks)):
                    if name1 == Cooks[i].getFirst():

                        Sa = int(self.lineEdit.text())
                        Cooks[i].salary = Sa
                        self.label.setText(name1+ " salary $ "+ self.lineEdit.text())


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ExitButton.setText(_translate("Form", "Exit"))
        self.Title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0410f1;\">Employee salary</span></p></body></html>"))
        self.Choose.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Choose a staff:</span></p></body></html>"))
        self.DS.setText(_translate("Form", "    <B>  $"))
        self.SelectB.setText(_translate("Form", "Select"))
        self.ComfSalary.setText(_translate("Form", "Comfirm"))

