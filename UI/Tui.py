# -*- coding: utf-8 -*-
import ast
import os
import re
import shutil
import subprocess
from collections import Counter
from multiprocessing import Pool


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QObject, pyqtSignal, QThread
from PyQt5.QtGui import QFont, QPixmap

from ETO.settings.config import cfg
from qfluentwidgets import qconfig, InfoBar, InfoBarPosition
from ETO.Mui import ScrollableMovableGridPixmapWidget
from ETO.Nui import DIDshow

names = locals()

class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, source_folder, target_folder):
        super().__init__()
        self.source_folder = source_folder
        self.target_folder = target_folder

    def run(self):
        # 获取所有PNG文件
        files = [os.path.join(self.source_folder, f) for f in os.listdir(self.source_folder) if f.lower().endswith('.png')]
        # 创建进程池并处理文件
        with Pool(processes=os.cpu_count()) as pool:
            pool.map(self.process_file, files)
        # 通知GUI任务完成
        self.finished.emit()

    @staticmethod
    def process_file(source_file):
        # 构建目标文件路径
        target_file = source_file.replace('spliting', 'split')
        subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\CIEDE2000.exe', '-i', source_file, '-o', target_file, '-l', './src/colorList.txt', '-n', '4'], shell=True)


class Worker2(QObject):
    finished2 = pyqtSignal()

    def __init__(self, itemList, palette, file):
        super().__init__()
        self.itemList = itemList
        self.palette = palette
        self.file = file

    def run(self):
        cmds = []
        for item in self.itemList:
            if item["parent"] == 'RAD':
                rad = item["Slider"].split(',')
                child = ['random', ','.join(rad[0:2]), ','.join(rad[2:4]), ','.join(rad[4:6])]
                print('flag provided but not defined: -seed')
                # [child.append(i) for i in ['--seed', item["Seed"]]]
            if item["parent"] == 'BMD':
                child = ['bayer', item["Tree"]]
            if item["parent"] == 'ODM':
                child = ['odm', item["List"]]
            if item["parent"] == 'EDM':
                child = ['edm', item["List"]]
                print('flag provided but not defined: -serpentine')
                # [child.insert(0, '--serpentine') if item["Snakes"] == 'True' else 0]

            cmd = [r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\didder.exe', '--in', self.file, '--out', './data/didder/{}.png'.format(item["Flag"]), '--strength', item["Strength"]+'%', '--palette', self.palette]

            [cmd.append(it) for it in child]

            cmds.append(cmd)

        print(cmds)

        # 创建进程池并处理文件
        with Pool(processes=os.cpu_count()) as pool:
            pool.map(self.turn_img, cmds)
        # 通知GUI任务完成
        self.finished2.emit()

    @staticmethod
    def turn_img(cmd):
        subprocess.run(cmd, shell=True)


class Ui_Tui(object):

    def setupUi(self, Tui):
        Tui.setObjectName("Tui")
        Tui.resize(1060, 659)
        self.bction_button = PushButton("Next")
        self.widget = QtWidgets.QWidget(Tui)
        self.widget.setGeometry(QtCore.QRect(79, 60, 800, 576))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.TitleLabel = TitleLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setTabletTracking(False)
        self.TitleLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout_2.addWidget(self.TitleLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(self.widget)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(256, 512))
        self.SimpleCardWidget.setMaximumSize(QtCore.QSize(256, 512))
        self.SimpleCardWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.SimpleCardWidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.TreeWidget = TreeWidget(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TreeWidget.setFont(font)
        self.TreeWidget.setStyleSheet("QTreeView {\n"
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
"    color: rgb(96, 96, 96);\n"
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
"}")
        self.TreeWidget.setAutoScrollMargin(0)
        self.TreeWidget.setDragEnabled(False)
        self.TreeWidget.setAutoExpandDelay(-1)
        self.TreeWidget.setIndentation(16)
        self.TreeWidget.setRootIsDecorated(False)
        self.TreeWidget.setUniformRowHeights(False)
        self.TreeWidget.setAnimated(True)
        self.TreeWidget.setAllColumnsShowFocus(False)
        self.TreeWidget.setWordWrap(True)
        self.TreeWidget.setHeaderHidden(False)
        self.TreeWidget.setColumnCount(1)
        self.TreeWidget.setObjectName("TreeWidget")
        self.TreeWidget.headerItem().setText(0, "任务列表")

        item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        self.TreeWidget.header().setVisible(True)
        self.TreeWidget.header().setCascadingSectionResizes(False)
        self.TreeWidget.header().setHighlightSections(False)
        self.gridLayout_6.addWidget(self.TreeWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.SimpleCardWidget)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.SimpleCardWidget_2 = SimpleCardWidget(self.widget)
        self.SimpleCardWidget_2.setMinimumSize(QtCore.QSize(512, 512))
        self.SimpleCardWidget_2.setMaximumSize(QtCore.QSize(512, 512))
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.SimpleCardWidget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.PushButton = PushButton(self.SimpleCardWidget_2)
        self.PushButton.setMinimumSize(QtCore.QSize(192, 64))
        self.PushButton.setMaximumSize(QtCore.QSize(192, 64))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton.setFont(font)
        self.PushButton.setObjectName("PushButton")
        self.PushButton.clicked.connect(self.on_pushButton_clicked)
        self.gridLayout.addWidget(self.PushButton, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.SimpleCardWidget_2, 2, 2, 1, 1)
        self.ImageLabel = ImageLabel(self.widget)
        self.ImageLabel.setMinimumSize(QtCore.QSize(16, 16))
        self.ImageLabel.setMaximumSize(QtCore.QSize(16, 16))
        self.ImageLabel.setObjectName("ImageLabel")
        self.gridLayout_3.addWidget(self.ImageLabel, 2, 1, 1, 1)

        self.retranslateUi(Tui)
        QtCore.QMetaObject.connectSlotsByName(Tui)

        self.window = Tui.window

    def retranslateUi(self, Tui):
        _translate = QtCore.QCoreApplication.translate
        Tui.setWindowTitle(_translate("Tui", "Form"))
        self.TitleLabel.setText(_translate("Tui", "进行地图画转换"))
        self.TreeWidget.setSortingEnabled(False)
        __sortingEnabled = self.TreeWidget.isSortingEnabled()
        self.TreeWidget.setSortingEnabled(False)
        font_8 = QtGui.QFont('萝莉体', 8)
        font_9 = QtGui.QFont('萝莉体', 9)

        self.TreeWidget.topLevelItem(0).setText(0, _translate("Tui", "CIEDE"))
        self.TreeWidget.topLevelItem(0).child(0).setText(0, _translate("Tui", "ΔE+KT"))
        self.TreeWidget.topLevelItem(1).setText(0, _translate("Tui", "DIDDER"))
        self.TreeWidget.topLevelItem(1).child(0).setText(0, _translate("Tui", "RAD"))
        self.TreeWidget.topLevelItem(1).child(1).setText(0, _translate("Tui", "BMD"))
        self.TreeWidget.topLevelItem(1).child(2).setText(0, _translate("Tui", "ODM"))
        self.TreeWidget.topLevelItem(1).child(3).setText(0, _translate("Tui", "EDM"))

        self.TreeWidget.topLevelItem(0).setFont(0, font_9)
        self.TreeWidget.topLevelItem(0).child(0).setFont(0, font_8)
        self.TreeWidget.topLevelItem(1).setFont(0, font_9)
        self.TreeWidget.topLevelItem(1).child(0).setFont(0, font_8)
        self.TreeWidget.topLevelItem(1).child(1).setFont(0, font_8)
        self.TreeWidget.topLevelItem(1).child(2).setFont(0, font_8)
        self.TreeWidget.topLevelItem(1).child(3).setFont(0, font_8)

        self.TreeWidget.setSortingEnabled(False)
        self.PushButton.setText(_translate("Tui", "开始转换"))

        for i in range(self.TreeWidget.topLevelItemCount()):
            item = self.TreeWidget.topLevelItem(i)
            self.expandAll(item)

    def expandAll(self, item):
        item.setExpanded(True)
        for i in range(item.childCount()):
            self.expandAll(item.child(i))

    def on_pushButton_clicked(self):
        if self.window.algorithmed['RadioBoxes'] == 'RadioButton_0':
            self.createWarningInfoBar()

        elif self.window.algorithmed['RadioBoxes'] == 'RadioButton_2':
            self.PushButton.deleteLater()
            self.StateToolTip = StateToolTip(' Working . . .      ', '正在转化中，请耐心等候。。。')
            self.StateToolTip.setObjectName(u"StateToolTip")
            self.StateToolTip.setGeometry(QRect(120, 590, 256, 64))
            self.StateToolTip.setStyleSheet(re.sub(r'\*\*\*', cfg.get(cfg.ThemeColor).name(), u"StateToolTip,\n"
"ToastToolTip {\n"
"    background-color: ***;\n"
"    border: none;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    font-family: '\u841d\u8389\u4f53';\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#titleLabel {\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QLabel#contentLabel {\n"
"    font-size: 12px;\n"
"}"))
            self.gridLayout.addWidget(self.StateToolTip, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.StateToolTip.closedSignal.connect(self.on_StateToolTip_closed2)
            self.start2_processing()

        elif self.window.algorithmed['RadioBoxes'] == 'RadioButton_1':
            self.PushButton.deleteLater()

            os.makedirs('./data/spliting', exist_ok=True)
            res = subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\ImgTransform.exe', '-i', self.window.algorithmed['imageFile'].replace('/', '\\'), '-o', './data/spliting/Label', '-m', 'false', '-s', '1.0'], shell=True, capture_output=True, text=True)
            n, m = res.stdout[1:-2].split(',')

            self.StateToolTip = ScrollableMovableGridPixmapWidget(int(n)-1, int(m)-1, 480)
            self.StateToolTip.setObjectName('ScrollableMovableGridPixmapWidget')
            self.StateToolTip.setGeometry(QRect(0, 0, 480, 480))
            self.gridLayout.addWidget(self.StateToolTip, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            self.start_processing()

        # 更新布局
        self.gridLayout.update()

    def start_processing(self):
        # 创建并启动工作进程
        self.worker = Worker(source_folder="./data/spliting", target_folder="./data/split")
        self.worker.finished.connect(self.on_finished)
        self.worker.moveToThread(QThread())
        self.worker.thread().started.connect(self.worker.run)
        self.worker.thread().start()

    def start2_processing(self):
        with open('./data/colorList.txt', 'r', encoding="utf-8") as file:
            palette = " ".join(ast.literal_eval(file.read())[1:])

        self.itemList = []

        for child in range(self.TreeWidget.topLevelItemCount()):
            parent_item = self.TreeWidget.topLevelItem(child)
            for child in range(parent_item.childCount()):
                child_item = parent_item.child(child)
                for item in range(child_item.childCount()):
                    if child_item.child(item):
                        it = ast.literal_eval('{"'+child_item.child(item).text(0).replace('\n', '", "').replace(': ', '": "')+'"}')
                        it['parent'] = parent_item.child(child).text(0)
                        self.itemList.append(it)

        print(self.itemList)

        # 创建并启动工作进程
        self.worker2 = Worker2(self.itemList, palette, self.window.algorithmed['imageFile'].replace('/', '\\'))
        self.worker2.finished2.connect(self.on_StateToolTip_closed)
        self.worker2.moveToThread(QThread())
        self.worker2.thread().started.connect(self.worker2.run)
        self.worker2.thread().start()

    def on_finished(self):
        self.createSuccessInfoBar()
        shutil.rmtree('./data/spliting')
        subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\ImgTransform.exe', '-i', './data/split', '-o', './data/image/ciede.png', '-m', 'none', '-s', '1.0'], shell=True)
        shutil.rmtree('./data/split')
        os.makedirs('./data/split', exist_ok=True)

    def on_StateToolTip_closed(self):
        # 删除 StateToolTip
        self.StateToolTip.deleteLater()

        pixmap = QPixmap(self.window.algorithmed['imageFile'])
        self.pixmap_size = pixmap.size()

        # 创建 DIDshow 实例
        self.didshow = DIDshow(self.pixmap_size)
        self.gridLayout.addWidget(self.didshow, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # 更新布局
        self.gridLayout.update()

        # 连接 itemClicked 信号到槽函数
        self.TreeWidget.itemClicked.connect(self.handleTreeItemClick)

        self.createSuccessInfoBar()

    def on_StateToolTip_closed2(self):
        self.StateToolTip.deleteLater()
        self.StateToolTip = StateToolTip(' Working . . .      ', '正在转化中，请耐心等候。。。')
        self.StateToolTip.setObjectName(u"StateToolTip")
        self.StateToolTip.setGeometry(QRect(120, 590, 256, 64))
        self.StateToolTip.setStyleSheet(re.sub(r'\*\*\*', cfg.get(cfg.ThemeColor).name(), u"StateToolTip,\n"
"ToastToolTip {\n"
"    background-color: ***;\n"
"    border: none;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    font-family: '\u841d\u8389\u4f53';\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#titleLabel {\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QLabel#contentLabel {\n"
"    font-size: 12px;\n"
"}"))
        self.gridLayout.addWidget(self.StateToolTip, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.StateToolTip.closedSignal.connect(self.on_StateToolTip_closed2)

    def handleTreeItemClick(self, item):
        # 检查是否是特定的子项
        if item.parent() is not None and item.parent().parent() is not None:
            flag = int(item.text(0).split("\n")[0].split(":")[1].strip())
            self.didshow.flipView.setCurrentIndex(flag)

    def createWarningInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="前按照步骤完成前面的提交",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP_RIGHT,
            duration=2500,
            parent=self
        )

    def createSuccessInfoBar(self):
        # convenient class mothod
        self.infoBar = InfoBar.success(
            title='Success',
            content="已完成全部加载！",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=-1,
            parent=self
        )
        self.infoBar.addWidget(self.bction_button)



from qfluentwidgets import ImageLabel, PushButton, SimpleCardWidget, TitleLabel, TreeWidget, StateToolTip
