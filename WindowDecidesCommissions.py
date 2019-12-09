# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowDecidesCommissions.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *
from Employee import *

class Ui_Form_Commissions(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(805, 717)
        self.exitbutton = QtWidgets.QPushButton(Form)
        self.exitbutton.setGeometry(QtCore.QRect(610, 570, 71, 21))
        self.exitbutton.setObjectName("exitbutton")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(30, 20, 251, 61))
        self.Title.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(11, 27, 255);")
        self.Title.setObjectName("Title")
        self.EnterCom = QtWidgets.QLineEdit(Form)
        self.EnterCom.setGeometry(QtCore.QRect(470, 200, 113, 20))
        self.EnterCom.setObjectName("EnterCom")
        self.DollarSign = QtWidgets.QLabel(Form)
        self.DollarSign.setGeometry(QtCore.QRect(440, 190, 20, 41))
        self.DollarSign.setObjectName("DollarSign")
        self.ShowSaleP = QtWidgets.QLabel(Form)
        self.ShowSaleP.setGeometry(QtCore.QRect(470, 149, 261, 31))
        self.ShowSaleP.setObjectName("ShowSaleP")
        self.ShowCom = QtWidgets.QLabel(Form)
        self.ShowCom.setGeometry(QtCore.QRect(470, 290, 261, 31))
        self.ShowCom.setObjectName("ShowCom")
        self.Choose = QtWidgets.QLabel(Form)
        self.Choose.setGeometry(QtCore.QRect(30, 99, 191, 31))
        self.Choose.setObjectName("Choose")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 140, 291, 291))
        self.listWidget.setObjectName("listWidget")
        self.SelectB = QtWidgets.QPushButton(Form)
        self.SelectB.setGeometry(QtCore.QRect(320, 270, 56, 27))
        self.SelectB.setObjectName("SelectB")
        self.ConfirmB = QtWidgets.QPushButton(Form)
        self.ConfirmB.setGeometry(QtCore.QRect(535, 237,69, 27))
        self.ConfirmB.setObjectName("ConfirmB")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.exitbutton.clicked.connect(lambda: self.closescr(Form))
        self.SelectB.clicked.connect(self.ChooseSP)
        self.ConfirmB.clicked.connect(self.DecidesCom)

        for i in range(len(Sales)):
            self.listWidget.addItem(Sales[i].getFirst() +" "+ Sales[i].getUser())

    def ChooseSP(self):
        person = self.listWidget.selectedItems()
        if not person: return
        for i in person:
            self.ShowSaleP.setText('Please enter ' + i.text() + ' commissions')



    def closescr(self, Form):
        Form.hide()

    def DecidesCom(self):
        Items = self.listWidget.selectedItems()
        if not Items: return
        for item in Items:
            Q=str(item.text())
            name1 = Q
            for i in range(len(Sales)):
                if name1 == str(Sales[i].getFirst()+" "+Sales[i].getUser()):
                    ep = Sales[i]
                    Com = self.EnterCom.text()
                    ep.Commissions = int(Com)
                    self.ShowCom.setText(name1+" Commissions $:" + self.EnterCom.text())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exitbutton.setText(_translate("Form", "Exit"))
        self.Title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">decides commissions:</span></p></body></html>"))
        self.DollarSign.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">$</span></p></body></html>"))
        self.ShowSaleP.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.ShowCom.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.Choose.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Choose a sales person:</span></p></body></html>"))
        self.SelectB.setText(_translate("Form", "Select"))
        self.ConfirmB.setText(_translate("Form", "Confirm"))

