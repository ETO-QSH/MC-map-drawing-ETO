# coding:utf-8

import ast
import subprocess
import sys
import json
from enum import Enum

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSlot, QSize, QEventLoop, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QStackedWidget, QStackedLayout, QCheckBox, QLabel, \
    QTreeWidgetItem, QTreeWidget

from collections import Counter
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow, NavigationAvatarWidget,
                            qrouter, SubtitleLabel, setFont, setThemeColor, theme, SplashScreen, InfoBar,
                            InfoBarPosition, PushButton, RadioButton, LineEdit, SpinBox, SegmentedWidget, TreeWidget,
                            SwitchButton, ListWidget, Slider, SimpleCardWidget)
from qfluentwidgets import FluentIcon as FIF

from ETO.Aui import Ui_Aui
from ETO.Bui import Ui_Bui
from ETO.Tui import Ui_Tui
from ETO.Xui import UI_Xui
from ETO.Zui import Ui_Zui
from ETO.Kui import Ui_Kui
from ETO.settings.demo import UI_Yui

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from PyQt5.QtCore import pyqtSlot
from qfluentwidgets import qconfig, Theme, StyleSheetBase

from qfluentwidgets import SplashScreen

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
                creat_BlockList_colorList(r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\src\BlockList.json',
                                          r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\src\colorList.txt',
                                       r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\data\BlockList.json',
                                       r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\data\colorList.txt',
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

                # 要在这里更新列表 ~
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

    @pyqtSlot()
    def handleButtonClicked(self):
        # 调用 Window 类的 onButtonClicked 方法
        button = self.sender()
        buttonName = button.objectName()
        self.window.onButtonClicked(buttonName, 'Kui')


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
                            self.window.onButtonClicked("go_last", 'Dui')
                            subprocess.run([r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\exe\ImgTransform.exe',
                                                  '-i', './data/didder/{}.png'.format(flag), '-o', './data/image/didder.png',
                                                  '-m', 'true', '-s', '1.0'], shell=True)
                        else:
                            self.createWarningInfoBar()
        else:
            self.createWarningInfoBar()


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
        self.appInterface.setObjectName("imageInterface")

        self.libraryInterface = Eui(self.navigationInterface, self)
        self.libraryInterface.setObjectName("libraryInterface")

        self.videoInterface = Widget('Result Export', self)

        # 连接 Cui 发出的信号到 Fui 的槽函数
        self.appInterface.updateUi.connect(self.imageInterface.updateUi)

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

    def initWindow(self):
        self.setFixedSize(1040, 720)
        self.setWindowIcon(QIcon(r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\256t.png'))
        self.setWindowTitle('MC-map-drawing-ETO')

        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(128, 128))
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

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/ETO-QSH/MC-map-drawing-ETO"))


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    algorithmed = {'RadioBoxes': 'RadioButton_0'}

    MapMod = 0

    #setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
