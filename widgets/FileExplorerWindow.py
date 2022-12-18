from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
  

def GetFilePath(ParentWidget, Mode, Filter='All files (*.*)', BasePath=QDir.currentPath()):
    #OpenFile = 0
    #OpenFiles = 1
    #OpenDirectory = 2

    FilePaths = None
    
    if Mode == 0:
        FilePaths = (QFileDialog.getOpenFileName(ParentWidget, caption='Escolha o arquivo',
                                                directory=BasePath,
                                                filter='All files (*.*)')[0])
    elif Mode == 1:
        FilePaths = (QFileDialog.getOpenFileNames(ParentWidget, caption='Escolha os arquivos',
                                                directory=BasePath,
                                                filter=Filter)[0])
    elif Mode == 2:
        FilePaths = (QFileDialog.getExistingDirectory(ParentWidget, caption='Escolha a pasta',
                                                directory=BasePath))
    
    ParentWidget.MainWidget.FilePaths = FilePaths
    ParentWidget.InitializeVideo()
    
    

  
  
