from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt 
from utils.StylesheetUtils import LoadCSS

def CreateVideoSlider(Widget, CSS):
    Slider = ClickerSlider(Widget)
    Slider.setOrientation(Qt.Horizontal)
    #Slider.setStyleSheet(u"QLabel{background-color:rgb(0,0,0)}")
    

    CSS = LoadCSS(CSS)
    Slider.setStyleSheet(CSS)
    
    return Slider

#Credits for eyllanesc, thanks bro, for real.
#His StackOverflow account -> https://stackoverflow.com/users/6622587/eyllanesc

class ClickerSlider(QtWidgets.QSlider):
    def __init__(self, ParentWidget, CSS):
        super().__init__(ParentWidget)
        self.setOrientation(Qt.Horizontal)

        CSS = LoadCSS(CSS)
        self.setStyleSheet(CSS)
        
    def mouseReleaseEvent(self, event):
        super(ClickerSlider, self).mouseReleaseEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            CurrentSliderValue = self.pixelPosToRangeValue(event.pos())
            self.setValue(CurrentSliderValue)

            self.Video.FrameIdTarget = CurrentSliderValue
            self.Video.ChangeFrameBoolean = True       

    def pixelPosToRangeValue(self, pos):
        opt = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderHandle, self)

        if self.orientation() == QtCore.Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1;
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == QtCore.Qt.Horizontal else pr.y()
        return QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin,
                                               sliderMax - sliderMin, opt.upsideDown)

    



