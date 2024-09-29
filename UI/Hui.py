# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime
from enum import Enum
from pathlib import Path
import nbtlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QStackedWidget, QLabel, QHBoxLayout, QFrame, QFileDialog

from qfluentwidgets import Theme, StyleSheetBase

from ETO.Mui import ScrollableMovableGridPixmapWidget
from ETO.Nui import DIDshow

from ETO.settings.config import cfg

class Ui_Pui(object):
    def setupUi(self, Pui):
        Pui.setObjectName("Pui")
        Pui.resize(420, 420)

        self.gridLayoutP = QtWidgets.QGridLayout(Pui)
        self.gridLayoutP.setObjectName("gridLayoutP")

        numbers = [list(map(int, item.split('.')[0].split('_')[1:])) for item in [item for item in os.listdir('./data/split/') if os.path.isfile(os.path.join('./data/split/', item))]]

        self.StateToolTip = ScrollableMovableGridPixmapWidget(max(numbers, key=lambda x: x[0])[0], max(numbers, key=lambda x: x[1])[1], 420, False)
        self.StateToolTip.setObjectName('ScrollableMovableGridPixmapWidget')
        self.StateToolTip.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.StateToolTip.setGeometry(QRect(0, 0, 420, 420))

        self.gridLayoutP.addWidget(self.StateToolTip, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.retranslateUi(Pui)
        QtCore.QMetaObject.connectSlotsByName(Pui)

    def retranslateUi(self, Pui):
        _translate = QtCore.QCoreApplication.translate
        Pui.setWindowTitle(_translate("Pui", "Form"))


class Ui_Qui(object):
    def setupUi(self, Qui):
        Qui.setObjectName("Qui")
        Qui.resize(450, 450)

        self.gridLayoutQ = QtWidgets.QGridLayout(Qui)
        self.gridLayoutQ.setObjectName("gridLayoutQ")

        pixmap = QPixmap([str(i) for i in Path('./data/image').glob('*')][0])
        width, height= pixmap.size().width(), pixmap.size().height()

        max_size, min_size = max(width, height), min(width, height)
        dpi_size = min_size / max_size
        size = QSize(420, int(dpi_size * 420)) if max_size == width else QSize(int(dpi_size * 420), 420)

        # 创建 DIDshow 实例
        self.didshow = DIDshow(size, './data/image', 420)
        self.didshow.setObjectName('DIDshow')
        self.gridLayoutQ.addWidget(self.didshow, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.retranslateUi(Qui)
        QtCore.QMetaObject.connectSlotsByName(Qui)

    def retranslateUi(self, Qui):
        _translate = QtCore.QCoreApplication.translate
        Qui.setWindowTitle(_translate("Qui", "Form"))


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


# 定义 StyleSheet 类
class StyleSheet(StyleSheetBase, Enum):
    WINDOW = "window"
    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"qss/{theme.value.lower()}/{self.value}.qss"


class AHui(Ui_Pui, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ui_hui = parent

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

class BHui(Ui_Qui, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ui_hui = parent

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)


class CHui(Ui_Qui, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ui_hui = parent

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)


class Ui_Hui(object):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.stackedWidget = QStackedWidget()
        self.segmentedWidget = SegmentedWidget()

        segmentedWidget_styleSheet = '''
        PivotItem {
            padding: 10px 12px;
            color: white;
            background-color: transparent;
            border: none;
            outline: none;
        }
        PivotItem[isSelected=true]:hover {
            color: rgba(255, 255, 255, 0.63);
        }
        PivotItem[isSelected=true]:pressed {
            color: rgba(255, 255, 255, 0.53);
        }
        PivotItem[isSelected=false]:pressed {
            color: rgba(255, 255, 255, 0.75);
        }
        PivotItem[hasIcon=false] {
            padding-left: 12px;
            padding-right: 12px;
        }
        PivotItem[hasIcon=true] {
            padding-left: 36px;
            padding-right: 12px;
        }
        Pivot {
            border: none;
            background-color: transparent;
        }
        #view {
            background-color: transparent;
        }
        SegmentedToolItem {
            padding: 5px 9px 6px 8px;
        }
        SegmentedWidget,
        SegmentedToolWidget {
            background-color: rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
        }
        SegmentedItem[isSelected=false], SegmentedToolItem[isSelected=false] {
            padding-top: 3px;
            padding-bottom: 3px;
            background-color: transparent;
            border: none;
            border-radius: 6px;
            margin: 3px 2px;
        }
        SegmentedItem[isSelected=false]:hover,
        SegmentedToolItem[isSelected=false]:hover {
            background-color: rgba(255, 255, 255, 9);
        }
        SegmentedItem[isSelected=false]:pressed,
        SegmentedToolItem[isSelected=false]:pressed {
            background-color: rgba(255, 255, 255, 6);
            margin: 3px 4px 3px 4px;
        }
        SegmentedItem[isSelected=true],
        SegmentedToolItem[isSelected=true] {
            padding-top: 6px;
            padding-bottom: 6px;
            margin: 0px;
            color: white;
            background-color: transparent;
        }
        QPushButton { font-family: '萝莉体'; font-size: 12px; }'''

        self.segmentedWidget.setStyleSheet(segmentedWidget_styleSheet)

        self.infoBarInstance = None  # 用于存储弹窗实例的引用

    def addSubInterface(self, widget: QLabel, objectName: str, text: str):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)

        # 使用全局唯一的 objectName 作为路由键
        self.segmentedWidget.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def onCurrentIndexChanged(self, index):
        print('index', index)
        widget = self.stackedWidget.widget(index)
        self.segmentedWidget.setCurrentItem(widget.objectName())

    def setupUi(self, Hui):
        Hui.setObjectName("Hui")
        Hui.resize(918, 678)

        self.layoutWidget = QtWidgets.QWidget(Hui)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 60, 820, 563))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.SimpleCardWidget_2 = SimpleCardWidget(self.layoutWidget)
        self.SimpleCardWidget_2.setMinimumSize(QtCore.QSize(450, 450))
        self.SimpleCardWidget_2.setMaximumSize(QtCore.QSize(450, 450))
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.SimpleCardWidget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.gridLayout_7.addWidget(self.SimpleCardWidget_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.segmentedWidget.setMinimumSize(QtCore.QSize(188, 31))
        self.segmentedWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.segmentedWidget.setObjectName("segmentedWidgetH")
        self.gridLayout_7.addWidget(self.segmentedWidget, 0, 0, 1, 1)

        self.stackedWidget.setObjectName("stackedWidgetH")
        self.stackedWidget.setMinimumSize(QtCore.QSize(450, 450))
        self.stackedWidget.setMaximumSize(QtCore.QSize(450, 450))
        self.gridLayout_7.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_7, 2, 0, 2, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_5.addItem(spacerItem, 1, 1, 1, 1)

        self.TitleLabel = TitleLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setTabletTracking(False)
        self.TitleLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TitleLabel.setObjectName("TitleLabel")

        self.gridLayout_5.addWidget(self.TitleLabel, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.SimpleCardWidget = SimpleCardWidget(self.layoutWidget)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(360, 490))
        self.SimpleCardWidget.setMaximumSize(QtCore.QSize(360, 490))
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.SimpleCardWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.VerticalSeparator_2 = VerticalSeparator(self.SimpleCardWidget)
        self.VerticalSeparator_2.setMinimumSize(QtCore.QSize(5, 0))
        self.VerticalSeparator_2.setMaximumSize(QtCore.QSize(5, 16777215))
        self.VerticalSeparator_2.setObjectName("VerticalSeparator_2")

        self.gridLayout_3.addWidget(self.VerticalSeparator_2, 1, 2, 1, 1)

        self.VerticalSeparator = VerticalSeparator(self.SimpleCardWidget)
        self.VerticalSeparator.setMinimumSize(QtCore.QSize(5, 0))
        self.VerticalSeparator.setMaximumSize(QtCore.QSize(5, 16777215))
        self.VerticalSeparator.setObjectName("VerticalSeparator")

        self.gridLayout_3.addWidget(self.VerticalSeparator, 1, 0, 1, 1)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.PushButton_SF = PushButton(self.SimpleCardWidget)
        self.PushButton_SF.setMinimumSize(QtCore.QSize(300, 30))
        self.PushButton_SF.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton_SF.setFont(font)
        self.PushButton_SF.setObjectName("PushButton_SF")

        self.gridLayout_2.addWidget(self.PushButton_SF, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.PushButton_2 = PushButton(self.SimpleCardWidget)
        self.PushButton_2.setMinimumSize(QtCore.QSize(60, 30))
        self.PushButton_2.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton_2.setFont(font)
        self.PushButton_2.setObjectName("PushButton_2")
        self.PushButton_2.clicked.connect(self.openFolderSelector)

        self.gridLayout_6.addWidget(self.PushButton_2, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.SimpleCardWidget)
        self.StrongBodyLabel_2.setMinimumSize(QtCore.QSize(75, 30))
        self.StrongBodyLabel_2.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.StrongBodyLabel_2.setFont(font)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")

        self.gridLayout_6.addWidget(self.StrongBodyLabel_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.LineEdit_2 = LineEdit(self.SimpleCardWidget)
        self.LineEdit_2.setMinimumSize(QtCore.QSize(150, 30))
        self.LineEdit_2.setMaximumSize(QtCore.QSize(150, 30))
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.LineEdit_2.setReadOnly(True)
        self.LineEdit_2.textChanged.connect(self.updateList)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit_2.setFont(font)

        self.gridLayout_6.addWidget(self.LineEdit_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.HorizontalSeparator = HorizontalSeparator(self.SimpleCardWidget)
        self.HorizontalSeparator.setMinimumSize(QtCore.QSize(0, 5))
        self.HorizontalSeparator.setMaximumSize(QtCore.QSize(16777215, 5))
        self.HorizontalSeparator.setObjectName("HorizontalSeparator")
        self.gridLayout_2.addWidget(self.HorizontalSeparator, 2, 0, 1, 1)

        self.TreeWidget = TreeWidget(self.SimpleCardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TreeWidget.sizePolicy().hasHeightForWidth())
        self.TreeWidget.setSizePolicy(sizePolicy)
        self.TreeWidget.setMinimumSize(QtCore.QSize(300, 360))
        self.TreeWidget.setMaximumSize(QtCore.QSize(300, 360))

        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TreeWidget.setFont(font)
        self.TreeWidget.setStyleSheet(re.sub(r'\*\*\*', '#FFFFFF' if qconfig.theme == Theme.DARK else '#000000',
"QTreeView {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    outline: 0;\n"
"    padding-right: 5px;\n"
"    font: 12px \'萝莉体\';\n"
"    selection-background-color: transparent;\n"
"}\n"
"\n"
"QTreeView[isBorderVisible=true] {\n"
"    border: 1px solid rgba(0, 0, 0, 15);\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    padding: 4px;\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    padding-left: 20px;\n"
"    border-radius: 5px;\n"
"    /* color: black; */\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qfluentwidgets/images/tree_view/TreeViewClose_black.svg);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"    image: url(:/qfluentwidgets/images/tree_view/TreeViewOpen_black.svg);\n"
"}\n"
"\n"
"QTreeView:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"QTreeView::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: ***;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 15);\n"
"    font: 15px \'萝莉体\';\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    border-left: none;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QTreeView[isBorderVisible=true] QHeaderView::section:horizontal {\n"
"    border-top: none;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:last {\n"
"    border-right: none;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    border-top: none;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"    image: url(:/qfluentwidgets/images/table_view/Down_black.svg);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"    image: url(:/qfluentwidgets/images/table_view/Up_black.svg);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(0, 0, 0, 15);\n"
"}\n"
"\n"
"QTableCornerButton::section:pressed {\n"
"    background-color: rgba(0, 0, 0, 12);\n"
"}"))

        self.TreeWidget.setDragEnabled(False)
        self.TreeWidget.setIconSize(QSize(32, 32))
        self.TreeWidget.setAutoExpandDelay(-1)
        self.TreeWidget.setIndentation(0)
        self.TreeWidget.setRootIsDecorated(True)
        self.TreeWidget.setUniformRowHeights(False)
        self.TreeWidget.setAnimated(True)
        self.TreeWidget.setAllColumnsShowFocus(False)
        self.TreeWidget.setWordWrap(False)
        self.TreeWidget.setHeaderHidden(False)
        self.TreeWidget.setColumnCount(1)
        self.TreeWidget.setObjectName("TreeWidget")
        self.TreeWidget.headerItem().setText(0, "选择世界")

        self.TreeWidget.header().setVisible(True)
        self.TreeWidget.header().setCascadingSectionResizes(False)
        self.TreeWidget.header().setHighlightSections(False)

        self.gridLayout_2.addWidget(self.TreeWidget, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.HorizontalSeparator_3 = HorizontalSeparator(self.SimpleCardWidget)
        self.HorizontalSeparator_3.setMinimumSize(QtCore.QSize(0, 5))
        self.HorizontalSeparator_3.setMaximumSize(QtCore.QSize(16777215, 5))
        self.HorizontalSeparator_3.setObjectName("HorizontalSeparator_3")
        self.gridLayout_3.addWidget(self.HorizontalSeparator_3, 0, 1, 1, 1)

        self.HorizontalSeparator_4 = HorizontalSeparator(self.SimpleCardWidget)
        self.HorizontalSeparator_4.setMinimumSize(QtCore.QSize(0, 5))
        self.HorizontalSeparator_4.setMaximumSize(QtCore.QSize(16777215, 5))
        self.HorizontalSeparator_4.setObjectName("HorizontalSeparator_4")
        self.gridLayout_3.addWidget(self.HorizontalSeparator_4, 2, 1, 1, 1)

        self.gridLayout_5.addWidget(self.SimpleCardWidget, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(Hui)
        QtCore.QMetaObject.connectSlotsByName(Hui)

    def retranslateUi(self, Hui):
        _translate = QtCore.QCoreApplication.translate
        Hui.setWindowTitle(_translate("Hui", "Form"))
        self.TitleLabel.setText(_translate("Hui", "地图画文件生成"))
        self.PushButton_SF.setText(_translate("Hui", "生 成 map.dat 和 idcounts.dat"))
        self.PushButton_2.setText(_translate("Hui", "浏览"))
        self.StrongBodyLabel_2.setText(_translate("Hui", " 打开文件夹"))
        self.LineEdit_2.setText(_translate("Hui", cfg.get(cfg.savesFolder)))
        self.TreeWidget.setSortingEnabled(False)

    def openFolderSelector(self):
        folderPath = QFileDialog.getExistingDirectory(self, "选择文件夹", "", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if folderPath:
            self.LineEdit_2.setText(folderPath)

    def updateList(self):

        self.TreeWidget.clear()

        folders = [item for item in os.listdir(self.LineEdit_2.text()) if os.path.isdir(os.path.join(self.LineEdit_2.text(), item))]

        for folder in folders:
            file_names = ['icon.png', 'level.dat']
            directory_path = os.path.join(self.LineEdit_2.text(), folder)
            for item in os.listdir(directory_path):
                if os.path.isfile(os.path.join(directory_path, item)):
                    if item in file_names:
                        file_names.remove(item)
            if file_names:
                folders.remove(folder)

        _translate = QtCore.QCoreApplication.translate
        font_8 = QtGui.QFont('萝莉体', 8)

        for folder in folders:
            icon_0 = QtGui.QIcon()
            icon_0.addPixmap(QtGui.QPixmap(os.path.join(self.LineEdit_2.text(), folder, 'icon.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            icon_0.addPixmap(QtGui.QPixmap(os.path.join(self.LineEdit_2.text(), folder, 'icon.png')), QtGui.QIcon.Selected, QtGui.QIcon.Off)
            item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
            Data = nbtlib.load(os.path.join(self.LineEdit_2.text(), folder, 'level.dat'))["Data"]
            Str = '   "{}"  '.format(Data["LevelName"]) + '({})'.format(
                datetime.fromtimestamp(Data["LastPlayed"] // 1000)) + '\n' + '   ' + \
                  {'0': '生存模式', '1': '创造模式', '2': '冒险模式', '3': '旁观模式'}[
                      str(int(Data["GameType"]))] + '--' + \
                  ["禁止作弊" if Data["allowCommands"] == False else "允许作弊"][0] + '  版本: ' + Data["Version"][
                      "Name"] + ['b' if Data["Version"]["Snapshot"] == True else ''][0] + '({})'.format(
                int(Data["Version"]["Id"]))
            item_0.setText(0, _translate("Hui", Str))
            item_0.setIcon(0, icon_0)
            item_0.setFont(0, font_8)


from qfluentwidgets import HorizontalSeparator, LineEdit, PushButton, SegmentedWidget, SimpleCardWidget, \
    StrongBodyLabel, TitleLabel, TreeWidget, VerticalSeparator, qconfig, Theme, setFont, SubtitleLabel
