# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUpListWIndow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Main import *
from WindowSignUp import *
from User import *


class Ui_Form_SignUplist(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(867, 558)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 31))
        self.label.setObjectName("label")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(750, 510, 61, 31))
        self.exitButton.setObjectName("exitButton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 130, 281, 351))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.AgreeButton = QtWidgets.QPushButton(Form)
        self.AgreeButton.setGeometry(QtCore.QRect(310, 230, 56, 21))
        self.AgreeButton.setObjectName("AgreeButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(454, 199, 381, 71))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 261, 61))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.exitButton.clicked.connect(lambda: self.closescr(Form))
        self.AgreeButton.clicked.connect(self.AgreeSignup)

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(Signup))
        for i in range(len(Signup)):
            for j in range(4):
                if j==0:
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(Signup[i].getEmail())))
                elif j==1:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(Signup[i].getFirst())))
                elif j==2:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(Signup[i].getLast())))
                elif j==3:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(Signup[i].getUser())))


    def closescr(self, Form):
        Form.hide()

    def AgreeSignup(self):
        try:
            cellr=self.tableWidget.currentRow()
            cellc=self.tableWidget.currentColumn()
            Em=self.tableWidget.currentItem().text()
            for i in Signup:
                if i.getEmail() == Em:
                    print(len(Members))
                    t1=i.getFirst()
                    t2=i.getLast()
                    t3=i.getUser()
                    t4=i.getPass()
                    t5=i.getEmail()
                    t6=i.getAddress()
                    Members.append(Member(t1,t2,t3,t4,t5,t6))
                    print(len(Members))
        except Exception as e:
            import traceback
            traceback.print_exc()

       # ''' for i in range(len(Signup)):
       #      if Em == Signup[i].getEmail():
       #          t1=Signup[i].getFirt()
       #          t2=Signup[i].getLast()
       #          t3=Signup[i].getUser()
       #          t4=Signup[i].getPass()
       #          t5=Signup[i].getEmail()
       #          t6=Signup[i].getAddress()
       #          addMember(t1,t2,t3,t4,t5,t6)
       #  print(Em)'''



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SignUp Information</span></p></body></html>"))
        self.exitButton.setText(_translate("Form", "Exit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Email"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "User Name"))
        self.AgreeButton.setText(_translate("Form", "Agree"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Select one, push Agree to agree</span></p><p><span style=\" font-weight:600;\">user to be Member:</span></p></body></html>"))

