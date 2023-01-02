from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtGui import QPixmap, QImage
import numpy
import time
class ViewerUpdater(QThread):
    def __init__(self, Viewer):
        super().__init__()
        self.UpdateViewer = False
        self.Viewer = Viewer
        self.Frame = None

    #The name of the method needs to be "run", because its a QThread native method
    def run(self):
        while True:
            if self.UpdateViewer:   
                Height, Width, Channel = self.Frame.shape
                BytesPerLine = 3 * Width
                QtImage = QImage(self.Frame.data, Width, Height, BytesPerLine, QImage.Format_BGR888)
                self.Viewer.setPixmap(QPixmap(QtImage))
                self.Viewer.setScaledContents(True)
                self.UpdateViewer = False
    
    @pyqtSlot(numpy.ndarray)
    def UpdateThreadImage(self, Frame):
        self.Frame = Frame
        self.UpdateViewer = True
        


    

        
        
    



