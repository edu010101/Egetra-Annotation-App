from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setFixedSize(100,100)
        self.button.setCheckable(True)

        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        
        self.setCentralWidget(Button)
        self.Widg

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)




app = QApplication(sys.argv)
window = MainWindow()
window.show() 
app.exec()

