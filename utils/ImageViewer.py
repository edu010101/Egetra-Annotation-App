from PyQt5.QtWidgets import QLabel
from utils.StylesheetUtils import LoadCSS

class VideoViewer(QLabel):
    def __init__(self, ParentWidget, CSS=False):
        super().__init__(ParentWidget)
        if CSS:
            CSS = LoadCSS(CSS)
            self.setStyleSheet(CSS)