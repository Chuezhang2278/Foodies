# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CusInforManagement.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *
from SignUpListWIndow import Ui_Form_SignUplist
from WindowCusinfor import Ui_Form_cusmberInfor
from WindowComplain import Ui_Form_Complain
from WindowOrderHistory import Ui_Form_OrderHistory

class Ui_Form_CusInfor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 499)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(24, 10, 291, 41))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(69, 79, 301, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SignButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SignButton.setObjectName("SignButton")
        self.verticalLayout.addWidget(self.SignButton)
        self.CusinforButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CusinforButton.setObjectName("CusinforButton")
        self.verticalLayout.addWidget(self.CusinforButton)
        self.orderinforButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.orderinforButton.setObjectName("orderinforButton")
        self.verticalLayout.addWidget(self.orderinforButton)
        #self.CusinforButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #self.CusinforButton_2.setObjectName("CusinforButton_2")
        #self.verticalLayout.addWidget(self.CusinforButton_2)
        self.exitbutton = QtWidgets.QPushButton(Form)
        self.exitbutton.setGeometry(QtCore.QRect(480, 460, 61, 21))
        self.exitbutton.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.exitbutton.clicked.connect(lambda: self.closescr(Form))
        self.SignButton.clicked.connect(lambda: self.SingupInformation())
        self.CusinforButton.clicked.connect(lambda: self.CusInformation())
        self.orderinforButton.clicked.connect(lambda: self.orderHistorystr())

    def closescr(self, Form):
        Form.hide()

    def SingupInformation(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form_SignUplist()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def CusInformation(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form_cusmberInfor()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def orderHistorystr(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form_OrderHistory()
        self.ui.setupUi(self.Form)
        self.Form.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Customer Information Management</span></p></body></html>"))
        self.SignButton.setText(_translate("Form", "SignUp Information"))
        self.CusinforButton.setText(_translate("Form", "Customer Information"))
        self.orderinforButton.setText(_translate("Form", "Order Information"))
        #self.CusinforButton_2.setText(_translate("Form", "Customers Management"))
        self.exitbutton.setText(_translate("Form", "Exit"))

