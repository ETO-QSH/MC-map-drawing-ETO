
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import SmoothScrollArea, PixmapLabel, isDarkTheme, qconfig

class Ui_Xui(SmoothScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        qconfig.themeChanged.connect(self.updatePixmap)

        self.setStyleSheet("""
                    SmoothScrollArea {
                        border: 0px solid #888;
                        border-radius: 0px;
                        padding: 0px;
                        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                          stop: 0 #fff, stop: 0.5 #eee, stop: 1 #fff);
                    }
                """)

        self.label = PixmapLabel(self)
        self.pixmap_light = QPixmap(r'help\help_write.jpeg')
        self.pixmap_dark = QPixmap(r'help\help_black.jpeg')
        self.updatePixmap()
        self.setWidget(self.label)


    def updatePixmap(self):
        self.pixmap = self.pixmap_dark if isDarkTheme() else self.pixmap_light
        pixmapWidth = self.width()
        pixmapHeight = int(self.pixmap.height() * pixmapWidth / self.pixmap.width())
        scaledPixmap = self.pixmap.scaled(pixmapWidth, pixmapHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaledPixmap)

    def resizeEvent(self, event):
        super().resizeEvent(event)   # 调用基类的resizeEvent以保持其他功能正常
        pixmapWidth = self.width() + 1
        pixmapHeight = int(self.pixmap.height() * pixmapWidth / self.pixmap.width())
        scaledPixmap = self.pixmap.scaled(pixmapWidth, pixmapHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaledPixmap)

class UI_Xui(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def setupUi(self, parent):

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)

        # 创建Ui_Xui实例
        self.pic = Ui_Xui(self)
        self.hBoxLayout.addWidget(self.pic)

        # 将容器设置为UI_Xui的布局
        self.setLayout(self.hBoxLayout)
