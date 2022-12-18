from PyQt5.QtWidgets import QLabel, QSizePolicy

def CreateImageViewer(Widget):
    Viewer = QLabel(Widget)
    Viewer.setStyleSheet(u"QLabel{background-color:rgb(0,0,0)}")
    #self.Viewer.setGeometry(QRect(X, Y, 1280, 720))  
    return Viewer
    
    