# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowComplaintManagement.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import *

class Ui_Form_ComplainManagement(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(468, 411)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 15, 171, 31))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(25, 61, 421, 231))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 320, 131, 21))
        self.pushButton.setObjectName("pushButton")
        self.ExitButton = QtWidgets.QPushButton(Form)
        self.ExitButton.setGeometry(QtCore.QRect(400, 380, 56, 17))
        self.ExitButton.setObjectName("ExitButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.ExitButton.clicked.connect(lambda: self.closescr(Form))
        self.pushButton.clicked.connect(self.DeleteComplain)

        for i in range(len(Complaint)):
            self.listWidget.addItem(Complaint[i])


    def DeleteComplain(self):
        Items = self.listWidget.selectedItems()
        if not Items: return
        for i in Items:
            Q=i.text()
            for j in range(len(Complaint)):
                if Q==Complaint[j]:
                    Complaint.pop(j)
                    self.listWidget.takeItem(self.listWidget.row(i))




    def closescr(self, Form):
        Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Complaint Management</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Delete Complaint"))
        self.ExitButton.setText(_translate("Form", "Exit"))

