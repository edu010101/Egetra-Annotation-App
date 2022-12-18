from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QMenuBar, QMenu, QStatusBar, QAction, QFileDialog
from PyQt5.QtCore import QDir
import sys
from widgets import VideoPlayerWidget, VideoInfoWidget, GetFilePath
from utils import AddWidgetInLayout
from functools import partial



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.MainWidget = QWidget(self)
        self.MainWidget.setStyleSheet(u"background-color: rgb(27, 27, 34);")
        self.MenuBar = QMenuBar(self)
        self.setMenuBar(self.MenuBar)
        
        self.FileMenu = QMenu(self.MenuBar)
        self.FileMenu.setTitle("Arquivo")
        self.MenuBar.addAction(self.FileMenu.menuAction())

        self.OpenFile = QAction(self)
        self.OpenFile.setText('Abrir arquivo')
        self.FileMenu.addAction(self.OpenFile)
        
        self.OpenFile.triggered.connect(partial(GetFilePath, self, 0))

    def InitializeVideo(self):
        self.PrincipalWidgetLayout = QHBoxLayout(self.MainWidget)

        self.VideoInfoSideBar = VideoInfoWidget(self.MainWidget, 200, 200)

        self.VideoPlayer = VideoPlayerWidget(self.MainWidget, self.VideoInfoSideBar)
        
        AddWidgetInLayout(self.PrincipalWidgetLayout, self.VideoPlayer)
        AddWidgetInLayout(self.PrincipalWidgetLayout, self.VideoInfoSideBar) 

        self.setCentralWidget(self.MainWidget)
    
    


    

App = QApplication(sys.argv)
Window = MainWindow()
Window.show() 
App.exec()





  
