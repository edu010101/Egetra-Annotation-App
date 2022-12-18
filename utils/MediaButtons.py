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
        


def CreatePlayPauseButton(Widget):
    PlayPause = QPushButton(Widget)
    PlayPause.setFixedWidth(50)
    PlayPause.setFixedHeight(50)
    #self.Pause.setFlat(True)
    PlayPause.setStyleSheet(u"border-image: url('icons/PlayIcon.png');")

    #self.Pause.setIconSize(QSize(45,45));
    return PlayPause

    
def CreateBack1SecondButton(Widget):
    Back1Second = QPushButton(Widget)
    Back1Second.setFixedWidth(50)
    Back1Second.setFixedHeight(40)
    Back1Second.setIcon(QIcon('/home/eduardo/Downloads/play-back-outline.svg'))

    return Back1Second

def CreateFoward1SecondButton(Widget):
    Foward1Second = QPushButton(Widget)
    Foward1Second.setFixedWidth(50)
    Foward1Second.setFixedHeight(40)
    Foward1Second.setIcon(QIcon('/home/eduardo/Downloads/play-forward-outline.svg'))
    
    return Foward1Second
    
def CreateBack1FrameButton(Widget):
    Back1Frame = QPushButton(Widget)
    Back1Frame.setFixedWidth(50)
    Back1Frame.setFixedHeight(40)
    Back1Frame.setIcon(QIcon('/home/eduardo/Downloads/play-skip-back-outline.svg'))
    
    return Back1Frame

def CreateFoward1FrameButton(Widget):
    Foward1Frame = QPushButton(Widget)
    Foward1Frame.setFixedWidth(50)
    Foward1Frame.setFixedHeight(40)
    Foward1Frame.setIcon(QIcon('/home/eduardo/Downloads/play-skip-forward-outline.svg'))
   
    return Foward1Frame

def CreateVideoSpeedButton(Widget):
    VideoSpeed = QPushButton(Widget)
    VideoSpeed.setFixedWidth(50)
    VideoSpeed.setFixedHeight(40)
    #VideoSpeed.setIcon()

    return VideoSpeed