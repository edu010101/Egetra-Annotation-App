from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtGui import QPixmap, QImage


class ViewerUpdater(QThread):
    FrameChangeSignal = pyqtSignal()
    def __init__(self, Viewer):
        super().__init__()
        self.UpdateViewer = False
        self.Viewer = Viewer

    #The name of the method needs to be "run", because its a QThread native method
    def run(self):
        while True:
            if self.UpdateViewer == True:
                Height, Width, Channel = self.Frame.shape
                BytesPerLine = 3 * Width
                QtImage = QImage(self.Frame.data, Width, Height, BytesPerLine, QImage.Format_BGR888)
                self.Viewer.setPixmap(QPixmap(QtImage))
                self.Viewer.setScaledContents(True)
                self.UpdateViewer = False

                self.FrameChangeSignal.emit()
    
    @pyqtSlot()
    def UpdateThreadImage(self, Frame):
        self.Frame = Frame
        self.UpdateViewer = True

        
        
    



