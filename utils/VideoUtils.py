import cv2
import numpy as np

def CalculateTimeBeetwenFrames(VideoFps):
    TimeBeetwenFrames = 1 / VideoFps
    return TimeBeetwenFrames