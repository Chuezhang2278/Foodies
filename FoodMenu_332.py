# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FoodMenu_332.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Food_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FoodButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.FoodButton_1.setGeometry(QtCore.QRect(60, 140, 61, 28))
        self.FoodButton_1.setObjectName("FoodButton_1")
        self.FoodButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.FoodButton_2.setGeometry(QtCore.QRect(220, 140, 61, 28))
        self.FoodButton_2.setObjectName("FoodButton_2")
        self.FoodButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.FoodButton_3.setGeometry(QtCore.QRect(40, 200, 93, 28))
        self.FoodButton_3.setObjectName("FoodButton_3")
        self.FoodButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.FoodButton_4.setGeometry(QtCore.QRect(210, 200, 93, 28))
        self.FoodButton_4.setObjectName("FoodButton_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(440, 90, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 120, 35, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 180, 35, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 120, 35, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 35, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.FoodButton_1.clicked.connect(self.add_salad)
        self.FoodButton_2.clicked.connect(self.add_cheese)
        self.FoodButton_3.clicked.connect(self.add_onion)
        self.FoodButton_4.clicked.connect(self.add_lettuce)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("BurgerShack", "BurgerShack"))
        self.FoodButton_1.setText(_translate("MainWindow", "$0.90"))
        self.FoodButton_2.setText(_translate("MainWindow", "$1"))
        self.FoodButton_3.setText(_translate("MainWindow", "$2"))
        self.FoodButton_4.setText(_translate("MainWindow", "$3"))
        self.label.setText(_translate("MainWindow", "Salad"))
        self.label_4.setText(_translate("MainWindow", "Cheese"))
        self.label_3.setText(_translate("MainWindow", "Onion"))
        self.label_2.setText(_translate("MainWindow", "Lettuce"))

    def add_salad(self):
        self.emp = ["salad          $0.90"]
        self.listWidget.addItems(self.emp)
    def add_cheese(self):
        self.emp = ["cheese         $1"]
        self.listWidget.addItems(self.emp)
    def add_onion(self):
        self.emp = ["onion          $2"]
        self.listWidget.addItems(self.emp)
    def add_lettuce(self):
        self.emp = ["lettuce        $3"]
        self.listWidget.addItems(self.emp)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Food_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
