from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
import sys
from widgets import VideoPlayer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        

        self.VideoPlayer = VideoPlayer(self)
        







App = QApplication(sys.argv)
Window = MainWindow()
Window.show() 
App.exec()

