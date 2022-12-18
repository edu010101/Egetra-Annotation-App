from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem
from PyQt5 import QtCore
def AddWidgetInLayout(Layout, Widget, Alignment=QtCore.Qt.AlignTop):
    Layout.addWidget(Widget, alignment=Alignment)

def AddLayoutInLayout(LayoutFather, LayoutSon):
    LayoutFather.addLayout(LayoutSon)   

def AddSpacerInLayout(Layout, Spacer):
    Layout.addSpacerItem(Spacer)