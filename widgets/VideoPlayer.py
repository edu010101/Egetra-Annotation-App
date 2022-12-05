import cv2
import numpy as np
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect
from PIL import Image

class VideoPlayer():
    def __init__(self, MainWindow):
        super().__init__()
        self.Viewer = QLabel(MainWindow)
        self.Viewer.setStyleSheet(u"QLabel{background-color:rgb(0,0,0)}")
        self.Viewer.setGeometry(QRect(0, 0, 500, 500))       

    def SetImage(self, Cv2Image):
        Height, Width, Channel = Cv2Image.shape
        BytesPerLine = 3 * Width
        QtImage = QImage(Cv2Image.data, Width, Height, BytesPerLine, QImage.Format_BGR888)
        self.Viewer.setPixmap(QPixmap(QtImage))
        self.Viewer.setScaledContents(True)

    