import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
import time 

class Video():
    def __init__(self, VideoPath, Viewer, Slider):
        self.Viewer = Viewer
        self.Slider = Slider
        self.Video = cv2.VideoCapture(VideoPath)
        self.TotalFrames = self.Video.get(cv2.CAP_PROP_FRAME_COUNT)
        self.FPS = self.Video.get(cv2.CAP_PROP_FPS)

        _, self.CurrentFrame = self.Video.read()
        self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
        
        self.SetImage()

    def SetVideoFrame(self, FrameNumber):
        if 0 < FrameNumber < self.TotalFrames:
            self.Video.set(cv2.CAP_PROP_POS_FRAMES, FrameNumber)
            self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
            #self.Slider.setValue(FrameNumber)
            _, self.CurrentFrame = self.Video.read()
            self.SetImage()
        
    def GetTotalFrames(self):
        return self.TotalFrames

    def ReadCurrentFrame(self):
        _, self.CurrentFrame = self.Video.read()

    def GetCurrentFrame(self):
        return self.CurrentFrame

    def SetImage(self):
        Height, Width, Channel = self.CurrentFrame.shape
        BytesPerLine = 3 * Width
        QtImage = QImage(self.CurrentFrame.data, Width, Height, BytesPerLine, QImage.Format_BGR888)
        self.Viewer.setPixmap(QPixmap(QtImage))
        self.Viewer.setScaledContents(True)

    def GetCurrentVideoStatus(self):
        print('Current in frame ',self.CurrentFrameId, ' de Fps ', self.FPS)

    def NextSecond(self):
        self.SetVideoFrame(self.CurrentFrameId+round(self.FPS))
        self.GetCurrentVideoStatus()

    def PreviousSecond(self):
        self.SetVideoFrame(self.CurrentFrameId-round(self.FPS))
        self.GetCurrentVideoStatus()
        
    def NextFrame(self):
        self.SetVideoFrame(self.CurrentFrameId+1)
        self.GetCurrentVideoStatus()
        

    def PreviousFrame(self):
        self.SetVideoFrame(self.CurrentFrameId-1)
        self.GetCurrentVideoStatus()
        

    def Play(self):
        x = 0 

        while(x< 10):
        # Capture frame-by-frame
            _, self.CurrentFrame = self.Video.read()
            print(self.Video.get(cv2.CAP_PROP_POS_FRAMES))
            self.SetImage()
            time.sleep(1)
            
            print('um')
            x+= 1
            
