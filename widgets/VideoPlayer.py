from PyQt5.QtWidgets import QLabel, QSlider, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt 
from services import Video
from utils import AddSpacerInLayout, AddWidgetInLayout, ClickerSlider, MediaButtons, CreateImageViewer, CreateVideoSlider, VideoThread

import asyncio
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread


class VideoPlayerWidget(QWidget):
    def __init__(self, MainWindow, X, Y):
        super().__init__(MainWindow)
        self.setGeometry(X, Y, 1280, 800)

        self.PrincipalVerticalLayout = QVBoxLayout(self)
        
        self.MediaButtonsLayout = QHBoxLayout()
        
        self.Viewer = CreateImageViewer(self)
        AddWidgetInLayout(self.PrincipalVerticalLayout, self.Viewer)
        
        self.Slider = CreateVideoSlider(self)
        self.Slider.valueChanged.connect(self.ChangeVideoFrameBasedOnSlider)
        AddWidgetInLayout(self.PrincipalVerticalLayout,self.Slider)

        self.CreateTimeCounter()
        
        self.Back1Second = MediaButtons.CreateBack1SecondButton(self)
        self.Back1Frame = MediaButtons.CreateBack1FrameButton(self)
        
        self.PlayPause = MediaButtons.CreatePlayPauseButton(self)

        self.Foward1Frame = MediaButtons.CreateFoward1FrameButton(self)
        self.Foward1Second = MediaButtons.CreateFoward1SecondButton(self)
        
        self.AddElementsToScreen()
        
        self.CreateHorizontalSpacer(470)
        
        self.CreateVideo()

        self.PrincipalVerticalLayout.addLayout(self.MediaButtonsLayout) 

    def CreateVideo(self):
        self.Video = VideoThread('/home/edu0101/Downloads/file_example_MP4_1280_10MG (1).mp4', self.Viewer, self.Slider)
        

        self.ActivateButtons()

    def CreateTimeCounter(self):
        self.TimeCounter = QLabel(self)
        self.TimeCounter.setText("10:55")
        AddWidgetInLayout(self.MediaButtonsLayout,self.TimeCounter)
    
    def CreateHorizontalSpacer(self, SpacerWidth):
        HorizontalSpacer = QSpacerItem(SpacerWidth, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        AddSpacerInLayout(self.MediaButtonsLayout, HorizontalSpacer)
    
    def ChangeVideoFrameBasedOnSlider(self):
      CurrentFrameId = self.Slider.value()
      self.Video.SetVideoFrame(CurrentFrameId)

    def ActivateButtons(self):
        self.Foward1Second.pressed.connect(self.Video.NextSecond)
        #self.Foward1Second.pressed.connect(self.Video.NextSecond)
        self.Foward1Frame.pressed.connect(self.Video.NextFrame)
        self.Back1Second.pressed.connect(self.Video.PreviousSecond)
        self.Back1Frame.pressed.connect(self.Video.PreviousFrame)
        self.PlayPause.clicked.connect(self.Video.Playf)

        self.Slider.setMinimum(0)
        self.Slider.setMaximum(int(self.Video.GetTotalFrames()))
        self.Video.FrameChangeSignal.connect(self.Video.UpdateThreadImage)
        self.Video.start()

    def AddElementsToScreen(self):
        AddWidgetInLayout(self.MediaButtonsLayout,self.Back1Second)
        AddWidgetInLayout(self.MediaButtonsLayout,self.Back1Frame)
        AddWidgetInLayout(self.MediaButtonsLayout,self.PlayPause)
        AddWidgetInLayout(self.MediaButtonsLayout,self.Foward1Frame)
        AddWidgetInLayout(self.MediaButtonsLayout,self.Foward1Second)





