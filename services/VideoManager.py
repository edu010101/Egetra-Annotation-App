import cv2
import numpy as np


class Video():
    def __init__(self, VideoPath):
        self.Video = cv2.VideoCapture(VideoPath)
        self.TotalFrames = self.Video.get(cv2.CAP_PROP_FRAME_COUNT)
        self.CurrentFrameId = self.Video.get(cv2.CAP_PROP_POS_FRAMES)

    def SetVideoFrame(self, FrameNumber):
        self.Video.set(cv2.CAP_PROP_POS_FRAMES, FrameNumber)
    
    def GetTotalFrames(self):
        return self.TotalFrames

    def ReadCurrentFrame(self):
        _, self.CurrentFrame = self.Video.read()


