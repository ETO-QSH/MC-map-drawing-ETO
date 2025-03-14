
import os
import re
import ast
import shutil
import subprocess
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QObject, pyqtSignal, QThread, QSize
from PyQt5.QtGui import QPixmap

from qfluentwidgets import qconfig, InfoBar, InfoBarPosition, Theme
from ETO.byETO.Mui import ScrollableMovableGridPixmapWidget
from ETO.byETO.Nui import DIDshow

names = locals()

def find_path(filename):
    for root, dirs, files in os.walk(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))):
        for file in files:
            if file.endswith(os.path.splitext(filename)[1]) and file.startswith(os.path.splitext(filename)[0]):
                return os.path.join(root, file)
    return None

def process_file(source_file, queue):
    for i in range(3):
        try:
            target_file = source_file.replace('spliting', 'split')
            subprocess.run(
                [find_path('CIEDE2000.exe'), '-i', source_file, '-o', target_file, '-l', './src/colorList.txt', '-n', '4'],
                      shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            queue.put(f"File {source_file} processed successfully.")
            break
        except Exception as e:
            queue.put(f"Error processing file {source_file}: {str(e)}")


class ProcessManager(QThread):
    finished = pyqtSignal()

    def __init__(self, source_folder):
        super().__init__()
        self.source_folder = source_folder
        self.queue = Queue()  # 线程安全的队列

    def run(self):
        # 获取所有PNG文件
        files = [
            os.path.join(self.source_folder, f)
            for f in os.listdir(self.source_folder)
            if f.lower().endswith('.png')
        ]

        # 使用线程池提交任务
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_file, file, self.queue) for file in files]
            for future in futures:
                try:
                    future.result()  # 等待任务完成（可处理异常）
                except Exception as e:
                    print(f"Error processing file: {e}")

        # 所有任务完成后发送完成信号
        self.queue.put('finished')
        self.finished.emit()


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
                child = ['random'] + ['--seed', item["Seed"]] + [','.join(rad[0:2]), ','.join(rad[2:4]), ','.join(rad[4:6])]
            if item["parent"] == 'BMD':
                child = ['bayer', item["Tree"]]
            if item["parent"] == 'ODM':
                child = ['odm', item["List"]]
            if item["parent"] == 'EDM':
                child = ['edm'] + [['--serpentine'] if item["Snakes"] == 'True' else []][0] + [item["List"]]

            cmd = [find_path('didder.exe'), '--in', self.file, '--out', './data/didder/{}.png'.format(item["Flag"]), '--strength', item["Strength"]+'%', '--palette', self.palette]

            cmd.extend(child)
            cmds.append(cmd)

        # 创建进程池并处理文件
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            # 使用lambda传递creationflags参数
            executor.map(lambda c: self.turn_img(c), cmds)

        # 通知GUI任务完成
        self.finished2.emit()

    @staticmethod
    def turn_img(cmd):
        subprocess.run(cmd, shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)


class Ui_Tui(object):
    def setupUi(self, Tui):
        self.process_manager = ProcessManager("./data/spliting")
        self.process_manager.finished.connect(self.on_finished)
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
        self.PushButton.setObjectName("PushButtonST")
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
            self.StateToolTip.setStyleSheet(re.sub(r'\*\*\*', qconfig.themeColor.value.name(), u"StateToolTip,\n"
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
            res = subprocess.run([find_path('ImgTransform.exe'), '-i', self.window.algorithmed['imageFile'].replace('/', '\\'), '-o', './data/spliting/Label', '-m', 'false', '-s', '1.0'], shell=True, capture_output=True, text=True)
            n, m = res.stdout[1:-2].split(',')

            self.StateToolTip = ScrollableMovableGridPixmapWidget(int(n)-1, int(m)-1, 480, True)
            self.StateToolTip.setObjectName('ScrollableMovableGridPixmapWidget')
            self.StateToolTip.setStyleSheet("background-color:rgb(50, 50, 50);")
            self.StateToolTip.setGeometry(QRect(0, 0, 480, 480))
            self.gridLayout.addWidget(self.StateToolTip, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            self.start_processes()

        # 更新布局
        self.gridLayout.update()

    # def start_processing(self):
    #     # 创建并启动工作进程
    #     self.worker = Worker(source_folder="./data/spliting", target_folder="./data/split")
    #     self.worker.finished.connect(self.on_finished)
    #
    #     self.thread = QThread()
    #     self.worker.moveToThread(self.thread)
    #     self.thread.started.connect(self.worker.run)
    #     self.thread.start()

    def start_processes(self):
        self.process_manager.start()

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

        # 创建并启动工作进程
        self.worker2 = Worker2(self.itemList, palette, self.window.algorithmed['imageFile'].replace('/', '\\'))
        self.worker2.finished2.connect(self.on_StateToolTip_closed)

        self.thread2 = QThread()
        self.worker2.moveToThread(self.thread2)
        self.thread2.started.connect(self.worker2.run)
        self.thread2.start()

    def on_finished(self):
        self.createSuccessInfoBar()
        shutil.rmtree('./data/spliting')
        subprocess.run([find_path('ImgTransform.exe'), '-i', './data/split', '-o', './data/image/ciede.png', '-m', 'none', '-s', '1.0'], shell=True)
        subprocess.run([find_path('ImgTransform.exe'), '-i', self.window.algorithmed['imageFile'].replace('/', '\\'), '-o', './data/image/contrast.png', '-m', 'true', '-s', '1.0'], shell=True)

    def on_StateToolTip_closed(self):
        # 删除 StateToolTip
        self.StateToolTip.deleteLater()

        pixmap = QPixmap(self.window.algorithmed['imageFile'])
        width, height= pixmap.size().width(), pixmap.size().height()

        max_size, min_size = max(width, height), min(width, height)
        dpi_size = min_size / max_size
        size = QSize(512, int(dpi_size * 512)) if max_size == width else QSize(int(dpi_size * 512), 512)

        # 创建 DIDshow 实例
        self.didshow = DIDshow(size, './data/didder', 512)
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
        self.StateToolTip.setStyleSheet(re.sub(r'\*\*\*', qconfig.themeColor.value.name(), u"StateToolTip,\n"
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
