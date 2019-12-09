from WindowSignUp import sign_window
from WindowFoodStackWidget import Food_Window
from WindowChef import Ui_WindowChef
from WindowManager import ManagerWindow
from WindowSalesperson import Sales_Window
from Main import *

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets

class LoginWindow(object):
    def setupUi(self, CurrentWindow):
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.setEnabled(True)
        CurrentWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
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
        CurrentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

        self.signUpButton.clicked.connect(self.switch_sign)
        self.loginButton.clicked.connect(self.LoginVeri)
        self.guestButton.clicked.connect(self.guestVeri)

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("CurrentWindow", "Login"))
        self.LogUser_Label.setText(_translate("CurrentWindow", "Username"))
        self.LogPass_Label.setText(_translate("CurrentWindow", "Password"))
        self.guestButton.setText(_translate("CurrentWindow", "Guest"))
        self.signUpButton.setText(_translate("CurrentWindow", "Sign Up"))
        self.loginButton.setText(_translate("CurrentWindow", "Login"))

    def switch_sign(self):
        self.sign_window = QtWidgets.QMainWindow()
        self.ui = sign_window()
        self.ui.setupUi(self.sign_window, CurrentWindow)
        self.sign_window.show()
        CurrentWindow.hide()

    def switch_menu(self):
        self.Food_window = QtWidgets.QMainWindow()
        self.ui = Food_Window()
        self.ui.setupUi(self.Food_window, CurrentWindow)
        CurrentWindow.hide()
        self.Food_window.show()
    
    def switch_cook(self):
        self.Cook_window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowChef()
        self.ui.setupUi(self.Cook_window, CurrentWindow)
        CurrentWindow.hide()
        self.Cook_window.show()
    
    def switch_sales(self):
        self.sales_window = QtWidgets.QMainWindow()
        self.ui = Sales_Window()
        self.ui.setupUi(self.sales_window)
        CurrentWindow.hide()
        self.sales_window.show()

    def switch_admin(self):
        self.Manager_Window = QtWidgets.QMainWindow()
        self.ui = ManagerWindow()
        self.ui.setupUi(self.Manager_Window)
        CurrentWindow.hide()
        self.Manager_Window.show()

    def guestVeri(self):
        addCurrentUser(User[0])
        addCurrentUser(0)
        self.switch_menu()
        
    def LoginVeri(self):
        value1 = self.LogUser_lineEdit.text()
        value2 = self.LogPass_lineEdit.text()

        test = getUserSize()

        for i in range(test):
            if(value1 == User[i].getUser() and value2 == User[i].getPass()):
                if(User[i].getType() == 1 or User[i].getType() == 2):
                    addCurrentUser(User[i]) 
                    addCurrentUser(i)
                    self.switch_menu()
                    break
                elif(User[i].getType() == 3):
                    addCurrentUser(User[i]) 
                    addCurrentUser(i)
                    print("Delivery")
                elif(User[i].getType() == 4):
                    addCurrentUser(User[i]) 
                    addCurrentUser(i)
                    self.switch_cook()
                    break
                elif(User[i].getType() == 5):
                    addCurrentUser(User[i]) 
                    addCurrentUser(i)
                    self.switch_sales()
                    break
                elif(User[i].getType() == 6):
                    addCurrentUser(User[i]) 
                    addCurrentUser(i)
                    self.switch_admin()
                    break
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    CurrentWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())
