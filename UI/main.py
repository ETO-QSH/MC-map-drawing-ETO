# coding:utf-8

import os
import re
import ast
import sys
import json
import nbtlib
import shutil
import zipfile
import subprocess
from enum import Enum
from datetime import datetime
from multiprocessing import Pool

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSlot, QSize, QEventLoop, QTimer, pyqtSignal, QThread, QRect
from PyQt5.QtGui import QIcon, QDesktopServices, QFont
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QStackedWidget, QStackedLayout, QCheckBox, QLabel, \
    QTreeWidgetItem, QTreeWidget, QAbstractItemView, QSpacerItem, QSizePolicy, QComboBox

from collections import Counter

from ETO.settings.config import cfg
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow, NavigationAvatarWidget,
                            qrouter, SubtitleLabel, setFont, setThemeColor, theme, SplashScreen, InfoBar,
                            InfoBarPosition, PushButton, RadioButton, LineEdit, SpinBox, SegmentedWidget, TreeWidget,
                            SwitchButton, ListWidget, Slider, SimpleCardWidget, DropDownPushButton, StateToolTip,
                            Dialog, EditableComboBox)
from qfluentwidgets import FluentIcon as FIF

from ETO.Aui import Ui_Aui
from ETO.Bui import Ui_Bui
from ETO.Hui import Ui_Hui
from ETO.Tui import Ui_Tui
from ETO.Xui import UI_Xui
from ETO.Zui import Ui_Zui
from ETO.Kui import Ui_Kui, CustomSpinBox, newDropDownPushButton
from ETO.Hui import AHui, BHui, CHui
from ETO.settings.demo import UI_Yui

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from PyQt5.QtCore import pyqtSlot
from qfluentwidgets import qconfig, Theme, StyleSheetBase

from qfluentwidgets import SplashScreen

def copy_and_replace_files(source_folder, target_folder):
    for item in os.listdir(source_folder):
        source_path = os.path.join(source_folder, item)
        target_path = os.path.join(target_folder, item)
        if os.path.isfile(source_path):
            if os.path.exists(target_path):
                os.remove(target_path)
            shutil.copy2(source_path, target_path)

def create_zip_with_data_folder(zip_filename, data_folder_path):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(data_folder_path):
            for file in files:
                # 创建ZIP文件中的文件路径
                in_path = os.path.join(root, file)
                # 相对于data文件夹的路径
                out_path = os.path.relpath(in_path, os.path.join(data_folder_path, '..'))
                # 写入文件到zip
                zipf.write(in_path, out_path)

def copy_items_to_path(items_list, destination_path):
    for source_path in items_list:
        destination_full_path = os.path.join(destination_path, os.path.basename(os.path.normpath(source_path)))
        if os.path.isdir(source_path):
            shutil.copytree(source_path, destination_full_path)
        elif os.path.isfile(source_path):
            shutil.copy2(source_path, destination_full_path)
        else:
            print(f'Error: {source_path}')

def check_format(s):
    parts = s.split(';')
    for part in parts:
        if not part:
            continue
        if ':' not in part:
            return False
        try:
            number, word = part.split(':')
        except ValueError:
            return False
        try:
            num = int(number)
            if num < -64 or num > 319:
                return False
        except ValueError:
            return False
        if word == '' or not word.replace('_', '').isalpha():
            return False
    return True

def creat_BlockList_colorList(BlockList, colorList, newBlockList, newcolorList, name_list, MapMod):

    with open(BlockList, 'r', encoding="utf-8") as file:
        data = json.load(file)

    color_set = set()

    filtered_blocks = [block for block in data["BlockList"] if block["icon"].split('.')[0] in name_list]

    [color_set.add(color["color"]) for color in filtered_blocks]

    filtered_json = {"BlockList": filtered_blocks}

    with open(newBlockList, 'w', encoding="utf-8") as file:
        json.dump(filtered_json, file, indent=4)

    with open(colorList, 'r', encoding="utf-8") as file:
        data1 = ast.literal_eval(file.read())

    data2 = ["#000000", ]

    for i in range(1, 62):
        if i in color_set:
            for x in range(MapMod):
                data2.append(data1[4*(i-1)+x+1])

    with open(newcolorList, 'w', encoding="utf-8") as file:
        file.write(str(data2))


class Worker3(QObject):
    finished3 = pyqtSignal(int, int)

    def __init__(self, mode):
        super().__init__()
        self.mode = mode

    def run(self):
        cmds = []

        for item in [item for item in os.listdir('./data/split/') if os.path.isfile(os.path.join('./data/split/', item))]:
            cmds.append([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\mapKey.exe', '-i', os.path.join('./data/split/', item),
                          '-p', os.path.join('./data/pixivColor/', 'pixivColor_{}_{}.txt'.format(item.split('.')[0].split('_')[1], item.split('.')[0].split('_')[2])),
                          '-k', './data/keyValue.json', '-c', './data/colorList.txt', '-n', '4'])

        # 创建进程池并处理文件
        with Pool(processes=os.cpu_count()) as pool:
            pool.map(self.to_pixivColor, cmds)

        res = subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\mapKey.exe', '-i', os.path.join('./data/image/', [item for item in os.listdir('./data/image/') if item != 'contrast.png'][0]),
                                    '-p', './data/pixivColor.txt/', '-k', './data/keyValue.json', '-c', './data/colorList.txt', '-n', str(self.mode)], shell=True, capture_output=True, text=True)

        a, b = [int(i) for i in res.stdout[1:-2].split(',')] if (not res.stdout == '' and str(self.mode) == '3') else [0, 0]

        # 通知GUI任务完成
        self.finished3.emit(a, b)

    @staticmethod
    def to_pixivColor(cmd):
        subprocess.run(cmd, shell=True)


class Worker4(QObject):
    finished4 = pyqtSignal(int, int, int, int, str, str)

    def __init__(self, mode, saves, dirName, max_x, max_y, a, b):
        super().__init__()
        self.dirName = dirName
        self.saves = saves
        self.max_x = max_x
        self.max_y = max_y
        self.mode = mode
        self.a = a
        self.b = b

    def run(self):
        cmds = []
        try:
            Data = int(nbtlib.load(os.path.join(self.saves, self.dirName, 'data/idcounts.dat'))["data"]["map"])
        except FileNotFoundError:
            Data = -1
        for item in [item for item in os.listdir('./data/pixivColor/') if os.path.isfile(os.path.join('./data/pixivColor/', item))]:
            cmds.append([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\nbtfile.exe', '-c', os.path.join('./data/pixivColor/', item),
                          '-f', './data/world_dat/map_{}.dat'.format(Data + (int(item.split('.')[0].split('_')[1]) - 1) * self.max_x + int(item.split('.')[0].split('_')[2]))])
        cmds.append([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\nbtfile.exe', '-p', './data/world_dat/idcounts.dat', '-n', str(self.max_x * self.max_y + Data + 1)])

        # 创建进程池并处理文件
        with Pool(processes=os.cpu_count()) as pool:
            pool.map(self.to_nbtfile, cmds)
        # 通知GUI任务完成
        self.finished4.emit(self.a, self.b, self.max_x, self.max_y, self.saves, self.dirName)

    @staticmethod
    def to_nbtfile(cmd):
        subprocess.run(cmd, shell=True)


class Worker5(QObject):
    finished5 = pyqtSignal()

    def __init__(self, x, y, z, dic):
        super().__init__()
        self.x = str(x)
        self.y = str(y)
        self.z = str(z)
        self.dic = dic

        Layer = "-64:bedrock;-63:dirt;-62:dirt;-61:grass_block"

        if list(dic.keys())[0] == 'RadioButton_1':
            dic = self.dic['RadioButton_1']
            if int(self.y) > -61 and dic != 'glass':
                Layer += ';{}:{}'.format(self.y, dic)
            elif dic != 'glass' and int(self.y)+64 > 0:
                Layer = ';'.join(Layer.split(';')[:int(self.y)+63]) + ';{}:{}'.format(self.y, dic)
            else:
                Layer = '-64:glass'
            Layer = '"' + Layer + '"'
        elif list(dic.keys())[0] == 'RadioButton_2':
            Layer = '"' + self.dic['RadioButton_2'] + '"'
        self.addLayer = ['-s', '"{}"'.format(Layer)]

    def run(self):
        SuperflatEdit_cmd = [r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\SuperflatEdit.exe', '-b', './data/blockList.txt', '-w', './data/world_mca'] + self.addLayer
        subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\Forblock.exe', '-b', './data/BlockList.json',
                              '-k', './data/keyValue.json', '-o', './data/blockList.txt', '-x', self.x, '-y', self.y, '-z', self.z], shell=True)
        print(SuperflatEdit_cmd)
        subprocess.run(SuperflatEdit_cmd, shell=True)

        # 通知GUI任务完成
        self.finished5.emit()


class Widget(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Aui(Ui_Aui, QWidget):
    def __init__(self, navigationInterface, windowInstance, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.navigationInterface = navigationInterface  # 保存导航界面引用
        self.window = windowInstance  # 确保引用了 Window 实例

        # 连接按钮点击事件到槽函数
        self.ElevatedCardWidget_1.clicked.connect(self.handleButtonClicked)
        self.ElevatedCardWidget_2.clicked.connect(self.handleButtonClicked)
        self.ElevatedCardWidget_3.clicked.connect(self.handleButtonClicked)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    @pyqtSlot()
    def handleButtonClicked(self):
        # 调用 Window 类的 onButtonClicked 方法
        button = self.sender()
        buttonName = button.objectName()
        self.window.onButtonClicked(buttonName, 'Aui')
        self.parent().MapMod = {'1': 1, '2': 3, '3': 4}[buttonName.split('_')[1]]
        print('MapMod:', self.parent().MapMod)


class Bui(Ui_Bui, QWidget):
    def __init__(self, navigationInterface, windowInstance, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.navigationInterface = navigationInterface  # 保存导航界面引用
        self.window = windowInstance  # 确保引用了 Window 实例

        # 连接按钮点击事件到槽函数
        self.PushButton.clicked.connect(self.handleButtonClicked)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    def updateCheckBoxStyles(self, styleSheet_0, styleSheet_1):
        # 查找所有特定名称前缀的控件
        checkBoxes_0 = self.findChildren(QCheckBox)
        checkBoxes_1 = [self.findChildren(QWidget, "CheckBox_B" + str(i))[0] for i in range(0, 62)]
        for checkBox in checkBoxes_0:
            checkBox.setStyleSheet(styleSheet_1)
        for checkBox in checkBoxes_1:
            checkBox.setStyleSheet(styleSheet_0)

    def createWarningInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="请与上页选择地图画模式",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    @pyqtSlot()
    def handleButtonClicked(self):
        # 调用 Window 类的 onButtonClicked 方法
        button = self.sender()
        buttonName = button.objectName()

        # 查找所有 QCheckBox 控件
        nameList = []
        checkBoxes = self.findChildren(QCheckBox)
        for checkBox in checkBoxes:
            if checkBox.isChecked():
                name = checkBox.objectName()
                if 'CheckBox_B' not in name:
                    nameList.append(name)

        try:
            if self.parent().MapMod:
                creat_BlockList_colorList('./src/BlockList.json', './src/colorList.txt',
                                       './data/BlockList.json', './data/colorList.txt',
                                          nameList, self.parent().MapMod)
                print('nameList:', nameList)
                self.window.onButtonClicked(buttonName, 'Bui')
        except AttributeError:
            self.createWarningInfoBar()


class Cui(Ui_Zui, QWidget):
    # 定义一个信号
    updateUi = pyqtSignal()

    def __init__(self, navigationInterface, windowInstance, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.navigationInterface = navigationInterface  # 保存导航界面引用
        self.window = windowInstance  # 确保引用了 Window 实例

        # 连接按钮点击事件到槽函数
        self.action_button.clicked.connect(self.handleButtonClicked)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    @pyqtSlot()
    def handleButtonClicked(self):

        RadioBoxes = self.findChildren(RadioButton)
        for Radio in RadioBoxes:
            if Radio.isChecked():
                name = Radio.objectName()
                algorithmed['RadioBoxes'] = name

        LineEditBoxes = self.findChildren(LineEdit)
        for LineE in LineEditBoxes:
            if LineE.objectName() == 'LineEdit_2':
                text = LineE.text()
                if text != '':
                    algorithmed['imageFile'] = text

        SpinBoxes = self.findChildren(SpinBox)
        for SpinB in SpinBoxes:
            if SpinB.objectName() == 'SpinBox':
                val = SpinB.value()
                if 'RadioBoxes' in algorithmed and algorithmed['RadioBoxes'] == 'RadioButton_1':
                    if val != 0:
                        algorithmed['KTree'] = val
                else:
                    algorithmed['KTree'] = 0

        if len(list(algorithmed)) == 3:
            if algorithmed["RadioBoxes"] == 'RadioButton_2' and self.globalList == []:
                self.createWarningInfoBar()
            else:
                print('algorithmed + globalList', algorithmed, self.globalList)
                self.window.onButtonClicked("go_next", 'Cui')
                self.updateUi.emit()
        else:
            self.createWarningInfoBar()

    def createWarningInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="请勾选单选框 or 提交文件路径 or 保证K-T>0",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )


class Dui(Ui_Kui, QWidget):
    def __init__(self, gui_instance, parent=None, xx=0, yu=0, yd=0, zz=0, saves=None, dirName=None, windowInstance=None, navigationInterface=None):
        super().__init__(parent=parent)
        self.navigationInterface = navigationInterface  # 保存导航界面引用
        self.window = windowInstance  # 确保引用了 Window 实例
        self.gui_instance = gui_instance  # 保存 Gui 实例的引用

        self.setupUi(self, xx, yu, yd, zz)
        self.dirName = dirName
        self.saves = saves
        self.xx = xx
        self.yu = yu
        self.yd = yd
        self.zz = zz

        # 连接按钮点击事件到槽函数
        self.PushButton_K.clicked.connect(self.PushButton_K_Clicked)
        self.PushButton_SFR.clicked.connect(self.PushButton_SFR_Clicked)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    def handleButtonClicked2(self, x, y, z, dic):
        self.PushButton_K.clicked.disconnect()
        self.PushButton_SFR.clicked.disconnect()
        self.gridLayout_4.removeWidget(self.PushButton_SFR)
        self.PushButton_SFR.deleteLater()

        self.PushButton_SFR = StateToolTip(' Working . . .      ', '正在转化中，请耐心等候。。。')
        self.PushButton_SFR.setObjectName(u"StateToolTip")
        self.PushButton_SFR.setMinimumSize(QtCore.QSize(256, 54))
        self.PushButton_SFR.setMaximumSize(QtCore.QSize(256, 54))
        self.PushButton_SFR.setStyleSheet(re.sub(r'\*\*\*', cfg.get(cfg.ThemeColor).name(), u"StateToolTip,\n"
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
        self.PushButton_SFR.closedSignal.connect(self.on_StateToolTip_closed2)
        self.gridLayout_4.addWidget(self.PushButton_SFR, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout_4.update()

        self.worker5 = Worker5(x, y, z, dic)
        self.worker5.finished5.connect(self.on_finsh5)
        self.worker5.moveToThread(QThread())
        self.worker5.thread().started.connect(self.worker5.run)
        self.worker5.thread().start()

    def on_StateToolTip_closed2(self):
        self.gridLayout_4.removeWidget(self.PushButton_SFR)
        self.PushButton_SFR.deleteLater()

        self.PushButton_SFR = StateToolTip(' Working . . .      ', '正在转化中，请耐心等候。。。')
        self.PushButton_SFR.setObjectName(u"StateToolTip")
        self.PushButton_SFR.setGeometry(QRect(120, 590, 256, 64))
        self.PushButton_SFR.setStyleSheet(re.sub(r'\*\*\*', cfg.get(cfg.ThemeColor).name(), u"StateToolTip,\n"
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
        self.PushButton_SFR.closedSignal.connect(self.on_StateToolTip_closed2)
        self.gridLayout_4.addWidget(self.PushButton_SFR, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout_4.update()

    def on_finsh5(self):
        self.gui_instance.createSuccessInfoBar2()
        self.PushButton_SFR.closedSignal.disconnect()
        self.gridLayout_4.removeWidget(self.PushButton_SFR)
        self.PushButton_SFR.deleteLater()

        _translate = QtCore.QCoreApplication.translate
        self.PushButton_SFR = PushButton(self.widget)
        self.PushButton_SFR.setMinimumSize(QtCore.QSize(256, 54))
        self.PushButton_SFR.setMaximumSize(QtCore.QSize(256, 54))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton_SFR.setFont(font)
        self.PushButton_SFR.setObjectName("PushButton_SFR")
        self.PushButton_SFR.clicked.connect(self.PushButton_SFR_Clicked2)
        self.PushButton_SFR.setText(_translate("Kui", "备 份 替 换 原 存 档 文 件"))
        self.gridLayout_4.addWidget(self.PushButton_SFR, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout_4.update()

    def PushButton_SFR_Clicked2(self):
        copy_items_to_path([os.path.join(self.saves, self.dirName, 'data'), os.path.join(self.saves, self.dirName, 'region'),
                                     os.path.join(self.saves, self.dirName, 'level.dat')], './data/Backup')
        copy_and_replace_files('./data/world_dat', os.path.join(self.saves, self.dirName, 'data'))
        copy_and_replace_files('./data/world_mca', os.path.join(self.saves, self.dirName, 'region'))
        create_zip_with_data_folder(os.path.join(cfg.get(cfg.downloadFolder), '{}.zip'.format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))), './data')

        _translate = QtCore.QCoreApplication.translate
        self.PushButton_SFR.clicked.disconnect()
        self.PushButton_SFR.setText(_translate("Kui", "程 序 运 行 结 束"))

        w = MessageBox("Success", "程序运行结束，请根据文档正确载入地图数据", self.gui_instance)
        w.yesButton.setText("确 认")
        w.cancelButton.setText("打 开")

        self.set_font("萝莉体", 10, w.yesButton)

        titleLabelStyle = """
                QLabel {
                    font-family: '萝莉体';
                    font-size: 20px;
                }
                """
        w.titleLabel.setStyleSheet(titleLabelStyle)

        contentLabelStyle = """
                QLabel {
                    font-family: '萝莉体';
                    font-size: 16px;
                }
                """
        w.contentLabel.setStyleSheet(contentLabelStyle)

        cancelButtonStyle = """
                QPushButton {
                    font-family: '萝莉体';
                    font-size: 13px;
                }
                """
        w.cancelButton.setStyleSheet(cancelButtonStyle)

        print("byETO") if w.exec() else self.window.switchTo(self.window.libraryInterface)

    def set_font(self, font_name, font_size, label):
        """ 设置指定标签的字体和大小 """
        font = QFont(font_name, font_size)
        label.setFont(font)

    @pyqtSlot()
    def PushButton_SFR_Clicked(self):

        RadioName, RadioBoxes = None, self.findChildren(RadioButton)
        for Radio in RadioBoxes:
            if Radio.isChecked():
                RadioName = Radio.objectName()

        text, LineEditBoxes = '', self.findChildren(LineEdit)
        for LineE in LineEditBoxes:
            if LineE.objectName() == 'LineEdit_R':
                text = LineE.text()

        SpinB, CustomSpinBoxes = {}, self.findChildren(CustomSpinBox)
        for item in CustomSpinBoxes:
            SpinB[item.objectName()] = int(item.text().split(' ~ ')[0])

        choice, EditableComboBoxs = None, self.findChildren(EditableComboBox)
        for item in EditableComboBoxs:
            choice = item.itemData(item.currentIndex())

        with open('./data/BlockList.json', 'r', encoding="utf-8") as file:
            data = ast.literal_eval(file.read())["BlockList"]

        if RadioName is not None:
            if RadioName == 'RadioButton_1':
                if choice is not None:
                    self.handleButtonClicked2(x=SpinB['SpinBox_x'], y=SpinB['SpinBox_y']-1, z=SpinB['SpinBox_z'], dic={'RadioButton_1': choice})
                else:
                    self.createWarningInfoBar0()
            elif RadioName == 'RadioButton_2':
                if check_format(text):
                    if [t.split(':')[1] for t in text.split(';') if t.split(':')[1] not in [item["id"].split(':')[1] for item in data]] != []:
                        self.handleButtonClicked2(x=SpinB['SpinBox_x'], y=SpinB['SpinBox_y']-1, z=SpinB['SpinBox_z'], dic={'RadioButton_2': text})
                    else:
                        self.createWarningInfoBar2()
                else:
                    self.createWarningInfoBar()
        else:
            self.createWarningInfoBar1()

    @pyqtSlot()
    def PushButton_K_Clicked(self):
        self.LineEdit_R.setText("-64:bedrock;-63:dirt;-62:dirt;-61:grass_block")

    def createWarningInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="格式错误 —— 例：'-64:bedrock;-63:dirt;-62:dirt;-61:grass_block'",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createWarningInfoBar0(self):
        InfoBar.warning(
            title='Warning',
            content="请勾选单选框",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createWarningInfoBar1(self):
        InfoBar.warning(
            title='Warning',
            content="请选择背景层",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createWarningInfoBar2(self):
        InfoBar.warning(
            title='Warning',
            content="方块id错误，请填写上文存在的id",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )


class Eui(UI_Xui, QWidget):
    def __init__(self, navigationInterface, windowInstance, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.navigationInterface = navigationInterface  # 保存导航界面引用
        self.window = windowInstance  # 确保引用了 Window 实例

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)


class Fui(Ui_Tui, QWidget):
    # 定义一个信号
    updateUiH = pyqtSignal()
    def __init__(self, navigationInterface, windowInstance, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.navigationInterface = navigationInterface  # 保存导航界面引用
        self.window = windowInstance  # 确保引用了 Window 实例

        # 连接按钮点击事件到槽函数
        self.bction_button.clicked.connect(self.handleButtonClicked)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    def updateUi(self):
        # 通过 SimpleCardWidget 查找 TreeWidget
        self.SimpleCardWidget = self.findChild(SimpleCardWidget, 'SimpleCardWidget')
        if self.SimpleCardWidget:
            self.TreeWidget = self.SimpleCardWidget.findChild(TreeWidget, 'TreeWidget')
            if self.TreeWidget:
                # 清除所有项
                self.TreeWidget.clear()
                # 创建新的项
                self.createTreeItems()

    def createTreeItems(self):
        font_8 = QtGui.QFont('萝莉体', 8)
        font_9 = QtGui.QFont('萝莉体', 9)

        # 创建树的分支结构
        if self.window.algorithmed['RadioBoxes'] == 'RadioButton_1':
            item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)

        elif self.window.algorithmed['RadioBoxes'] == 'RadioButton_2':
            item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
            item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)

            sorted_data = sorted(self.window.appInterface.globalList, key=lambda x: x['QS'])
            nums = Counter(d['QS'] for d in sorted_data)

            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            for i in range(nums.get(0, 0)):
                item_2 = QtWidgets.QTreeWidgetItem(item_1)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            for i in range(nums.get(1, 0)):
                item_2 = QtWidgets.QTreeWidgetItem(item_1)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            for i in range(nums.get(2, 0)):
                item_2 = QtWidgets.QTreeWidgetItem(item_1)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            for i in range(nums.get(3, 0)):
                item_2 = QtWidgets.QTreeWidgetItem(item_1)

        _translate = QtCore.QCoreApplication.translate

        if self.window.algorithmed['RadioBoxes'] == 'RadioButton_1':
            self.TreeWidget.topLevelItem(0).setText(0, _translate("Tui", "CIEDE"))
            self.TreeWidget.topLevelItem(0).child(0).setText(0, _translate("Tui", "ΔE+KT"+'--->'+'KTree: {}'.format(self.window.algorithmed['KTree'])))

            self.TreeWidget.topLevelItem(1).setText(0, _translate("Tui", "DIDDER"))
            self.TreeWidget.topLevelItem(1).child(0).setText(0, _translate("Tui", "RAD"))
            self.TreeWidget.topLevelItem(1).child(1).setText(0, _translate("Tui", "BMD"))
            self.TreeWidget.topLevelItem(1).child(2).setText(0, _translate("Tui", "ODM"))
            self.TreeWidget.topLevelItem(1).child(3).setText(0, _translate("Tui", "EDM"))

            self.TreeWidget.topLevelItem(0).setFont(0, font_9)
            self.TreeWidget.topLevelItem(0).child(0).setFont(0, font_8)
            self.TreeWidget.topLevelItem(1).setFont(0, font_9)
            self.TreeWidget.topLevelItem(1).child(0).setFont(0, font_9)
            self.TreeWidget.topLevelItem(1).child(1).setFont(0, font_9)
            self.TreeWidget.topLevelItem(1).child(2).setFont(0, font_9)
            self.TreeWidget.topLevelItem(1).child(3).setFont(0, font_9)

        elif self.window.algorithmed['RadioBoxes'] == 'RadioButton_2':
            self.TreeWidget.topLevelItem(0).setText(0, _translate("Tui", "CIEDE"))
            self.TreeWidget.topLevelItem(1).setText(0, _translate("Tui", "DIDDER"))

            self.TreeWidget.topLevelItem(0).setFont(0, font_9)
            self.TreeWidget.topLevelItem(1).setFont(0, font_9)

            sorted_data = sorted(self.window.appInterface.globalList, key=lambda x: x['QS'])
            nums = Counter(d['QS'] for d in sorted_data)
            flag = 0

            self.TreeWidget.topLevelItem(1).child(0).setFont(0, font_8)
            self.TreeWidget.topLevelItem(1).child(0).setText(0, _translate("Tui", "RAD"))
            if nums.get(0, 0) > 0:
                for i, data in enumerate(sorted_data[flag:flag+nums.get(0, 0)]):
                    self.TreeWidget.topLevelItem(1).child(0).child(i).setText(0, _translate(
                        "Tui", 'Flag: {}\nStrength: {}\nSeed: {}\nSlider: {}'.format(flag, data['strength'], data['Seed'], data['SliderB'])))
                    self.TreeWidget.topLevelItem(1).child(0).child(i).setFont(0, font_8)
                    flag += 1

            self.TreeWidget.topLevelItem(1).child(1).setFont(0, font_8)
            self.TreeWidget.topLevelItem(1).child(1).setText(0, _translate("Tui", "BMD"))
            if nums.get(1, 0) > 0:
                for i, data in enumerate(sorted_data[flag:flag+nums.get(1, 0)]):
                    self.TreeWidget.topLevelItem(1).child(1).child(i).setText(0, _translate(
                        "Tui", 'Flag: {}\nStrength: {}\nTree: {}'.format(flag, data['strength'], data['Tree'])))
                    self.TreeWidget.topLevelItem(1).child(1).child(i).setFont(0, font_8)
                    flag += 1

            self.TreeWidget.topLevelItem(1).child(2).setFont(0, font_8)
            self.TreeWidget.topLevelItem(1).child(2).setText(0, _translate("Tui", "ODM"))
            if nums.get(2, 0) > 0:
                for i, data in enumerate(sorted_data[flag:flag+nums.get(2, 0)]):
                    self.TreeWidget.topLevelItem(1).child(2).child(i).setText(0, _translate(
                        "Tui", 'Flag: {}\nStrength: {}\nList: {}'.format(flag, data['strength'], data['ListWidget_E'])))
                    self.TreeWidget.topLevelItem(1).child(2).child(i).setFont(0, font_8)
                    flag += 1

            self.TreeWidget.topLevelItem(1).child(3).setFont(0, font_8)
            self.TreeWidget.topLevelItem(1).child(3).setText(0, _translate("Tui", "EDM"))
            if nums.get(3, 0) > 0:
                for i, data in enumerate(sorted_data[flag:flag+nums.get(3, 0)]):
                    self.TreeWidget.topLevelItem(1).child(3).child(i).setText(0, _translate(
                        "Tui", 'Flag: {}\nStrength: {}\nList: {}\nSnakes: {}'.format(flag, data['strength'], data['ListWidget_F'], data['Snakes'])))
                    self.TreeWidget.topLevelItem(1).child(3).child(i).setFont(0, font_8)
                    flag += 1

        for i in range(self.TreeWidget.topLevelItemCount()):
            item = self.TreeWidget.topLevelItem(i)
            self.expandAll(item)

    def expandAll(self, item):
        item.setExpanded(True)
        for i in range(item.childCount()):
            self.expandAll(item.child(i))

    def createWarningInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="请点击左侧树控件选择算法与图片匹配",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    @pyqtSlot()
    def handleButtonClicked(self):
        if self.window.algorithmed['RadioBoxes'] == 'RadioButton_2':

            # 获取当前选中的项
            selected_items = self.TreeWidget.selectedItems()

            if selected_items:
                for item in selected_items:
                    parent_item = item.parent()
                    if parent_item is not None:
                        grandparent_item = parent_item.parent()
                        if grandparent_item is not None:
                            flag = int(item.text(0).split("\n")[0].split(":")[1].strip())
                            if self.didshow.flipView.currentIndex() == flag:

                                subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\ImgTransform.exe',
                                                      '-i', './data/didder/{}.png'.format(flag), '-o', './data/image/didder.png',
                                                      '-m', 'true', '-s', '1.0'], shell=True)

                                subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\ImgTransform.exe',
                                                      '-i',self.window.algorithmed['imageFile'].replace('/', '\\'), '-o',
                                                      './data/image/contrast.png', '-m', 'true', '-s', '1.0'], shell=True)

                                subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\ImgTransform.exe',
                                                      '-i', './data/didder/{}.png'.format(flag), '-o', './data/split/Label',
                                                      '-m', 'false', '-s', '1.0'], shell=True)

                                self.window.onButtonClicked("go_last", 'Dui')
                                self.updateUiH.emit()

                            else:
                                self.createWarningInfoBar()
            else:
                self.createWarningInfoBar()

        elif self.window.algorithmed['RadioBoxes'] == 'RadioButton_1':
            self.window.onButtonClicked("go_last", 'Dui')
            self.updateUiH.emit()

class Gui(Ui_Hui, QWidget):
    def __init__(self, navigationInterface, windowInstance, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.navigationInterface = navigationInterface  # 保存导航界面引用
        self.window = windowInstance  # 确保引用了 Window 实例
        self.PushButton_SF.clicked.connect(self.handleButtonClicked)
        self.CreateStackedItemsed = False

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    def updateUiH(self):
        self.createStackedItems()

    @pyqtSlot()
    def handleButtonClicked(self):
        self.SimpleCardWidget = self.findChild(SimpleCardWidget, 'SimpleCardWidget')
        if self.SimpleCardWidget:
            self.TreeWidget = self.SimpleCardWidget.findChild(TreeWidget, 'TreeWidget')

        selected_items = self.TreeWidget.selectedItems()
        if selected_items:
            if self.CreateStackedItemsed == True:
                self.dirName = selected_items[0].text(0).split("\n")[0].split('"')[1]
                self.TreeWidget.setSelectionMode(QAbstractItemView.NoSelection)
                self.PushButton_SF.clicked.disconnect()
                self.PushButton_2.clicked.disconnect()
                _translate = QtCore.QCoreApplication.translate
                self.PushButton_SF.setText(_translate("Hui", "控 件 已 锁 定 请 耐 心 等 候"))
                self.idcounts_dat = os.path.join(self.LineEdit_2.text(), self.dirName, 'data', 'idcounts.dat')
                self.map_data = os.path.join(self.LineEdit_2.text(), self.dirName, 'data', 'map.dat')

                # 创建并启动工作进程
                self.worker3 = Worker3(self.parent().MapMod)
                self.worker3.finished3.connect(self.on_finsh3)
                self.worker3.moveToThread(QThread())
                self.worker3.thread().started.connect(self.worker3.run)
                self.worker3.thread().start()

            else:
                self.createWarningInfoBar2()
        else:
            self.createWarningInfoBar()

    @pyqtSlot(int, int)
    def on_finsh3(self, a, b):
        numbers = [list(map(int, item.split('.')[0].split('_')[1:])) for item in [item for item in os.listdir('./data/split/') if os.path.isfile(os.path.join('./data/split/', item))]]
        max_x, max_y = max(numbers, key=lambda x: x[0])[0], max(numbers, key=lambda x: x[1])[1]
        self.worker4 = Worker4(self.parent().MapMod, self.LineEdit_2.text(), self.dirName, max_x, max_y, a, b)
        self.worker4.finished4.connect(self.on_finsh4)
        self.worker4.moveToThread(QThread())
        self.worker4.thread().started.connect(self.worker4.run)
        self.worker4.thread().start()

    @pyqtSlot(int, int, int, int, str, str)
    def on_finsh4(self, a, b, max_x, max_y, saves, dirName):
        print(a, b, max_x, max_y, dirName, saves)
        _translate = QtCore.QCoreApplication.translate
        if self.parent().MapMod in [1, 3]:
            self.createStackedItems2(xx=max_x-1, yu=a, yd=b, zz=max_y-1, saves=saves, dirName=dirName)
        self.PushButton_SF.setText(_translate("Hui", "纯 文 件 地 图 画 生 成 完 成"))
        self.createSuccessInfoBar()

    def createStackedItems2(self, xx, yu, yd, zz, saves, dirName):
        self.CCCInterface = Dui(self, self, xx, yu, yd, zz, saves, dirName, self.window, self.navigationInterface)
        self.CCCInterface.setObjectName("CCCInterface")

        self.segmentedWidget.clear()

        self.addSubInterface(self.CCCInterface, 'CCCInterface', '位置编辑')
        self.stackedWidget.addWidget(self.CCCInterface)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.CCCInterface)
        self.segmentedWidget.setCurrentItem(self.CCCInterface.objectName())

        self.addSubInterface(self.AAAInterface, 'AAAInterface', '切割预览')
        self.addSubInterface(self.BBBInterface, 'BBBInterface', '对比预览')

        self.stackedWidget.addWidget(self.AAAInterface)
        self.stackedWidget.addWidget(self.BBBInterface)

    def createStackedItems(self):
        self.CreateStackedItemsed = True

        self.AAAInterface = AHui(self)
        self.AAAInterface.setObjectName("AAAInterface")
        self.BBBInterface = BHui(self)
        self.BBBInterface.setObjectName("BBBInterface")

        self.addSubInterface(self.AAAInterface, 'AAAInterface', '切割预览')
        self.addSubInterface(self.BBBInterface, 'BBBInterface', '对比预览')

        self.stackedWidget.addWidget(self.AAAInterface)
        self.stackedWidget.addWidget(self.BBBInterface)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.AAAInterface)
        self.segmentedWidget.setCurrentItem(self.AAAInterface.objectName())

    def createWarningInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="请选择世界文件夹",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createWarningInfoBar2(self):
        InfoBar.warning(
            title='Warning',
            content="前按照步骤完成前面的提交",
            orient=Qt.Horizontal,
            isClosable=True,   # disable close button
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createSuccessInfoBar(self):
        self.infoBar = InfoBar.success(
            title='Success',
            content="map.dat & idcounts.dat 已完成！",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=-1,
            parent=self
        )

    def createSuccessInfoBar2(self):
        self.infoBar = InfoBar.success(
            title='Success',
            content="地图存档文件生成成功！",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=-1,
            parent=self
        )


class StyleSheet(StyleSheetBase, Enum):
    WINDOW = "window"
    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"qss/{theme.value.lower()}/{self.value}.qss"


class Window(MSFluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.algorithmed = algorithmed
        self.MapMod = MapMod

        # create sub interface
        self.settingButton = UI_Yui(self.navigationInterface)
        self.settingButton.setObjectName("settingInterface")

        self.homeInterface = Aui(self.navigationInterface, self)
        self.colorInterface = Bui(self.navigationInterface, self)

        self.appInterface = Cui(self.navigationInterface, self)
        self.appInterface.setObjectName("homeInterface")

        self.imageInterface = Fui(self.navigationInterface, self)
        self.imageInterface.setObjectName("imageInterface")

        self.libraryInterface = Eui(self.navigationInterface, self)
        self.libraryInterface.setObjectName("libraryInterface")

        self.videoInterface = Gui(self.navigationInterface, self)

        # 连接 Cui 发出的信号到 Fui 的槽函数
        self.appInterface.updateUi.connect(self.imageInterface.updateUi)
        self.imageInterface.updateUiH.connect(self.videoInterface.updateUiH)

        self.setThemeBasedStyles()  # 在初始化时设置样式
        self.initNavigation()
        self.initWindow()

        QTimer.singleShot(1500, self.splashScreen.finish)

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '引入')
        self.addSubInterface(self.colorInterface, FIF.PALETTE, '材质')
        self.addSubInterface(self.appInterface, FIF.LABEL, '算法')
        self.addSubInterface(self.imageInterface, FIF.IMAGE_EXPORT, '转换')
        self.addSubInterface(self.videoInterface, FIF.SAVE_AS, '导出')

        self.addSubInterface(self.settingButton, FIF.SETTING, '设置', FIF.SETTING, NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.libraryInterface, FIF.HELP, '帮助', FIF.HELP, NavigationItemPosition.BOTTOM)
        self.navigationInterface.addItem(
            routeKey='Help',
            icon=FIF.GITHUB,
            text='源码',
            onClick=self.showMessageBox,
            selectable=False,
            position=NavigationItemPosition.BOTTOM,
        )

        # 确保所有子界面都添加到 stackedWidget 中
        self.stackedWidget.addWidget(self.homeInterface)
        self.stackedWidget.addWidget(self.colorInterface)
        self.stackedWidget.addWidget(self.appInterface)
        self.stackedWidget.addWidget(self.imageInterface)
        self.stackedWidget.addWidget(self.videoInterface)
        self.stackedWidget.addWidget(self.libraryInterface)
        self.stackedWidget.addWidget(self.settingButton)

        # 设置初始页面
        self.navigationInterface.setCurrentItem(self.homeInterface.objectName())

        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.navigationInterface.setFont(font)

        self.navigationInterface.setStyleSheet('''
        NavigationPanel[menu=true] {
            background-color: rgb(32, 32, 32);
            border: 1px solid rgb(57, 57, 57);
            border-top-right-radius: 7px;
            border-bottom-right-radius: 7px;
        }
        
        NavigationPanel[menu=false] {
            background-color: transparent;
            border: 1px solid transparent;
            border-top-right-radius: 7px;
            border-bottom-right-radius: 7px;
        }
        
        NavigationPanel[transparent=true] {
            background-color: transparent;
        }
        
        QScrollArea,
        #scrollWidget {
            border: none;
            background-color: transparent;
        }
        
        /* NavigationInterface {
            background-color: rgb(32, 32, 32);
        } */''')

    def initWindow(self):
        self.setFixedSize(1040, 720)

        self.titleBar.maxBtn.hide()
        self.titleBar.setDoubleClickEnabled(False)

        icon = QtGui.QIcon("./image/Sprite-0001.ico")
        self.titleBar.iconLabel.setPixmap(icon.pixmap(24, 24))
        self.titleBar.iconLabel.setFixedSize(36, 36)

        self.titleBar.hBoxLayout.insertSpacing(0, 4)

        self.titleBar.titleLabel.setText('MC-map-drawing-ETO')

        titleLabelStyle = """
        QLabel {
            font-family: '萝莉体';
            font-size: 15px;
        }
        """
        self.titleBar.titleLabel.setStyleSheet(titleLabelStyle)

        self.splashScreen = SplashScreen(QIcon('./image/setup.jpg'), self)
        self.splashScreen.setIconSize(QSize(1040, 720))
        self.splashScreen.raise_()

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        self.show()
        QApplication.processEvents()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, 'splashScreen'):
            self.splashScreen.resize(self.size())

    def setThemeBasedStyles(self):
        # 设置初始样式
        StyleSheet.WINDOW.apply(self)
        # 根据当前主题更新复选框样式
        currentTheme = qconfig.theme

        if currentTheme == Theme.LIGHT:
            self.colorInterface.updateCheckBoxStyles("CheckBox {\n"
"    color: #000000;\n"
"    font: 8px \'萝莉体\';\n"
"    spacing: 8px;\n"
"    min-width: 28px;\n"
"    min-height: 22px;\n"
"    outline: none;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"CheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 1px;\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CheckBox:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"", "CheckBox {\n"
"    color: #000000;\n"
"    font: 12px \'萝莉体\';\n"
"    spacing: 6px;\n"
"    min-width: 16px;\n"
"    min-height: 16px;\n"
"    outline: none;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"CheckBox::indicator {\n"
"    width: 9px;\n"
"    height: 9px;\n"
"    border-radius: 1px;\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CheckBox:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"")
        elif currentTheme == Theme.DARK:
            self.colorInterface.updateCheckBoxStyles("CheckBox {\n"
"    color: #FFFFFF;\n"
"    font: 8px \'萝莉体\';\n"
"    spacing: 8px;\n"
"    min-width: 28px;\n"
"    min-height: 22px;\n"
"    outline: none;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"CheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 1px;\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CheckBox:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"", "CheckBox {\n"
"    color: #FFFFFF;\n"
"    font: 12px \'萝莉体\';\n"
"    spacing: 6px;\n"
"    min-width: 16px;\n"
"    min-height: 16px;\n"
"    outline: none;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"CheckBox::indicator {\n"
"    width: 9px;\n"
"    height: 9px;\n"
"    border-radius: 1px;\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CheckBox:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"")

    def onButtonClicked(self, buttonName, next):
        # 获取当前发送信号的按钮对象
        print(f"Clicked button: {buttonName}")
        # 根据按钮名称切换到相应的页面
        if next == 'Aui':
            self.switchTo(self.colorInterface)
        elif next == 'Bui':
            self.switchTo(self.appInterface)
        elif next == 'Cui':
            self.switchTo(self.imageInterface)
        elif next == 'Dui':
            self.switchTo(self.videoInterface)

    def showMessageBox(self):
        w = MessageBox(
            'byETO',
            '跳转至项目GitHub首页，可以为本项目提交Issue哦~',
            self
        )
        w.yesButton.setText('这就去')
        w.cancelButton.setText('懒得看')

        self.set_font("萝莉体", 10, w.yesButton)

        titleLabelStyle = """
        QLabel {
            font-family: '萝莉体';
            font-size: 20px;
        }
        """
        w.titleLabel.setStyleSheet(titleLabelStyle)

        contentLabelStyle = """
        QLabel {
            font-family: '萝莉体';
            font-size: 16px;
        }
        """
        w.contentLabel.setStyleSheet(contentLabelStyle)

        cancelButtonStyle = """
        QPushButton {
            font-family: '萝莉体';
            font-size: 13px;
        }
        """
        w.cancelButton.setStyleSheet(cancelButtonStyle)

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/ETO-QSH/MC-map-drawing-ETO"))

    def set_font(self, font_name, font_size, label):
        """ 设置指定标签的字体和大小 """
        font = QFont(font_name, font_size)
        label.setFont(font)


if __name__ == '__main__':

    shutil.rmtree('./data')
    for dirs in ['./data/didder', './data/image', './data/pixivColor', './data/split', './data/world_dat', './data/world_mca', './data/Backup']:
        os.makedirs(dirs, exist_ok=True)

    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    MapMod, algorithmed = 0, {'RadioBoxes': 'RadioButton_0'}

    setTheme(Theme.DARK) if cfg.get(cfg.themeModeETO) == '暗色主题' else setTheme(Theme.LIGHT)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
