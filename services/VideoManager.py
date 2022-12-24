import cv2
from PyQt5.QtGui import QPixmap, QImage
from utils import JsonUtils

class Video():
    def __init__(self, VideoPath, JsonPath, Viewer, Slider):
        self.Viewer = Viewer
        self.Slider = Slider

        self.VideoJson = JsonUtils.LoadJson(JsonPath)

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
            self.Slider.setValue(round(FrameNumber))
            _, self.CurrentFrame = self.Video.read()
            self.SetImage()
            self.GetCurrentVideoStatus()

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

    def PreviousSecond(self):
        self.SetVideoFrame(self.CurrentFrameId-round(self.FPS))
        
    def NextFrame(self):
        self.SetVideoFrame(self.CurrentFrameId+1)

    def PreviousFrame(self):
        self.SetVideoFrame(self.CurrentFrameId-1)

    

    def GetTotalFrames(self):
        return self.TotalFrames

    def ReadCurrentFrame(self):
        _, self.CurrentFrame = self.Video.read()

    def GetCurrentFrame(self):
        return self.CurrentFrame    
            

