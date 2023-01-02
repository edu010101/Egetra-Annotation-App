from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
import time
import os
import cv2
import numpy
from PyQt5.QtGui import QPixmap, QImage
from utils import VideoUtils, TimeAndDateUtils, JsonUtils, CoordinatesUtils

class VideoThread(QThread):
    FrameChangeSignal = pyqtSignal(numpy.ndarray)
    def __init__(self, VideoWidget):
        super().__init__()
        self.coords = JsonUtils.LoadJson('/home/edu0101/Desktop/Egetra-Annotation-App/CoordinatesDatabase/CorrdinatesDict.json')
        
        self.PlayBoolean = False
        self.HaveJson = False
        self.VideoSpeedMode = 1
        self.VideoInfoWidget = VideoWidget.VideoInfoWidget
        self.Viewer = VideoWidget.Viewer
        self.Slider = VideoWidget.Slider
        self.TimeCounter = VideoWidget.TimeCounter
        self.VideoSpeedButton = VideoWidget.VideoSpeed
        
        self.VideoPath = VideoWidget.ParentWidget.FilePaths
        self.Video = cv2.VideoCapture(self.VideoPath)
        self.TotalFrames = self.Video.get(cv2.CAP_PROP_FRAME_COUNT)
        self.FPS = self.Video.get(cv2.CAP_PROP_FPS)
        self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS)
        
        self.CurrentCoordinates = None
        self.CreateJson()

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

            if self.HaveJson:
                self.CurrentCoordinates = self.GetCurrentCoordinates()
                self.VideoInfoWidget.Latitude.ChangeInformation(str(self.CurrentCoordinates[0]))
                self.VideoInfoWidget.Longitude.ChangeInformation(str(self.CurrentCoordinates[1]))
                self.VideoInfoWidget.Km.ChangeInformation(str(CoordinatesUtils.FindClosestPoint(self.CurrentCoordinates, self.coords['MS-112'])[1])) 
            
            #self.Slider.setValue(round(FrameNumber))
            self.TimeCounter.setText(TimeAndDateUtils.ConvertMillisecondsTime(self.CurrentTimeInMilliseconds))
            self.GetCurrentVideoStatus()
            self.FrameChangeSignal.emit(self.CurrentFrame)
            

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
                #self.Slider.setValue(round(self.CurrentFrameId))
                
                #self.FrameChangeSignal.emit(self.CurrentFrame)
                Height, Width, Channel = self.CurrentFrame.shape
                BytesPerLine = 3 * Width
                QtImage = QImage(self.CurrentFrame.data, Width, Height, BytesPerLine, QImage.Format_BGR888)
                self.Viewer.setPixmap(QPixmap(QtImage))
                self.Viewer.setScaledContents(True)
                self.UpdateViewer = False
    
    def SwitchSpeed(self):
        if self.VideoSpeedMode == 1:
            self.VideoSpeedMode = 2
            self.VideoSpeedButton.setText('2x')
            self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS) / 2

        elif self.VideoSpeedMode == 2:
            self.VideoSpeedMode = 5
            self.VideoSpeedButton.setText('5x')
            self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS) / 5

        else:
            self.VideoSpeedMode = 1
            self.VideoSpeedButton.setText('1x')
            self.TimeBeetwenFrames = VideoUtils.CalculateTimeBeetwenFrames(self.FPS) 
    
    def CreateJson(self):
        if os.path.isfile(self.VideoPath + '.json'):
            self.HaveJson = True
            self.VideoJson = JsonUtils.LoadJson(self.VideoPath + '.json')

    def GetTotalFrames(self):
        return self.TotalFrames

    def GetCurrentFrame(self):
        return self.CurrentFrame
    
    def GetCurrentCoordinates(self):
        FrameDict = self.VideoJson[str(int(self.CurrentFrameId))]
        Coordinates = FrameDict['Latitude'],FrameDict['Longitude']
        return Coordinates

    def GetCurrentVideoStatus(self):
        print('Current in frame ',self.CurrentFrameId, ' de Fps ', self.FPS, self.HaveJson)

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



