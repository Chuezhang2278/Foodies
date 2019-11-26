# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapWindow.ui',
# licensing of 'MapWindow.ui' applies.
#
# Created: Mon Nov 25 18:08:54 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKit, QtWebKitWidgets

class MapWindow(object):
    def setupUi(self, MapWindow):
        MapWindow.setObjectName("MapWindow")
        MapWindow.resize(1402, 1050)
        MapWindow.setMinimumSize(QtCore.QSize(1402, 1050))
        MapWindow.setMaximumSize(QtCore.QSize(1402, 1050))
        self.centralwidget = QtWidgets.QWidget(MapWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1402, 1025))
        self.centralwidget.setMaximumSize(QtCore.QSize(1402, 1025))
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(60, 20, 93, 30))
        self.backButton.setObjectName("backButton")
        self.stepButton = QtWidgets.QPushButton(self.centralwidget)
        self.stepButton.setGeometry(QtCore.QRect(1150, 20, 191, 30))
        self.stepButton.setObjectName("stepButton")
        self.customerLabel = QtWidgets.QLabel(self.centralwidget)
        self.customerLabel.setGeometry(QtCore.QRect(55, 720, 700, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.customerLabel.setFont(font)
        self.customerLabel.setObjectName("customerLabel")
        self.customerLabel.setStyleSheet("background-color: #32414b;")
        self.initialLabel = QtWidgets.QLabel(self.centralwidget)
        self.initialLabel.setGeometry(QtCore.QRect(60, 770, 361, 31))
        self.initialLabel.setObjectName("initialLabel")
        self.initialLabel.setStyleSheet("background-color: #32414b;")
        self.finalLabel = QtWidgets.QLabel(self.centralwidget)
        self.finalLabel.setGeometry(QtCore.QRect(60, 800, 361, 31))
        self.finalLabel.setObjectName("finalLabel")
        self.finalLabel.setStyleSheet("background-color: #32414b;")
        self.startLabel = QtWidgets.QLabel(self.centralwidget)
        self.startLabel.setGeometry(QtCore.QRect(730, 770, 361, 31))
        self.startLabel.setObjectName("startLabel")
        self.startLabel.setStyleSheet("background-color: #32414b;")
        self.arrivalLabel = QtWidgets.QLabel(self.centralwidget)
        self.arrivalLabel.setGeometry(QtCore.QRect(730, 800, 361, 31))
        self.arrivalLabel.setObjectName("arrivalLabel")
        self.arrivalLabel.setStyleSheet("background-color: #32414b;")
        self.distanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.distanceLabel.setGeometry(QtCore.QRect(60, 830, 361, 31))
        self.distanceLabel.setObjectName("distanceLabel")
        self.distanceLabel.setStyleSheet("background-color: #32414b;")
        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel.setGeometry(QtCore.QRect(730, 830, 361, 31))
        self.durationLabel.setObjectName("durationLabel")
        self.durationLabel.setStyleSheet("background-color: #32414b;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 950, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.oneStar = QtWidgets.QRadioButton(self.centralwidget)
        self.oneStar.setGeometry(QtCore.QRect(555, 913, 61, 20))
        self.oneStar.setObjectName("oneStar")
        self.twoStar = QtWidgets.QRadioButton(self.centralwidget)
        self.twoStar.setGeometry(QtCore.QRect(625, 913, 71, 20))
        self.twoStar.setObjectName("twoStar")
        self.threeStar = QtWidgets.QRadioButton(self.centralwidget)
        self.threeStar.setGeometry(QtCore.QRect(705, 913, 81, 20))
        self.threeStar.setObjectName("threeStar")
        self.fourStar = QtWidgets.QRadioButton(self.centralwidget)
        self.fourStar.setGeometry(QtCore.QRect(795, 913, 81, 20))
        self.fourStar.setObjectName("fourStar")
        self.fiveStar = QtWidgets.QRadioButton(self.centralwidget)
        self.fiveStar.setGeometry(QtCore.QRect(895, 913, 95, 20))
        self.fiveStar.setObjectName("fiveStar")
        self.rateLabel = QtWidgets.QLabel(self.centralwidget)
        self.rateLabel.setGeometry(QtCore.QRect(430, 910, 121, 25))
        self.rateLabel.setObjectName("rateLabel")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 700, 1402, 181))
        self.background.setStyleSheet("background-color: #32414b;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.background.lower()
        font = QtGui.QFont()
        font.setPointSize(9.5)
        self.initialLabel.setFont(font)
        self.finalLabel.setFont(font)
        self.startLabel.setFont(font)
        self.arrivalLabel.setFont(font)
        self.distanceLabel.setFont(font)
        self.durationLabel.setFont(font)

        MapWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MapWindow)
        self.statusbar.setObjectName("statusbar")
        MapWindow.setStatusBar(self.statusbar)

        self.web = QtWebKitWidgets.QWebView(self.centralwidget)
        self.web.setGeometry(QtCore.QRect(0, 70, 1400, 610))
        self.web.load(QtCore.QUrl("https://www.google.com/maps/dir/The+City+College+of+New+York,+160+Convent+Ave,+New+York,+NY+10031/Grand+St,+New+York,+NY"))
        self.web.show()

        self.retranslateUi(MapWindow)
        QtCore.QMetaObject.connectSlotsByName(MapWindow)

    def retranslateUi(self, MapWindow):
        MapWindow.setWindowTitle(QtWidgets.QApplication.translate("MapWindow", "Delivery Information", None, -1))
        self.backButton.setText(QtWidgets.QApplication.translate("MapWindow", "Back", None, -1))
        self.stepButton.setText(QtWidgets.QApplication.translate("MapWindow", "Step By Step Instructions", None, -1))
        self.customerLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Customer: Placeholder Jia Ming Ma", None, -1))
        self.initialLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Initial Location: City College of New York", None, -1))
        self.finalLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Final Destination: Grand St ", None, -1))
        self.startLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Start Time: 07:43 PM", None, -1))
        self.arrivalLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Arrival Time: 8:03 PM", None, -1))
        self.distanceLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Distance: 312 miles", None, -1))
        self.durationLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Duration: 20 minutes", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MapWindow", "Delivery Complete", None, -1))
        self.oneStar.setText(QtWidgets.QApplication.translate("MapWindow", "☆", None, -1))
        self.twoStar.setText(QtWidgets.QApplication.translate("MapWindow", "☆☆", None, -1))
        self.threeStar.setText(QtWidgets.QApplication.translate("MapWindow", "☆☆☆", None, -1))
        self.fourStar.setText(QtWidgets.QApplication.translate("MapWindow", "☆☆☆☆", None, -1))
        self.fiveStar.setText(QtWidgets.QApplication.translate("MapWindow", "☆☆☆☆☆", None, -1))
        self.rateLabel.setText(QtWidgets.QApplication.translate("MapWindow", "Rate the customer:", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = MapWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
