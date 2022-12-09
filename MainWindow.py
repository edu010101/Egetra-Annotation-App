from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
import sys
from widgets import VideoPlayerWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.VideoPlayer = VideoPlayerWidget(self, 320, 0)
        

        self.showMaximized()






App = QApplication(sys.argv)
Window = MainWindow()
Window.show() 
App.exec()

