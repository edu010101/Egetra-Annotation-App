from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem

def AddWidgetInLayout(Layout, Widget):
    Layout.addWidget(Widget)

def AddLayoutInLayout(LayoutFather, LayoutSon):
    LayoutFather.addLayout(LayoutSon)   

def AddSpacerInLayout(Layout, Spacer):
    Layout.addSpacerItem(Spacer)