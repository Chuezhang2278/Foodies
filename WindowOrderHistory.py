# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowOrderHistory.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *

class Ui_Form_OrderHistory(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 521)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 19, 101, 31))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(25, 51, 521, 411))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(510, 490, 56, 17))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(lambda:self.closescr(Form))

        for i in range(len(OrderHistory)):
            ordernmber = str("Order: " + i +"\tCustomr: " + OrderHistory[i].CurrentUser())

            self.listWidget.addItem()

    def closescr(self, Form):
        Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Order History </span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Exit"))

