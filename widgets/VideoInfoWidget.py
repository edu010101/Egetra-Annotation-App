from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QSizePolicy
from utils import InformationLabel, AddWidgetInLayout

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
        AddWidgetInLayout(self.MainVerticallayout, self.RoadLabel)
        AddWidgetInLayout(self.MainVerticallayout, self.Direction)
        AddWidgetInLayout(self.MainVerticallayout, self.Latitude)
        AddWidgetInLayout(self.MainVerticallayout, self.Longitude)
        AddWidgetInLayout(self.MainVerticallayout, self.Km)
        AddWidgetInLayout(self.MainVerticallayout, self.Data)



