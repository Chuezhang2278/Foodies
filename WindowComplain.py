# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowComplain.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Main import  *

class Ui_Form_Complain(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 415)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 310, 71, 31))
        self.label.setObjectName("label")
        self.SendButton = QtWidgets.QPushButton(Form)
        self.SendButton.setGeometry(QtCore.QRect(210, 370, 61, 21))
        self.SendButton.setObjectName("SendButton")
        self.exitB = QtWidgets.QPushButton(Form)
        self.exitB.setGeometry(QtCore.QRect(400, 390, 56, 17))
        self.exitB.setObjectName("exitB")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 15, 111, 41))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(25, 61, 421, 201))
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(83, 293, 361, 61))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.exitB.clicked.connect(lambda: self.closescr(Form))
        self.SendButton.clicked.connect(self.ComplainSend)

    def closescr(self, Form):
        Form.hide()

    def ComplainSend(self):
        comp = self.textEdit.toPlainText()
        Complaint.append(str(comp))
        self.listWidget.addItem("Complain" + str(len(Complaint)) + ": " + str(comp))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Complain：</span></p></body></html>"))
        self.SendButton.setText(_translate("Form", "Send"))
        self.exitB.setText(_translate("Form", "Exit"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Complain:</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QMainWindow()
    ui = Ui_Form_Complain()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())