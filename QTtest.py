import Manager

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
if __name__=='__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Manager.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())