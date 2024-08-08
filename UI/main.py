# coding:utf-8
import sys
from enum import Enum

from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSlot, QSize, QEventLoop, QTimer
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QStackedWidget, QStackedLayout, QCheckBox, QLabel

from qfluentwidgets.components.widgets.frameless_window import FramelessWindow

from examples.window.clock.view.Ui_FocusInterface import Ui_FocusInterface
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow, NavigationAvatarWidget,
                            qrouter, SubtitleLabel, setFont, setThemeColor, theme, SplashScreen, InfoBar,
                            InfoBarPosition, PushButton, RadioButton, LineEdit, SpinBox, SegmentedWidget, TreeWidget,
                            SwitchButton, ListWidget, Slider)
from qfluentwidgets import FluentIcon as FIF

from ETO.Aui import Ui_Aui
from ETO.Bui import Ui_Bui
from ETO.Zui import Ui_Zui
from ETO.Kui import Ui_Kui

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from PyQt5.QtCore import pyqtSlot
from qfluentwidgets import qconfig, Theme, StyleSheetBase

from qfluentwidgets import Theme
from qfluentwidgets import QConfig

from qfluentwidgets import SplashScreen


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
        MapMod = buttonName.split('_')[1]
        print('MapMod:', MapMod)


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
        self.window.onButtonClicked(buttonName, 'Bui')
        print('nameList:', nameList)

    def updateCheckBoxStyles(self, styleSheet_0, styleSheet_1):
        # 查找所有特定名称前缀的控件
        checkBoxes_0 = self.findChildren(QCheckBox)
        checkBoxes_1 = [self.findChildren(QWidget, "CheckBox_B" + str(i))[0] for i in range(0, 62)]
        for checkBox in checkBoxes_0:
            checkBox.setStyleSheet(styleSheet_1)
        for checkBox in checkBoxes_1:
            checkBox.setStyleSheet(styleSheet_0)


class Cui(Ui_Zui, QWidget):
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

        algorithmed = {}

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
            val = SpinB.value()
            if 'RadioBoxes' in algorithmed and algorithmed['RadioBoxes'] == 'RadioButton_1':
                if val != 0:
                    algorithmed['KTree'] = val
            else:
                algorithmed['KTree'] = 0

        if len(list(algorithmed)) == 3:
            print('DICT:', algorithmed, self.globalList)
            buttonName = "go_next"
            self.window.onButtonClicked(buttonName, 'Cui')
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


# 定义 StyleSheet 类
class StyleSheet(StyleSheetBase, Enum):
    WINDOW = "window"
    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"qss/{theme.value.lower()}/{self.value}.qss"


class Window(MSFluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # create sub interface
        self.homeInterface = Aui(self.navigationInterface, self)
        self.colorInterface = Bui(self.navigationInterface, self)
        self.appInterface = Cui(self.navigationInterface, self)
        self.appInterface.setObjectName("homeInterface")
        self.imageInterface = Dui(self.navigationInterface, self)
        self.videoInterface = Widget('Result Export', self)
        self.libraryInterface = Widget('GitHub Home', self)
        self.settingButton = Widget('Setting Button', self)

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
        self.addSubInterface(self.libraryInterface, FIF.GITHUB, '源码', FIF.GITHUB, NavigationItemPosition.BOTTOM)
        self.navigationInterface.addItem(
            routeKey='Help',
            icon=FIF.HELP,
            text='帮助',
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
        # self.resize(900, 720)
        self.setFixedSize(1040, 720)
        self.setWindowIcon(QIcon(r'D:\Work Files\PyQt-Fluent-Widgets-exploit\ETO\256t.png'))
        self.setWindowTitle('MC-map-drawing-ETO')

        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(128, 128))
        self.splashScreen.raise_()

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        # self.move(w//2 - self.width()//2 - 66, h//2 - self.height()//2)
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

    def showMessageBox(self):
        w = MessageBox(
            '喵~',
            '喵喵喵喵喵喵喵~',
            self
        )
        w.yesButton.setText('喵喵喵~')
        w.cancelButton.setText('喵喵喵喵喵~')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/ETO-QSH/MC-map-drawing-ETO"))


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    setTheme(Theme.DARK)
    setThemeColor('#FFBFBF')

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
