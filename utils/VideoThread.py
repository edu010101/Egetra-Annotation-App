from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
import time
import cv2
from PyQt5.QtGui import QPixmap, QImage
from utils import VideoUtils

class VideoThread(QThread):
    FrameChangeSignal = pyqtSignal()

    def __init__(self, VideoPath, Viewer, Slider):
        super().__init__()
        self.Viewer = Viewer
        self.Slider = Slider
        self.Video = cv2.VideoCapture(VideoPath)
        self.TotalFrames = self.Video.get(cv2.CAP_PROP_FRAME_COUNT)
        self.FPS = self.Video.get(cv2.CAP_PROP_FPS)
        self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS)
        self.PlayBoolean = False

        #Loads the first frame to display
        _, self.CurrentFrame = self.Video.read()
        self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
        
        self.SetImage()

    def SetVideoFrame(self, FrameNumber):
        if 0 < FrameNumber < self.TotalFrames:
            self.Video.set(cv2.CAP_PROP_POS_FRAMES, FrameNumber)
            self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
            self.Slider.setValue(round(FrameNumber))
            _, self.CurrentFrame = self.Video.read()
            #self.FrameChangeSignal.emit()
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
    
    def Playf(self):
        self.PlayBoolean = not self.PlayBoolean

    #The name of the method needs to be run, beacuse its a QThread 
    def run(self):
        while True:
            if self.PlayBoolean == True:
                #The delay beetwen frames that set the video speed
                time.sleep(self.TimeBeetwenFrames)

                _, self.CurrentFrame = self.Video.read()
                self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
                self.GetCurrentVideoStatus()
                #self.Slider.setValue(round(FrameNumber))
                
                self.FrameChangeSignal.emit()
    
    @pyqtSlot()
    def UpdateThreadImage(self):
        self.SetImage()
        
    



