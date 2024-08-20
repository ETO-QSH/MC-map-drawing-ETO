import copy
import os
import random
import time
from functools import partial
from typing import Union

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl, QSize, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QMovie
from PyQt5.QtWidgets import QSizePolicy, QWidget, QHBoxLayout, QLabel, QMainWindow
from ETO.settings.config import cfg

from qfluentwidgets.components.widgets.teaching_tip import ImagePosition

from qfluentwidgets import TeachingTipTailPosition, FlyoutViewBase, TeachingTip, TeachingTipView, \
    FluentIconBase, setTheme, Theme, PushButton, PixmapLabel, InfoBar, InfoBarPosition

names = locals()

class MovableWidget(QtWidgets.QWidget):
    newFileDetected = pyqtSignal(str)

    def __init__(self, n, m, s, folder_path, scrollable_widget, parent=None):
        super().__init__(parent)
        self.folder_path = folder_path
        self.lastMousePressTime = None  # 用于记录上一次鼠标左键按下的时间
        self.scrollable_widget = scrollable_widget
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.currentTip = None  # 用于跟踪当前显示的TopTip
        self.s = s // max(m, n)
        self.movielst = []
        self.filelst = []
        self.lst = []
        self.S = s

        # 创建一个定时器，用于定期检查文件夹
        self.checkTimer = QTimer(self)
        self.checkTimer.setInterval(1000)
        self.checkTimer.timeout.connect(partial(self.checkForNewFiles, folder_path=self.folder_path))
        self.checkTimer.start()

        image_paths = r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\loading\{}'.format({'动画式一': "load_0.gif", '动画式二': "load_1.gif", '动画式三': "load_2.gif"}[cfg.get(cfg.loadingStyle)])

        # 创建并添加PixmapLabel控件，并为每个PixmapLabel设置图片
        for i in range(n):
            for j in range(m):
                #names['Label_%s_%s' % (i, j)] = PixmapLabel(self)
                #names['Label_%s_%s' % (i, j)].setFixedSize(self.s, self.s)
                #names['Label_%s_%s' % (i, j)].setPixmap(QtGui.QPixmap(image_paths[i * m + j]))
                #names['Label_%s_%s' % (i, j)].mouseReleaseEvent = lambda event, label=names['Label_%s_%s' % (i, j)]: self.onLabelClicked(label, event)
                #self.gridLayout.addWidget(names['Label_%s_%s' % (i, j)], i, j)
                #self.lst.append(names['Label_%s_%s' % (i, j)])

                names['Label_%s_%s' % (i, j)] = QtWidgets.QLabel(self)
                names['Label_%s_%s' % (i, j)].setFixedSize(self.s, self.s)
                movie = QMovie(image_paths)
                names['Label_%s_%s' % (i, j)].setMovie(movie)
                movie.setScaledSize(PyQt5.QtCore.QSize(self.s, self.s))
                movie.setSpeed(10000)
                self.movielst.append(movie)
                self.gridLayout.addWidget(names['Label_%s_%s' % (i, j)], i, j)
                self.lst.append(names['Label_%s_%s' % (i, j)])

        for label in self.lst:
            label.setFixedSize(self.s, self.s)
            label.movie().jumpToFrame(random.randint(0, label.movie().frameCount() - 1))

        # 初始化移动功能的变量
        self.mousePressPos = None
        self.mousePressGlobalPos = None
        self.gridSize = (n, m)

        # 保存初始位置
        self.initialPos = self.pos()

    def checkForNewFiles(self, folder_path):
        for file in os.listdir(folder_path):
            if file not in self.filelst:
                if file.startswith('Label_') and file.endswith('.png'):
                    self.filelst.append(file)
                    # 如果文件是新出现的，发出信号
                    self.newFileDetected.emit(os.path.join(folder_path, file))

    def handleNewFile(self, file_path):
        try:
            _, i, j = os.path.splitext(os.path.split(file_path)[1])[0].split('_')
            if i.isdigit() and j.isdigit():

                # 检查旧标签是否存在，并从布局和列表中移除
                if 'Label_%s_%s' % (i, j) in names:
                    old_label = names['Label_%s_%s' % (i, j)]
                    self.gridLayout.removeWidget(old_label)
                    old_label.setParent(None)
                    index = self.lst.index(old_label)
                    self.lst.remove(old_label)
                    del names['Label_%s_%s' % (i, j)]

                    # 创建新的PixmapLabel控件
                    names['Label_%s_%s' % (i, j)] = PixmapLabel(self)
                    names['Label_%s_%s' % (i, j)].setFixedSize(self.s, self.s)
                    names['Label_%s_%s' % (i, j)].setPixmap(QtGui.QPixmap(file_path))
                    names['Label_%s_%s' % (i, j)].mouseReleaseEvent = lambda event, label=names['Label_%s_%s' % (i, j)]: self.onLabelClicked(label, event)
                    self.gridLayout.addWidget(names['Label_%s_%s' % (i, j)], int(i), int(j))
                    self.lst.insert(index, names['Label_%s_%s' % (i, j)])

                    for label in self.lst:
                        label.setFixedSize(self.s, self.s)

            else:
                raise 'Error: is not digit'

        except Exception as e:
            print(e)

    # 连接信号到槽函数
    def connectNewFileSignal(self):
        self.newFileDetected.connect(self.handleNewFile)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        new_size = QSize(self.s, self.s)
        for label in self.lst:
            movie = label.movie()
            if movie:
                movie.setScaledSize(new_size)
                movie.start()

    def onLabelClicked(self, label, event):
        if event.button() == Qt.LeftButton:
            if self.lastMousePressTime != None:
                nowTime = time.time()
                if nowTime - self.lastMousePressTime < 0.5:

                    index = self.lst.index(label)
                    i = index // self.gridSize[1]
                    j = index % self.gridSize[1]

                    if self.currentTip != None:
                        self.currentTip.close()
                        self.currentTip = None

                    def currentTipNone():
                        self.currentTip = None

                    # 创建CustomTeachingTip实例
                    title = 'pic_%s_%s' % (i, j)
                    view = CustomTeachingTipView(
                        title=title,
                        content="",
                        image=label.pixmap(),  # 使用PixmapLabel的图片
                        isClosable=True,
                        tailPosition=TeachingTipTailPosition.BOTTOM,
                    )

                    # 显示TopTip
                    w = CustomTeachingTip.make(
                        target=label,
                        view=view,
                        duration=-1,
                        tailPosition=TeachingTipTailPosition.BOTTOM,
                        parent=self
                    )
                    view.closed.connect(w.close)
                    view.closed.connect(currentTipNone)

                    # 更新当前显示的TopTip
                    self.currentTip = w

                    # 显示TopTip
                    w.show()

                self.lastMousePressTime = None

            else:
                self.lastMousePressTime = time.time()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.mousePressPos = event.pos()
            self.mousePressGlobalPos = event.globalPos()
            event.accept()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.mousePressPos is not None:
            if event.buttons() & Qt.RightButton:
                delta = event.pos() - self.mousePressPos
                newX = self.initialPos.x() + delta.x()
                newY = self.initialPos.y() + delta.y()

                # 设置滑块位置
                self.scrollable_widget.setScrollPosition(newX, newY)

                event.accept()
            else:
                self.mousePressPos = None
                event.ignore()
        else:
            super().mouseMoveEvent(event)

    def zoomLabels(self, factor, mousePos):
        if self.s * factor * self.gridSize[0] <= self.S and self.s * factor * self.gridSize[1] <= self.S:
            factor = min(self.S / (self.s * self.gridSize[0]), self.S / (self.s * self.gridSize[1]))

        for label in self.lst:
            label.setFixedSize(int(self.s * factor), int(self.s * factor))

        scrollPos = self.scrollable_widget.getScrollPosition()

        newCenterX = (mousePos.x() + scrollPos[0]) * (1 - factor)
        newCenterY = (mousePos.y() + scrollPos[1]) * (1 - factor)

        self.scrollable_widget.setScrollPosition(int(newCenterX), int(newCenterY))

        self.s = int(self.s * factor)

class ScrollableMovableGridPixmapWidget(QtWidgets.QWidget):
    def __init__(self, n, m, s, parent=None):
        super().__init__(parent)
        self.movableWidget = MovableWidget(n, m, s, 'D:\\Work Files\\PyQt-Fluent-Widgets-exploit\\ETO\\data', self)
        self.movableWidget.connectNewFileSignal()
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.movableWidget)
        self.scrollArea.setLineWidth(0)
        self.S = s

        # 禁用 QScrollArea 的默认滚动事件
        self.scrollArea.wheelEvent = lambda event: event.ignore()

        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.scrollArea)
        self.setLayout(layout)

        if n == m:
            self.scrollArea.setMinimumSize(QtCore.QSize(self.S, self.S))
            self.scrollArea.setMaximumSize(QtCore.QSize(self.S, self.S))
        elif m > n:
            self.scrollArea.setMinimumSize(QtCore.QSize(self.S, int(self.S*(n/m))))
            self.scrollArea.setMaximumSize(QtCore.QSize(self.S, int(self.S*(n/m))))
        elif m < n:
            self.scrollArea.setMinimumSize(QtCore.QSize(int(self.S*(m/n)), self.S))
            self.scrollArea.setMaximumSize(QtCore.QSize(int(self.S*(m/n)), self.S))


    def setScrollPosition(self, horizontal, vertical):
        currentHorizontal = self.scrollArea.horizontalScrollBar().value()
        currentVertical = self.scrollArea.verticalScrollBar().value()

        self.scrollArea.horizontalScrollBar().setValue(currentHorizontal - horizontal)
        self.scrollArea.verticalScrollBar().setValue(currentVertical - vertical)

    def getScrollPosition(self):
        currentHorizontal = self.scrollArea.horizontalScrollBar().value()
        currentVertical = self.scrollArea.verticalScrollBar().value()

        return currentHorizontal, currentVertical

    def wheelEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                self.zoomIn(event)
            elif event.angleDelta().y() < 0:
                self.zoomOut(event)

    def zoomIn(self, event):
        mousePos = self.scrollArea.mapFromGlobal(event.globalPos())
        self.movableWidget.zoomLabels(9/8, mousePos)

    def zoomOut(self, event):
        mousePos = self.scrollArea.mapFromGlobal(event.globalPos())
        self.movableWidget.zoomLabels(8/9, mousePos)

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Success',
            content="已完成全部加载！",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=-1,
            parent=self
        )


class CustomTeachingTipView(TeachingTipView):
    def __init__(self, title: str, content: str, icon: Union[FluentIconBase, QIcon, str] = None,
                 image: Union[str, QPixmap, QImage] = None, isClosable=True, tailPosition=TeachingTipTailPosition.BOTTOM,
                 parent=None):
        super().__init__(title, content, icon, image, isClosable, tailPosition, parent)
        # 设置图片标签的大小策略为固定，防止图片被缩放
        if hasattr(self, 'imageLabel'):
            self.imageLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def _adjustImage(self):
        # 确保图片大小与窗口大小一致
        if hasattr(self, 'imageLabel'):
            self.imageLabel.setScaledContents(False)
            # 根据图片位置调整图片大小
            if self.manager.imagePosition() in [ImagePosition.TOP, ImagePosition.BOTTOM]:
                self.imageLabel.setPixmap(self.imageLabel.pixmap().scaledToHeight(self.imageLabel.height(), Qt.SmoothTransformation))
            elif self.manager.imagePosition() in [ImagePosition.LEFT, ImagePosition.RIGHT]:
                self.imageLabel.setPixmap(self.imageLabel.pixmap().scaledToWidth(self.imageLabel.width(), Qt.SmoothTransformation))


class CustomTeachingTip(TeachingTip):
    def __init__(self, view: FlyoutViewBase, target: QWidget, duration=1000,
                 tailPosition=TeachingTipTailPosition.BOTTOM, parent=None, isDeleteOnClose=True):
        super().__init__(view, target, duration, tailPosition, parent, isDeleteOnClose)
        # 设置图片标签的大小策略为固定，防止图片被缩放
        if hasattr(self, 'bubble') and hasattr(self.bubble, 'view') and hasattr(self.bubble.view, 'imageLabel'):
            self.bubble.view.imageLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def _adjustImage(self):
        # 确保图片大小与窗口大小一致
        if hasattr(self, 'bubble') and hasattr(self.bubble, 'view') and hasattr(self.bubble.view, 'imageLabel'):
            self.bubble.view.imageLabel.setScaledContents(False)
            # 根据图片位置调整图片大小
            if self.manager.imagePosition() in [ImagePosition.TOP, ImagePosition.BOTTOM]:
                self.bubble.view.imageLabel.setPixmap(self.bubble.view.imageLabel.pixmap().scaledToHeight(self.bubble.view.imageLabel.height(), Qt.SmoothTransformation))
            elif self.manager.imagePosition() in [ImagePosition.LEFT, ImagePosition.RIGHT]:
                self.bubble.view.imageLabel.setPixmap(self.bubble.view.imageLabel.pixmap().scaledToWidth(self.bubble.view.imageLabel.width(), Qt.SmoothTransformation))

