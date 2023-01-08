from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from utils import InformationLabel, AddWidgetInLayout, CoordinatesUtils
import os

class VideoInfoWidget(QWidget):
    def __init__(self, ParentWidget, X, Y):
        super().__init__(ParentWidget)
        self.MainVerticallayout = QVBoxLayout(self)
        
        self.RoadLabel = InformationLabel(self, 'Rodovia', 'Conteudo')
        self.Direction = InformationLabel(self, 'Sentido', 'Conteudo')
        self.Latitude = InformationLabel(self, 'Latitude', '?')
        self.Longitude = InformationLabel(self, 'Longitude', '?')
        self.Km = InformationLabel(self, 'Quilômetro', '?')
        self.Data = InformationLabel(self, 'Data', 'Conteudo')

        self.CoordinatesUpdater = CoordinatesInfoUpdaterThread(self)
        self.Thread = QThread()
        self.CoordinatesUpdater.moveToThread(self.Thread)
        self.Thread.start()
       
        self.AddWidgetsinLayout()
        
    def StartContent(self, VideoPath):
        #Video Name example: MS-112_C_01_R0
        VideoName = os.path.splitext(os.path.split(VideoPath)[1])[0]
        Road = VideoName.split('_')[0] 
        Direction = VideoName.split('_')[1]
        
        self.CoordinatesManager = CoordinatesUtils.CoordinatesManager(Road, Direction)
        
        if Direction == 'C':
            Direction = 'Crescente'
        else:
            Direction = 'Decrescente'
        
        self.RoadLabel.ChangeInformation(Road)
        self.Direction.ChangeInformation(Direction)

    def AddWidgetsinLayout(self):
        AddWidgetInLayout(self.MainVerticallayout, self.RoadLabel)
        AddWidgetInLayout(self.MainVerticallayout, self.Direction)
        AddWidgetInLayout(self.MainVerticallayout, self.Latitude)
        AddWidgetInLayout(self.MainVerticallayout, self.Longitude)
        AddWidgetInLayout(self.MainVerticallayout, self.Km)
        AddWidgetInLayout(self.MainVerticallayout, self.Data)

class CoordinatesInfoUpdaterThread(QObject):
    def __init__(self, InfoWidget):
        super().__init__()
        self.InfoWidget = InfoWidget
    
    @pyqtSlot(tuple)
    def run(self, Coordinates):
        self.InfoWidget.Latitude.ChangeInformation("{:.4f}".format(Coordinates[0]))
        self.InfoWidget.Longitude.ChangeInformation("{:.4f}".format(Coordinates[1]))
        self.InfoWidget.Km.ChangeInformation("{:.2f}".format(int(self.InfoWidget.CoordinatesManager.FindClosestPoint(Coordinates)[1]) / 1000))