# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_332.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SignUp_332 import sign_window
from FoodMenu_332 import Food_Window

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_Username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.horizontalLayout.addWidget(self.lineEdit_Username)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.horizontalLayout_2.addWidget(self.lineEdit_Password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Login_button = QtWidgets.QPushButton(self.groupBox)
        self.Login_button.setObjectName("Login_button")
        self.gridLayout.addWidget(self.Login_button, 0, 1, 1, 1)
        self.signup_button = QtWidgets.QPushButton(self.groupBox)
        self.signup_button.setObjectName("signup_button")
        self.gridLayout.addWidget(self.signup_button, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Login_button.clicked.connect(self.switch_menu) #self created event handle for login button
        self.signup_button.clicked.connect(self.switch_sign) #brings up signup page

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Sign In"))
        self.label.setText(_translate("MainWindow", "UserName"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.Login_button.setText(_translate("MainWindow", "Login"))
        self.signup_button.setText(_translate("MainWindow", "Sign Up"))

    def switch_sign(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = sign_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def switch_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Food_Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def labelUsername(self):
        value = self.lineEdit_Username.text()
        print(value)

    def LoginVeri(self):
        value1 = self.lineEdit_Username.text()
        value2 = self.lineEdit_Password.text()
        if(value1 == "Andy" and value2 == "Zhang"):
            self.switch_menu
        else:  
            print("Invalid")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
