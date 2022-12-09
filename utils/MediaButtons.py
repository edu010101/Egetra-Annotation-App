from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QSize


def CreatePlayPauseButton(Widget):
    PlayPause = QPushButton(Widget)
    PlayPause.setFixedWidth(50)
    PlayPause.setFixedHeight(50)
    #self.Pause.setFlat(True)
    PlayPause.setIcon(QIcon('/home/eduardo/Downloads/play-outline.svg'))
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
