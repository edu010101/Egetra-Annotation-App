from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QSlider

def CreateVideoSlider(Widget):
    Slider = ClickerSlider(Widget)
    Slider.setOrientation(Qt.Horizontal)
    Slider.setStyleSheet(u"QLabel{background-color:rgb(0,0,0)}")
    Slider.setTickPosition(QSlider.TicksRight)
    Slider.setTickInterval(20)
    
    return Slider

#Credits for eyllanesc, thanks bro, for real.
#His StackOverflow account -> https://stackoverflow.com/users/6622587/eyllanesc

class ClickerSlider(QtWidgets.QSlider):
    def mousePressEvent(self, event):
        super(ClickerSlider, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)

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



