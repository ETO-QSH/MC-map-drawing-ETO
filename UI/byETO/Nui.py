# coding:utf-8

from pathlib import Path

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from qfluentwidgets import HorizontalPipsPager, HorizontalFlipView


class DIDshow(QWidget):

    def __init__(self, size, path, how):
        super().__init__()

        self.flipView = HorizontalFlipView(self)
        self.pager = HorizontalPipsPager(self)

        # change aspect ratio mode
        self.flipView.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)

        if max(size.width(), size.height()) < how:
            dpi = how / max(size.width(), size.height())
            size = QSize(int(size.width() * dpi), int(size.height() * dpi))

        # adjust view size
        self.flipView.setItemSize(size)
        self.flipView.setFixedSize(size)

        # add images
        self.flipView.addImages([str(i) for i in Path(path).glob('*')])
        self.pager.setPageNumber(self.flipView.count())

        self.pager.currentIndexChanged.connect(self.flipView.setCurrentIndex)
        self.flipView.currentIndexChanged.connect(self.pager.setCurrentIndex)

        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self.flipView, 0, Qt.AlignCenter)
        self.layout().addWidget(self.pager, 0, Qt.AlignCenter)
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setSpacing(16)
        self.resize(512, 512)
