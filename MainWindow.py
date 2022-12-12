from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
import sys
from widgets import VideoPlayerWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.VideoPlayer = VideoPlayerWidget(self, 0, -100)
        

        self.showMaximized()






App = QApplication(sys.argv)
Window = MainWindow()
Window.show() 
App.exec()



from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import time


X = True
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    global X

    def run(self):
        print('mechamara') 
        # capture from web cam
        cap = cv2.VideoCapture('/home/edu0101/Downloads/file_example_MP4_1280_10MG (1).mp4')
        while True:
            if X == True:
                print(X)
                time.sleep(0.025)
                ret, cv_img = cap.read()
                if ret:
                    self.change.emit(cv_img)
                    

def swap():
    global X
    if X == False:
        X = True
    else:
        X= False
    print(X)

class App(QWidget):
    global X
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt live label demo")
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Webcam')
        self.button = QPushButton('Start')
        


        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        vbox.addWidget(self.button)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change.connect(self.update_image)
        # start the thread
        self.thread.start()
        self.button.clicked.connect(swap)



    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
   