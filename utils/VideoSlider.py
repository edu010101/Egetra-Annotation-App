from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt 

def CreateVideoSlider(Widget):
    Slider = ClickerSlider(Widget)
    Slider.setOrientation(Qt.Horizontal)
    Slider.setStyleSheet(u"QLabel{background-color:rgb(0,0,0)}")
    
    return Slider

#Credits for eyllanesc, thanks bro, for real.
#His StackOverflow account -> https://stackoverflow.com/users/6622587/eyllanesc

class ClickerSlider(QtWidgets.QSlider):
    def mouseReleaseEvent(self, event):
        super(ClickerSlider, self).mouseReleaseEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)
            self.Video.FrameIdTarget = int(val)
            print(val)
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

    def start(self, Video):
        self.Video = Video



