# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DecidesCommissions.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Commissions(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.exitbutton = QtWidgets.QPushButton(Form)
        self.exitbutton.setGeometry(QtCore.QRect(420, 380, 61, 21))
        self.exitbutton.setObjectName("exitbutton")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(30, 20, 250, 41))
        self.Title.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(11, 27, 255);")
        self.Title.setObjectName("Title")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 160, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SalePerson1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SalePerson1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.SalePerson1.setObjectName("SalePerson1")
        self.verticalLayout.addWidget(self.SalePerson1)
        self.SalePerson2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SalePerson2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.SalePerson2.setObjectName("SalePerson2")
        self.verticalLayout.addWidget(self.SalePerson2)
        self.EnterCom = QtWidgets.QLineEdit(Form)
        self.EnterCom.setGeometry(QtCore.QRect(310, 190, 113, 20))
        self.EnterCom.setObjectName("EnterCom")
        self.DollarSign = QtWidgets.QLabel(Form)
        self.DollarSign.setGeometry(QtCore.QRect(285, 180, 20, 41))
        self.DollarSign.setObjectName("DollarSign")
        self.ShowSaleP = QtWidgets.QLabel(Form)
        self.ShowSaleP.setGeometry(QtCore.QRect(284, 160, 300, 20))
        self.ShowSaleP.setObjectName("ShowSaleP")
        self.ShowCom = QtWidgets.QLabel(Form)
        self.ShowCom.setGeometry(QtCore.QRect(260, 230, 280, 61))
        self.ShowCom.setObjectName("ShowCom")
        self.Choose = QtWidgets.QLabel(Form)
        self.Choose.setGeometry(QtCore.QRect(30, 110, 250, 30))
        self.Choose.setObjectName("Choose")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.EnterCom.returnPressed.connect(self.ShowCommissions)
        self.exitbutton.clicked.connect(lambda: self.closescr(Form))
        self.SalePerson1.clicked.connect(self.ChooseSP1)
        self.SalePerson2.clicked.connect(self.ChooseSP2)

    def ChooseSP1(self):
        self.ShowSaleP.setText("Please enter Sale Person 1 commission ")


    def ChooseSP2(self):
        self.ShowSaleP.setText("Please enter Sale Person 2 commission ")



    def closescr(self, Form):
        Form.hide()

    def ShowCommissions(self):
        self.ShowCom.setText("The total commissions is $"+self.EnterCom.text())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exitbutton.setText(_translate("Form", "Exit"))
        self.Title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">decides commissions:</span></p></body></html>"))
        self.SalePerson1.setText(_translate("Form", "Sale Person 1"))
        self.SalePerson2.setText(_translate("Form", "Sale Person 2"))
        self.DollarSign.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">$</span></p></body></html>"))
        self.ShowSaleP.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.ShowCom.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.Choose.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Choose a sales person:</span></p></body></html>"))
