from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class BotaoLado():
    def __init__(self):
        self.button = QPushButton("IMPORTOUUUUU!")
        self.button.setFixedSize(100,100)
        self.button.setCheckable(True)
    def GetButton(self):
        return self.button