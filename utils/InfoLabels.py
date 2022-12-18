from PyQt5.QtWidgets import QLabel

class InformationLabel(QLabel):
    def __init__(self, ParentWidget, Title, Information):
        super().__init__(ParentWidget) 
        self.Title = Title
        self.setText(Title + ': ' + Information)
        self.setFixedHeight(25)
        self.setStyleSheet(u"color: rgb(255, 255, 255);")

    
    def ChangeInformation(self, Information):
        self.setText(self.Title + ': ' + Information)
    


         