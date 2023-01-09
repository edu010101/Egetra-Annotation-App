from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from utils import AddSpacerInLayout, AddWidgetInLayout, MediaButtons, CreateVideoSlider, VideoThread, ViewerUpdater, ClickerSlider, ImageViewer
import os

class VideoPlayerWidget(QWidget):
    def __init__(self, ParentWidget, VideoInfoWidget):
        super().__init__(ParentWidget)        
        self.ParentWidget = ParentWidget
        self.setMinimumSize(300, 300)
        
        self.VideoInfoWidget = VideoInfoWidget
        self.VideoInfoWidget.StartContent(self.ParentWidget.FilePaths)
        
        self.PrincipalVerticalLayout = QVBoxLayout(self)
                                                          
        self.MediaButtonsLayout = QHBoxLayout()
        self.MediaButtonsLayout.setSpacing(20)
        
        self.Viewer = ImageViewer.VideoViewer(self)
        self.Slider = ClickerSlider(self, 'stylesheets/VideoSlider.css')

        self.CreateTimeCounter()
        
        self.Back1Second = MediaButtons.FixedButton(self, 'stylesheets/FastRewindButton.css', 45, 30)
        self.Back1Frame = MediaButtons.FixedButton(self, 'stylesheets/RewindButton.css', 30, 30)
        self.Foward1Frame = MediaButtons.FixedButton(self, 'stylesheets/FowardButton.css', 30, 30)
        self.Foward1Second = MediaButtons.FixedButton(self, 'stylesheets/FastFowardButton.css', 45, 30)
        self.PlayPause  = MediaButtons.ToggleButton(self, 'stylesheets/PlayButton.css','stylesheets/PauseButton.css', 30, 30)
        
        self.AddElementsToScreen()
        
        self.CreateHorizontalSpacer(350)

        self.VideoSpeed = MediaButtons.CreateVideoSpeedButton(self)
        AddWidgetInLayout(self.MediaButtonsLayout,self.VideoSpeed)
        
        self.CreateVideo()

        self.Slider.Video = self.Video

        self.PrincipalVerticalLayout.addLayout(self.MediaButtonsLayout) 


    def CreateVideo(self):
        self.Video = VideoThread(self)

        self.ActivateButtons()

    def CreateTimeCounter(self):
        self.TimeCounter = QLabel(self)
        self.TimeCounter.setText("00:00:00")
        self.TimeCounter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.TimeCounter.setStyleSheet(u"color: rgb(255, 255, 255);")
        AddWidgetInLayout(self.MediaButtonsLayout,self.TimeCounter)
    
    def CreateHorizontalSpacer(self, SpacerWidth):
        HorizontalSpacer = QSpacerItem(SpacerWidth, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        AddSpacerInLayout(self.MediaButtonsLayout, HorizontalSpacer)
    
    def ChangeVideoFrameBasedOnSlider(self):
        CurrentFrameId = self.Slider.value()
        #self.Video.SetVideoFrame(CurrentFrameId)

    def ActivateButtons(self):
        self.Foward1Second.pressed.connect(self.Video.NextSecond)
        self.Foward1Frame.pressed.connect(self.Video.NextFrame)
        self.Back1Second.pressed.connect(self.Video.PreviousSecond)
        self.Back1Frame.pressed.connect(self.Video.PreviousFrame)
        self.PlayPause.clicked.connect(self.Video.PlayOrPause)
        self.VideoSpeed.clicked.connect(self.Video.SwitchVideoSpeed)

        self.Slider.setMinimum(0)
        self.Slider.setMaximum(int(self.Video.GetTotalFrames())-5)
        
        self.Video.start()


    def AddElementsToScreen(self):
        AddWidgetInLayout(self.PrincipalVerticalLayout, self.Viewer)
        AddWidgetInLayout(self.PrincipalVerticalLayout,self.Slider)

        AddWidgetInLayout(self.MediaButtonsLayout,self.Back1Second)
        AddWidgetInLayout(self.MediaButtonsLayout,self.Back1Frame)
        AddWidgetInLayout(self.MediaButtonsLayout,self.PlayPause)
        AddWidgetInLayout(self.MediaButtonsLayout,self.Foward1Frame)
        AddWidgetInLayout(self.MediaButtonsLayout,self.Foward1Second)
        





