from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from utils.StylesheetUtils import LoadCSS


class ToggleButton(QPushButton):
    def __init__(self, ParentWidget, CSS1, CSS2, X=40, Y=40):
        super().__init__(ParentWidget)
        self.CSS1 = LoadCSS(CSS1)
        self.CSS2 = LoadCSS(CSS2)
        self.setStyleSheet(self.CSS1)
        self.clicked.connect(self.Toggle)
        self.setCheckable(True)
        self.setFixedWidth(X)
        self.setFixedHeight(Y)
    
    def Toggle(self):
        if self.isChecked():
            self.setStyleSheet(self.CSS2)
        else:
            self.setStyleSheet(self.CSS1)
    
class FixedButton(QPushButton):
    def __init__(self, ParentWidget, CSS, X=40, Y=40):
        super().__init__(ParentWidget)
        self.setFixedWidth(X)
        self.setFixedHeight(Y)
        CSS = LoadCSS(CSS)
        self.setStyleSheet(CSS)

def CreateVideoSpeedButton(Widget):
    VideoSpeed = QPushButton(Widget)
    VideoSpeed.setFixedWidth(50)
    VideoSpeed.setFixedHeight(40)
    VideoSpeed.setText('1x')
    VideoSpeed.setFlat(True)
    VideoSpeed.setStyleSheet(u"""font: 75 20pt "Ubuntu";color:rgb(255, 255, 255); font-weight: bold;""")
    #VideoSpeed.setIcon()

    return VideoSpeed