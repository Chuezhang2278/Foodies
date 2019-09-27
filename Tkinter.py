import sys
from PyQt5.QtWidgets import QDialog, QApplication

from Test import *

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.disp) # Event handeling when button is clicked, self.disp is calling function below
        self.show()
    def disp(self): # Function activated when button is pressed
        print('hello') # Action
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())