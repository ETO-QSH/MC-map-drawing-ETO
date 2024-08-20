# coding:utf-8
import sys
from pathlib import Path

from PyQt5.QtCore import QModelIndex, Qt, QRect, QSize
from PyQt5.QtGui import QIcon, QPainter, QFont, QColor
from PyQt5.QtWidgets import QApplication, QStyleOptionViewItem, QWidget, QHBoxLayout, QVBoxLayout, QListWidget

from qfluentwidgets import (FlipImageDelegate, setTheme, Theme, HorizontalPipsPager, HorizontalFlipView,
                            VerticalFlipView, getFont, InfoBar, InfoBarPosition)


class DIDshow(QWidget):

    def __init__(self):
        super().__init__()
        #setTheme(Theme.DARK)
        #self.setStyleSheet('Demo{background:rgb(32,32,32)}')

        self.flipView = HorizontalFlipView(self)
        self.pager = HorizontalPipsPager(self)

        # change aspect ratio mode
        self.flipView.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)

        # adjust view size
        self.flipView.setItemSize(QSize(512, 512))
        self.flipView.setFixedSize(QSize(341, 512))

        # add images
        self.flipView.addImages([str(i) for i in Path('./test').glob('*')])
        self.pager.setPageNumber(self.flipView.count())

        self.pager.currentIndexChanged.connect(self.flipView.setCurrentIndex)
        self.flipView.currentIndexChanged.connect(self.pager.setCurrentIndex)

        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self.flipView, 0, Qt.AlignCenter)
        self.layout().addWidget(self.pager, 0, Qt.AlignCenter)
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setSpacing(16)
        self.resize(512, 512)
