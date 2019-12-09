# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowCusinfor.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Form_cusmberInfor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(523, 444)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 31))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(25, 61, 471, 291))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 400, 91, 21))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(lambda: self.closescr(Form))


        self.tableWidget.setColumnCount(5)

        for i in range(len(Members)):
            for j in range(5):
                if j == 0:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str('Member')))
                elif j == 1:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(Members[i].getFirst()))
                elif j == 2:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(Members[i].getLast())))
                elif j == 3:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(Members[i].getUser())))
                elif j==4:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(Members[i].getEmail())))



        for k in range(len(Members),len(Members)+len(VIPs)):
            for l in range(5):
                if l == 0:
                    self.tableWidget.setItem(k, l, QTableWidgetItem(str('VIP')))
                elif l == 1:
                    self.tableWidget.setItem(k, l, QTableWidgetItem(str(VIPs[k-len(Members)].getFirst())))
                elif l == 2:
                    self.tableWidget.setItem(k, l, QTableWidgetItem(str(VIPs[k-len(Members)].getLast())))
                elif l == 3:
                    self.tableWidget.setItem(k, l, QTableWidgetItem(str(VIPs[k-len(Members)].getUser())))
                elif l == 4:
                    self.tableWidget.setItem(k, l, QTableWidgetItem(str(VIPs[k-len(Members)].getEmail())))

    def closescr(self, Form):
        Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Customer Information</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "User Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Rating"))
        self.pushButton.setText(_translate("Form", "Exit"))

