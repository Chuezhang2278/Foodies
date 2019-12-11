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
        self.listWidget.setGeometry(QtCore.QRect(25, 61, 431, 181))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 260, 131, 21))
        self.pushButton.setObjectName("pushButton")
        self.ExitButton = QtWidgets.QPushButton(Form)
        self.ExitButton.setGeometry(QtCore.QRect(400, 380, 56, 27))
        self.ExitButton.setObjectName("ExitButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 310, 271, 64))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 330, 61, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 380, 61, 21))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.ExitButton.clicked.connect(lambda: self.closescr(Form))
        self.pushButton.clicked.connect(self.DeleteComplain)
        self.pushButton_2.clicked.connect(self.replySend)

        for i in range(len(Complaint)):
            self.listWidget.addItem(Complaint[i])

    def DeleteComplain(self):
        try:
            Items = self.listWidget.selectedItems()
            if not Items: return
            for i in Items:
                Q = i.text()
                for j in range(0,len(Complaint)):
                    if Q == Complaint[j]:
                        Complaint.pop(j)
                        self.listWidget.takeItem(self.listWidget.row(i))
        except Exception as e:
            import traceback
            traceback.print_exc()
    def closescr(self, Form):
        Form.hide()

    def replySend(self):
        comp = self.textEdit.toPlainText()
        Complaint.append(str(comp))
        Complaint.append("Management： " + str(comp))
        self.listWidget.addItem("Management： " + str(comp))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Complaint Management</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Delete Complaint"))
        self.ExitButton.setText(_translate("Form", "Exit"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">reply:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Send"))

