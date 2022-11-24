from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
import sys

from ButtonTest import BotaoLado

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")
        button= BotaoLado()
        button2 = button.GetButton()
        print(type(button2))
        self.setCentralWidget(button2)
        

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)




app = QApplication(sys.argv)
window = MainWindow()
window.show() 
app.exec()

