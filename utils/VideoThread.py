from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
import time
import cv2
from PyQt5.QtGui import QPixmap, QImage
from utils import VideoUtils

class VideoThread(QThread):
    FrameChangeSignal = pyqtSignal()

    def __init__(self, VideoPath, Viewer, Slider, TimeCounter, VideoInfoWidget):
        super().__init__()
        self.Viewer = Viewer
        self.Slider = Slider
        self.TimeCounter = TimeCounter
        self.Video = cv2.VideoCapture(VideoPath)
        self.PlayBoolean = False
        self.VideoSpeedMode = 1

        self.TotalFrames = self.Video.get(cv2.CAP_PROP_FRAME_COUNT)
        self.FPS = self.Video.get(cv2.CAP_PROP_FPS)
        self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS)

        #Loads the first frame to display
        _, self.CurrentFrame = self.Video.read()
        self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
        
        self.ShowImageInViewer()

    def SetVideoFrame(self, FrameNumber):
        if 0 < FrameNumber < self.TotalFrames:
            self.Video.set(cv2.CAP_PROP_POS_FRAMES, FrameNumber)
            
            _, self.CurrentFrame = self.Video.read()
            self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
            self.CurrentTimeInMilliseconds = self.Video.get(cv2.CAP_PROP_POS_MSEC)
            
            self.Slider.setValue(round(FrameNumber))
            self.TimeCounter.setText(self.ConvertMillisecondsTime(self.CurrentTimeInMilliseconds))
            #self.FrameChangeSignal.emit()
            self.GetCurrentVideoStatus()
            self.ShowImageInViewer()

    def ShowImageInViewer(self):
        Height, Width, Channel = self.CurrentFrame.shape
        BytesPerLine = 3 * Width
        QtImage = QImage(self.CurrentFrame.data, Width, Height, BytesPerLine, QImage.Format_BGR888)
        self.Viewer.setPixmap(QPixmap(QtImage))
        self.Viewer.setScaledContents(True)

    #The name of the method needs to be "run", because its a QThread native method
    def run(self):
        while True:
            if (self.PlayBoolean == True) and (self.CurrentFrameId < self.TotalFrames):
                #The delay beetwen frames that set the video speed
                time.sleep(self.TimeBeetwenFrames)

                _, self.CurrentFrame = self.Video.read()
                self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
                self.GetCurrentVideoStatus()
                #self.Slider.setValue(round(FrameNumber))
                
                self.FrameChangeSignal.emit()
    
    def ConvertMillisecondsTime(self, MilisecondsTime):
        Seconds=int((MilisecondsTime/1000)%60)
        Minutes=int((MilisecondsTime/(1000*60))%60)
        Hours=int((MilisecondsTime/(1000*60*60))%24)

        TimeString = "%02d:%02d:%02d" % (Hours, Minutes, Seconds)

        return TimeString

    def GetTotalFrames(self):
        return self.TotalFrames

    def GetCurrentFrame(self):
        return self.CurrentFrame

    def GetCurrentVideoStatus(self):
        print('Current in frame ',self.CurrentFrameId, ' de Fps ', self.FPS)

    def NextSecond(self):
        self.SetVideoFrame(self.CurrentFrameId+round(self.FPS))

    def PreviousSecond(self):
        self.SetVideoFrame(self.CurrentFrameId-round(self.FPS))
        
    def NextFrame(self):
        self.SetVideoFrame(self.CurrentFrameId+1)
        
    def PreviousFrame(self):
        self.SetVideoFrame(self.CurrentFrameId-1)
    
    def PlayOrPause(self):
        self.PlayBoolean = not self.PlayBoolean

    def SwitchSpeed(self):
        if self.VideoSpeedMode == 1:
            self.VideoSpeedMode = 2
            self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS) / 2
        elif self.VideoSpeedMode == 2:
            self.VideoSpeedMode = 5
            self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS) / 5
        else:
            self.VideoSpeedMode = 1
            self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS) 
    
    @pyqtSlot()
    def UpdateThreadImage(self):
        self.ShowImageInViewer()
        
        
    



