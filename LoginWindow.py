from SignUp import sign_window
from FoodMenu import Food_Window
from User import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogUser_Label = QtWidgets.QLabel(self.centralwidget)
        self.LogUser_Label.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.LogUser_Label.setObjectName("LogUser_Label")
        self.LogPass_Label = QtWidgets.QLabel(self.centralwidget)
        self.LogPass_Label.setGeometry(QtCore.QRect(40, 80, 61, 16))
        self.LogPass_Label.setObjectName("LogPass_Label")
        self.LogUser_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LogUser_lineEdit.setGeometry(QtCore.QRect(110, 40, 241, 22))
        self.LogUser_lineEdit.setObjectName("LogUser_lineEdit")
        self.LogPass_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LogPass_lineEdit.setGeometry(QtCore.QRect(110, 80, 241, 22))
        self.LogPass_lineEdit.setObjectName("LogPass_lineEdit")
        self.guestButton = QtWidgets.QPushButton(self.centralwidget)
        self.guestButton.setGeometry(QtCore.QRect(40, 120, 93, 28))
        self.guestButton.setObjectName("guestButton")
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(150, 120, 93, 28))
        self.signUpButton.setObjectName("signUpButton")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(260, 120, 93, 28))
        self.loginButton.setObjectName("loginButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signUpButton.clicked.connect(self.switch_sign)
        self.loginButton.clicked.connect(self.LoginVeri)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LogUser_Label.setText(_translate("MainWindow", "Username"))
        self.LogPass_Label.setText(_translate("MainWindow", "Password"))
        self.guestButton.setText(_translate("MainWindow", "Guest"))
        self.signUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.loginButton.setText(_translate("MainWindow", "Login"))

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

    def LoginVeri(self): 
        value1 = self.LogUser_lineEdit.text()
        value2 = self.LogPass_lineEdit.text()

        test = Customer.getsize()

        for i in range(test):
            if(value1 == Customer.Members[i].getUser() and value2 == Customer.Members[i].getPass()):
                    print(Customer.Members[i].getType(), "Member")
            elif(value1 == Customer.VIP[i].getUser() and value2 == Customer.VIP[i].getPass()):
                    print(Customer.VIP[i].getType(), "VIP")
            else:
                print("Guest")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
