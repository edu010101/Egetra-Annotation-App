from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QSizePolicy
from utils import InformationLabel, AddWidgetInLayout

class VideoInfoWidget(QWidget):
    def __init__(self, ParentWidget, X, Y):
        super().__init__(ParentWidget)
        self.MainVerticallayout = QVBoxLayout(self)
        
       
        self.RoadLabel = InformationLabel(self, 'Rodovia', 'Conteudo')
        self.Direction = InformationLabel(self, 'Sentido', 'Conteudo')
        self.Coordinates = InformationLabel(self, 'Coordenadas', 'Conteudo')
        self.Data = InformationLabel(self, 'Data', 'Conteudo')
        AddWidgetInLayout(self.MainVerticallayout, self.RoadLabel)
        AddWidgetInLayout(self.MainVerticallayout, self.Direction)
        AddWidgetInLayout(self.MainVerticallayout, self.Coordinates)
        AddWidgetInLayout(self.MainVerticallayout, self.Data)



