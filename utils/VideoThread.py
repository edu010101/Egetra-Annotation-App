from PyQt5.QtCore import pyqtSignal, QThread
import time
import os
import cv2
from PyQt5.QtGui import QPixmap, QImage
from utils import VideoUtils, TimeAndDateUtils, JsonUtils

class VideoThread(QThread):
    UpdateCoordinates = pyqtSignal(tuple)
    def __init__(self, VideoWidget):
        super().__init__()
        self.ChangeFrameBoolean = False
        self.CurrentSecond = 0
        self.PlayBoolean = False
        self.HaveJson = False
        self.CurrentCoordinates = None
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
        
        self.CheckAndStartJson()

        #Loads the first frame to display
        self.UpdateFrameAndTime()
        self.ConvertAndShowFrame()
        
        self.UpdateCoordinates.connect(self.VideoInfoWidget.CoordinatesUpdater.run)

    #The name of the method needs to be "run", because its a QThread native method
    def run(self):
        #Since this method is executed in parallel it should contain all the code necessary for it to run, thats why the code is so ugly 
        while True:
            #1º Scenario, play button is pressed
            if (self.PlayBoolean == True) and (self.CurrentFrameId < self.TotalFrames):
                #The delay beetwen frames that set the video speed
                time.sleep(self.TimeBeetwenFrames)

                self.UpdateFrameAndTime()
                self.ConvertAndShowFrame()

                self.CurrentTimeInMilliseconds = self.Video.get(cv2.CAP_PROP_POS_MSEC)

                #Update some elements every second instead of every frame
                if self.CurrentSecond != self.CurrentTimeInMilliseconds // 1000:
                    self.CurrentSecond = self.CurrentTimeInMilliseconds // 1000
                    print('Entrou')
                    
                    self.Slider.setValue(self.CurrentFrameId)
                    self.TimeCounter.setText(TimeAndDateUtils.ConvertMillisecondsTime(self.CurrentTimeInMilliseconds))
                    self.GetCurrentVideoStatus()

                    if self.HaveJson:
                        self.CurrentCoordinates = self.GetCurrentCoordinates()
                        self.UpdateCoordinates.emit(self.CurrentCoordinates)    
            
            #2º Scenario, any other way of change the video frame
            elif self.ChangeFrameBoolean :
                if 0 < self.FrameIdTarget < self.TotalFrames:
                    self.Video.set(cv2.CAP_PROP_POS_FRAMES, self.FrameIdTarget-1)
                    
                    self.UpdateFrameAndTime()
                    self.ConvertAndShowFrame()

                    self.Slider.setValue(self.CurrentFrameId)
                    self.TimeCounter.setText(TimeAndDateUtils.ConvertMillisecondsTime(self.CurrentTimeInMilliseconds))
                    self.GetCurrentVideoStatus()
                    
                    if self.HaveJson:
                        self.CurrentCoordinates = self.GetCurrentCoordinates()
                        self.UpdateCoordinates.emit(self.CurrentCoordinates)

                    self.ChangeFrameBoolean = False
                
    def UpdateFrameAndTime(self):
        _, self.CurrentFrame = self.Video.read()
        self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)
        self.CurrentTimeInMilliseconds = self.Video.get(cv2.CAP_PROP_POS_MSEC)

    def ConvertAndShowFrame(self):
        Height, Width, Channel = self.CurrentFrame.shape
        BytesPerLine = 3 * Width
        QtImage = QImage(self.CurrentFrame.data, Width, Height, BytesPerLine, QImage.Format_BGR888)
        self.Viewer.setPixmap(QPixmap(QtImage))
        self.Viewer.setScaledContents(True)    

    def SwitchVideoSpeed(self):
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
    
    def CheckAndStartJson(self):
        if os.path.isfile(self.VideoPath + '.json'):
            self.HaveJson = True
            self.VideoJson = JsonUtils.LoadJson(self.VideoPath + '.json')

    def GetTotalFrames(self):
        return self.TotalFrames

    def GetCurrentFrame(self):
        return self.CurrentFrame
    
    def GetCurrentCoordinates(self):
        FrameDict = self.VideoJson[str(int(self.CurrentFrameId))]
        Coordinates = FrameDict['latitude'],FrameDict['longitude']
        return Coordinates

    def GetCurrentVideoStatus(self):
        print('Current in frame ',self.CurrentFrameId, ' de Fps ', self.FPS, self.HaveJson)

    def NextSecond(self):
        self.FrameIdTarget = self.CurrentFrameId+round(self.FPS)
        self.ChangeFrameBoolean = True

    def PreviousSecond(self):
        self.FrameIdTarget = self.CurrentFrameId-round(self.FPS)
        self.ChangeFrameBoolean = True
        
    def NextFrame(self):
        self.FrameIdTarget = self.CurrentFrameId+1
        self.ChangeFrameBoolean = True
        
    def PreviousFrame(self):
        self.FrameIdTarget = self.CurrentFrameId-1
        self.ChangeFrameBoolean = True
    
    def PlayOrPause(self):
        self.PlayBoolean = not self.PlayBoolean



