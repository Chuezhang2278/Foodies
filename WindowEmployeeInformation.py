# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowEmployeeInformation.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  Main import *
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_Form_EmployeeInformation(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 457)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 9, 161, 41))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(25, 51, 561, 321))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(14)
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

        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(490, 416, 61, 21))
        self.exitButton.setObjectName("pushButton")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.exitButton.clicked.connect(lambda:self.closescr(Form))
        try:
            for i in range(len(Cooks)):
                for j in range(4):
                    if j == 0:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str('Cook')))
                    elif j == 1:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(Cooks[i].getFirst()))
                    elif j == 2:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(Cooks[i].getUser()))
                    elif j == 3:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(Cooks[i].getSalary())))

            for k in range(len(Cooks), len(Cooks) + len(DeliveryPeople)):
                for l in range(5):
                    if l == 0:
                        self.tableWidget.setItem(k, l, QTableWidgetItem(str('DeliveryPeople')))
                    elif l == 1:
                        self.tableWidget.setItem(k, l, QTableWidgetItem(str(DeliveryPeople[k - len(Cooks)].getFirst())))
                    elif l == 2:
                        self.tableWidget.setItem(k, l, QTableWidgetItem(str(DeliveryPeople[k - len(Cooks)].getUser())))
                    elif l == 3:
                        self.tableWidget.setItem(k, l, QTableWidgetItem(str(DeliveryPeople[k - len(Cooks)].getSalary())))
                    elif l == 4:
                        self.tableWidget.setItem(k, l, QTableWidgetItem(str(DeliveryPeople[k - len(Cooks)].getWarning())))

            lencd = len(Cooks) + len(DeliveryPeople)

            for m in range(lencd, lencd + len(Sales)):
                for n in range(6):
                    if n == 0:
                        self.tableWidget.setItem(m, n, QTableWidgetItem(str('Sales')))
                    elif n == 1:
                        self.tableWidget.setItem(m, n, QTableWidgetItem(str(Sales[m - lencd].getFirst())))
                    elif n == 2:
                        self.tableWidget.setItem(m, n, QTableWidgetItem(str(Sales[m - lencd].getUser())))
                    elif n == 3:
                        self.tableWidget.setItem(m, n, QTableWidgetItem(str(Sales[m - lencd].getSalary())))
                    elif n == 4:
                        self.tableWidget.setItem(m, n, QTableWidgetItem(str(Sales[m - lencd].getWarning())))
                    elif n == 5:
                        self.tableWidget.setItem(m, n, QTableWidgetItem(str(Sales[m - lencd].getCommissions())))
        except Exception as e:
            import traceback
            traceback.print_exc()


    def closescr(self, Form):
        Form.hide()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Employee Information</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Last Name"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Warning"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Commissions"))
        self.exitButton.setText(_translate("Form", "Exit"))

