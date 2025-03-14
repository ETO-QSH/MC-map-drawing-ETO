
import os, re
from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHBoxLayout, QFrame, QLabel, QStackedWidget
from qfluentwidgets import SmoothScrollArea, LineEdit, PushButton, HyperlinkLabel, qconfig, Theme, StyleSheetBase, \
    InfoBarPosition, InfoBar, SwitchButton, TreeWidget, Slider

from ETO.byETO.Cui import Ui_Cui
from ETO.byETO.Dui import Ui_Dui
from ETO.byETO.Eui import Ui_Eui
from ETO.byETO.Fui import Ui_Fui

def find_path(filename):
    for root, dirs, files in os.walk(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))):
        for file in files:
            if file.endswith(os.path.splitext(filename)[1]) and file.startswith(os.path.splitext(filename)[0]):
                return os.path.join(root, file)
    return None

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

class MyScrollWidget(SmoothScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.targetLineEdit = None  # 用于存储目标 LineEdit 控件

    def setTargetLineEdit(self, lineEdit):
        self.targetLineEdit = lineEdit  # 设置目标 LineEdit 控件

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                filePath = url.toLocalFile()
                if self.isValidImage(filePath):
                    links.append(filePath)
            if links:
                self.targetLineEdit.setText(links[0])
            else:
                self.showTeachingTip()
        else:
            event.ignore()

    def isValidImage(self, filePath):
        # 检查文件扩展名是否为 PNG 或 JPG
        return filePath.lower().endswith(('.png', '.jpg', '.jpeg'))

    def showTeachingTip(self):
        TeachingTip.create(
            target=self,
            icon=InfoBarIcon.ERROR,
            title='错误',
            content='请拖入单个图片文件（PNG或JPG）',
            isClosable=True,
            tailPosition=TeachingTipTailPosition.BOTTOM,
            duration=3000,
            parent=self
        )


class Aui(Ui_Cui, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 添加一个 QLabel 实例
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.PushButton_SF.clicked.connect(self.handleButtonClicked)
        self.ui_zui = parent  # 假设 parent 是 Ui_Zui 的实例

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    @pyqtSlot()
    def handleButtonClicked(self):
        algorithm = {}

        algorithm['QS'] = 0

        SSpinBoxBoxes = self.ui_zui.findChildren(SpinBox)
        for SSpin in SSpinBoxBoxes:
            val = SSpin.value()
            algorithm['strength'] = val

        LineEditBoxes = self.findChildren(LineEdit)
        for LineE in LineEditBoxes:
            if LineE.objectName() == 'Text_seed':
                text = LineE.text()
                algorithm['Seed'] = text

        lst = {}
        SliderBoxes = self.findChildren(Slider)
        for SliderB in SliderBoxes:
            name = SliderB.objectName()
            lst[name] = SliderB.value() / 100
        algorithm['SliderB'] = '{},{},{},{},{},{}'.format(lst['Slider_R_min'], lst['Slider_R_max']
                                                              , lst['Slider_G_min'], lst['Slider_G_max']
                                                              , lst['Slider_B_min'], lst['Slider_B_max'])

        nameB, RadioBoxes = 'RadioButton_0', self.ui_zui.findChildren(RadioButton)
        for Radio in RadioBoxes:
            if Radio.isChecked():
                nameB = Radio.objectName()
                break

        if nameB == 'RadioButton_1':
            Ui_Fui.createSuccessInfoBar(self)
            self.ui_zui.createInfoInfoBar()  # 假设 self.window 是 Ui_Zui 的实例
        elif nameB == 'RadioButton_2':
            if len(list(algorithm)) == 4 and algorithm['Seed'] != '':
                if algorithm in self.ui_zui.globalList:
                    Ui_Cui.createRepeatInfoBar(self)
                else:
                    self.ui_zui.globalList.append(algorithm)
                    Ui_Cui.createSuccessInfoBar(self)
                    self.ui_zui.createInfoInfoBar()
            else:
                Ui_Cui.createWarningInfoBar(self)
        else:
            Ui_Cui.createWarningInfoBar2(self)

class Bui(Ui_Dui, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 添加一个 QLabel 实例
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.PushButton_SF.clicked.connect(self.handleButtonClicked)
        self.ui_zui = parent  # 假设 parent 是 Ui_Zui 的实例

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    @pyqtSlot()
    def handleButtonClicked(self):
        algorithm = {}

        algorithm['QS'] = 1

        SSpinBoxBoxes = self.ui_zui.findChildren(SpinBox)
        for SSpin in SSpinBoxBoxes:
            val = SSpin.value()
            algorithm['strength'] = val

        TreeBoxes = self.findChildren(TreeWidget)
        for Tree in TreeBoxes:
            for item in Tree.selectedItems():
                if '.' not in item.text(0):
                    algorithm['Tree'] = item.text(0).replace(" ", "")

        nameB, RadioBoxes = 'RadioButton_0', self.ui_zui.findChildren(RadioButton)
        for Radio in RadioBoxes:
            if Radio.isChecked():
                nameB = Radio.objectName()
                break

        if nameB == 'RadioButton_1':
            Ui_Fui.createSuccessInfoBar(self)
            self.ui_zui.createInfoInfoBar()  # 假设 self.window 是 Ui_Zui 的实例
        elif nameB == 'RadioButton_2':
            if len(list(algorithm)) == 3:
                if algorithm in self.ui_zui.globalList:
                    Ui_Dui.createRepeatInfoBar(self)
                else:
                    self.ui_zui.globalList.append(algorithm)
                    Ui_Dui.createSuccessInfoBar(self)
                    self.ui_zui.createInfoInfoBar()  # 假设 self.window 是 Ui_Zui 的实例
            else:
                Ui_Dui.createWarningInfoBar(self)
        else:
            Ui_Dui.createWarningInfoBar2(self)

class Cui(Ui_Eui, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 添加一个 QLabel 实例
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.PushButton_SF.clicked.connect(self.handleButtonClicked)
        self.ui_zui = parent  # 假设 parent 是 Ui_Zui 的实例

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    @pyqtSlot()
    def handleButtonClicked(self):
        algorithm = {}

        algorithm['QS'] = 2

        SSpinBoxBoxes = self.ui_zui.findChildren(SpinBox)
        for SSpin in SSpinBoxBoxes:
            val = SSpin.value()
            algorithm['strength'] = val

        ListWidgetBoxes = self.findChildren(ListWidget)
        for ListW in ListWidgetBoxes:
            if ListW.objectName() == 'ListWidget_E':
                for item in ListW.selectedItems():
                    algorithm['ListWidget_E'] = item.text()

        nameB, RadioBoxes = 'RadioButton_0', self.ui_zui.findChildren(RadioButton)
        for Radio in RadioBoxes:
            if Radio.isChecked():
                nameB = Radio.objectName()
                break

        if nameB == 'RadioButton_1':
            Ui_Fui.createSuccessInfoBar(self)
            self.ui_zui.createInfoInfoBar()  # 假设 self.window 是 Ui_Zui 的实例
        elif nameB == 'RadioButton_2':
            if len(list(algorithm)) == 3:
                if algorithm in self.ui_zui.globalList:
                    Ui_Eui.createRepeatInfoBar(self)
                else:
                    self.ui_zui.globalList.append(algorithm)
                    Ui_Eui.createSuccessInfoBar(self)
                    self.ui_zui.createInfoInfoBar()  # 假设 self.window 是 Ui_Zui 的实例
            else:
                Ui_Eui.createWarningInfoBar(self)
        else:
            Ui_Eui.createWarningInfoBar2(self)

class Dui(Ui_Fui, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 添加一个 QLabel 实例
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.PushButton_SF.clicked.connect(self.handleButtonClicked)
        self.ui_zui = parent  # 假设 parent 是 Ui_Zui 的实例

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)

    @pyqtSlot()
    def handleButtonClicked(self):
        algorithm = {}

        algorithm['QS'] = 3

        SSpinBoxBoxes = self.ui_zui.findChildren(SpinBox)
        for SSpin in SSpinBoxBoxes:
            val = SSpin.value()
            algorithm['strength'] = val

        SwitchBoxes = self.findChildren(SwitchButton)
        for Switch in SwitchBoxes:
            algorithm['Snakes'] = Switch.isChecked()

        ListWidgetBoxes = self.findChildren(ListWidget)
        for ListW in ListWidgetBoxes:
            if ListW.objectName() == 'ListWidget_F':
                for item in ListW.selectedItems():
                    algorithm['ListWidget_F'] = item.text()

        nameB, RadioBoxes = 'RadioButton_0', self.ui_zui.findChildren(RadioButton)
        for Radio in RadioBoxes:
            if Radio.isChecked():
                nameB = Radio.objectName()
                break

        if nameB == 'RadioButton_1':
            Ui_Fui.createSuccessInfoBar(self)
            self.ui_zui.createInfoInfoBar()  # 假设 self.window 是 Ui_Zui 的实例
        elif nameB == 'RadioButton_2':
            if len(list(algorithm)) == 4:
                if algorithm in self.ui_zui.globalList:
                    Ui_Fui.createRepeatInfoBar(self)
                else:
                    self.ui_zui.globalList.append(algorithm)
                    Ui_Fui.createSuccessInfoBar(self)
                    self.ui_zui.createInfoInfoBar()  # 假设 self.window 是 Ui_Zui 的实例
            else:
                Ui_Fui.createWarningInfoBar(self)
        else:
            Ui_Fui.createWarningInfoBar2(self)


class Ui_Zui(object):
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
        self.action_button = PushButton('Next')
        self.globalList = []

        # 创建 Aui 实例
        self.RADInterface = Aui(self)
        self.RADInterface.setObjectName("RADInterface")
        self.BMDInterface = Bui(self)
        self.BMDInterface.setObjectName("BMDInterface")
        self.ODMInterface = Cui(self)
        self.ODMInterface.setObjectName("ODMInterface")
        self.EDMInterface = Dui(self)
        self.EDMInterface.setObjectName("EDMInterface")

        self.addSubInterface(self.RADInterface, 'RADInterface', 'RAD')
        self.addSubInterface(self.BMDInterface, 'BMDInterface', 'BMD')
        self.addSubInterface(self.ODMInterface, 'ODMInterface', 'ODM')
        self.addSubInterface(self.EDMInterface, 'EDMInterface', 'EDM')

        # 添加 Aui 实例到 stackedWidget
        self.stackedWidget.addWidget(self.RADInterface)
        self.stackedWidget.addWidget(self.BMDInterface)
        self.stackedWidget.addWidget(self.ODMInterface)
        self.stackedWidget.addWidget(self.EDMInterface)

        # 连接 SegmentedWidget 的信号到槽函数
        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.RADInterface)
        self.segmentedWidget.setCurrentItem(self.RADInterface.objectName())

    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.segmentedWidget.setCurrentItem(widget.objectName())

    def setupUi(self, Zui):
        Zui.setWindowTitle("Zui")
        Zui.resize(960, 750)
        Zui.setFocusPolicy(QtCore.Qt.ClickFocus)

        # 创建并设置布局
        self.gridLayout = QtWidgets.QGridLayout(Zui)
        Zui.setLayout(self.gridLayout)  # 确保为 Zui 设置了布局

        # 创建一个垂直布局作为中心容器
        self.centerLayout = QtWidgets.QVBoxLayout()
        self.centerLayout.setContentsMargins(0, 0, 0, 0)
        self.centerLayout.setAlignment(Qt.AlignCenter)  # 设置布局居中

        # 创建 widget 并设置为居中布局的中心控件
        self.widget = QtWidgets.QWidget(Zui)
        self.widget.setGeometry(QtCore.QRect(185, 56, 592, 600))
        self.widget.setObjectName("widget")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.HorizontalSeparator = HorizontalSeparator(self.widget)
        self.HorizontalSeparator.setObjectName("HorizontalSeparator")
        self.gridLayout_3.addWidget(self.HorizontalSeparator, 1, 0, 1, 1)

        self.HorizontalSeparator_2 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_2.setObjectName("HorizontalSeparator_2")
        self.gridLayout_3.addWidget(self.HorizontalSeparator_2, 1, 2, 1, 1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.StrongBodyLabel_1 = StrongBodyLabel(self.widget)
        self.StrongBodyLabel_1.setObjectName("StrongBodyLabel_1")
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.StrongBodyLabel_1.setFont(font)
        self.StrongBodyLabel_1.setMinimumSize(QtCore.QSize(120, 30))
        self.StrongBodyLabel_1.setMaximumSize(QtCore.QSize(120, 30))
        self.gridLayout.addWidget(self.StrongBodyLabel_1, 2, 0, 1, 1)

        self.RadioButton_1 = RadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RadioButton_1.setFont(font)
        self.RadioButton_1.setStyleSheet(re.sub(r'\*\*\*', qconfig.themeColor.value.name(), '''
RadioButton {
    min-height: 24px;
    max-height: 24px;
    background-color: transparent;
    font: 15px \'萝莉体\';
    color: black;
}

RadioButton::indicator {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: rgba(0, 0, 0, 5);
    margin-right: 3px;
}

RadioButton::indicator:hover {
    background-color: rgba(0, 0, 0, 0);
}

RadioButton::indicator:pressed {
    border: 2px solid #bbbbbb;
    background-color: ***;
}

RadioButton::indicator:checked {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: ***;
}

RadioButton::indicator:checked:hover {
    background-color: ***;
}

RadioButton::indicator:checked:pressed {
    background-color: ***;
}

RadioButton:disabled {
    color: rgba(0, 0, 0, 110);
}

RadioButton::indicator:disabled {
    border: 2px solid #bbbbbb;
    background-color: transparent;
}

RadioButton::indicator:disabled:checked {
    border: none;
    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
            stop:0 rgb(255, 255, 255),
            stop:0.5 rgb(255, 255, 255),
            stop:0.6 rgba(0, 0, 0, 0.2169),
            stop:1 rgba(0, 0, 0, 0.2169));
}'''))

        self.RadioButton_1.setObjectName("RadioButton_1")
        self.gridLayout.addWidget(self.RadioButton_1, 0, 0, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.SpinBox = SpinBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SpinBox.setFont(font)
        self.SpinBox.setObjectName("SpinBox")
        self.gridLayout.addWidget(self.SpinBox, 2, 1, 1, 1, QtCore.Qt.AlignVCenter|QtCore.Qt.AlignVCenter)
        self.SpinBox.setMinimumSize(QtCore.QSize(120, 30))
        self.SpinBox.setMaximumSize(QtCore.QSize(120, 30))
        self.SpinBox.setValue(4)
        self.SpinBox.setRange(0, 244)
        self.SpinBox.setSingleStep(1)

        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.VerticalSeparator = VerticalSeparator(self.widget)
        self.VerticalSeparator.setObjectName("VerticalSeparator")
        self.gridLayout_3.addWidget(self.VerticalSeparator, 0, 1, 1, 1)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.RadioButton_2 = RadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RadioButton_2.setFont(font)
        self.RadioButton_2.setStyleSheet(re.sub(r'\*\*\*', qconfig.themeColor.value.name(), '''
RadioButton {
    min-height: 24px;
    max-height: 24px;
    background-color: transparent;
    font: 15px \'萝莉体\';
    color: black;
}

RadioButton::indicator {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: rgba(0, 0, 0, 5);
    margin-right: 3px;
}

RadioButton::indicator:hover {
    background-color: rgba(0, 0, 0, 0);
}

RadioButton::indicator:pressed {
    border: 2px solid #bbbbbb;
    background-color: ***;
}

RadioButton::indicator:checked {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: ***;
}

RadioButton::indicator:checked:hover {
    background-color: ***;
}

RadioButton::indicator:checked:pressed {
    background-color: ***;
}

RadioButton:disabled {
    color: rgba(0, 0, 0, 110);
}

RadioButton::indicator:disabled {
    border: 2px solid #bbbbbb;
    background-color: transparent;
}

RadioButton::indicator:disabled:checked {
    border: none;
    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
            stop:0 rgb(255, 255, 255),
            stop:0.5 rgb(255, 255, 255),
            stop:0.6 rgba(0, 0, 0, 0.2169),
            stop:1 rgba(0, 0, 0, 0.2169));
}'''))

        self.RadioButton_2.setObjectName("RadioButton_2")
        self.gridLayout_2.addWidget(self.RadioButton_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.SpinBox_S = SpinBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SpinBox_S.setFont(font)
        self.SpinBox_S.setObjectName("SpinBox_S")
        self.gridLayout_2.addWidget(self.SpinBox_S, 2, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SpinBox_S.setMinimumSize(QtCore.QSize(120, 30))
        self.SpinBox_S.setMaximumSize(QtCore.QSize(120, 30))
        self.SpinBox_S.setRange(-100, 100)
        self.SpinBox_S.setValue(100)
        self.SpinBox_S.setSingleStep(1)

        self.StrongBodyLabel_3 = StrongBodyLabel(self.widget)
        self.StrongBodyLabel_3.setObjectName("StrongBodyLabel_3")
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.StrongBodyLabel_3.setFont(font)
        self.StrongBodyLabel_3.setMinimumSize(QtCore.QSize(120, 30))
        self.StrongBodyLabel_3.setMaximumSize(QtCore.QSize(120, 30))
        self.gridLayout_2.addWidget(self.StrongBodyLabel_3, 2, 0, 1, 1)

        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(6)
        self.segmentedWidget.setFont(font)
        self.segmentedWidget.setObjectName("segmentedWidget")
        self.segmentedWidget.setMinimumSize(QtCore.QSize(250, 25))
        self.segmentedWidget.setMaximumSize(QtCore.QSize(250, 25))
        self.gridLayout_2.addWidget(self.segmentedWidget, 3, 0, 1, 2)

        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setMinimumSize(QtCore.QSize(250, 300))
        self.stackedWidget.setMaximumSize(QtCore.QSize(250, 300))
        self.gridLayout_2.addWidget(self.stackedWidget, 4, 0, 1, 2)

        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 1)

        self.VerticalSeparator_2 = VerticalSeparator(self.widget)
        self.VerticalSeparator_2.setObjectName("VerticalSeparator_2")
        self.gridLayout_3.addWidget(self.VerticalSeparator_2, 2, 1, 1, 1)

        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.StrongBodyLabel_2 = StrongBodyLabel(self.widget)
        self.StrongBodyLabel_2.setMinimumSize(QtCore.QSize(60, 30))
        self.StrongBodyLabel_2.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.StrongBodyLabel_2.setFont(font)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.gridLayout_6.addWidget(self.StrongBodyLabel_2, 0, 0, 1, 1)

        self.LineEdit_2 = LineEdit(self.widget)
        self.LineEdit_2.setMinimumSize(QtCore.QSize(150, 30))
        self.LineEdit_2.setMaximumSize(QtCore.QSize(150, 30))
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.LineEdit_2.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit_2.setFont(font)
        self.gridLayout_6.addWidget(self.LineEdit_2, 0, 1, 1, 1)

        self.PushButton_2 = PushButton(self.widget)
        self.PushButton_2.setMinimumSize(QtCore.QSize(60, 30))
        self.PushButton_2.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton_2.setFont(font)
        self.PushButton_2.setObjectName("PushButton_2")
        self.PushButton_2.clicked.connect(self.openFileSelector)
        self.gridLayout_6.addWidget(self.PushButton_2, 0, 2, 1, 1)

        self.SmoothScrollArea_2 = MyScrollWidget(self.widget)
        self.SmoothScrollArea_2.setMinimumSize(QtCore.QSize(280, 30))
        self.SmoothScrollArea_2.setMaximumSize(QtCore.QSize(280, 30))
        self.SmoothScrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SmoothScrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.SmoothScrollArea_2.setWidgetResizable(True)
        self.SmoothScrollArea_2.setObjectName("SmoothScrollArea_2")
        self.SmoothScrollArea_2.setStyleSheet("background-color: transparent;")
        self.SmoothScrollArea_2.setTargetLineEdit(self.LineEdit_2)  # 设置目标 LineEdit 控件

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 300, 30))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.HyperlinkLabel = HyperlinkLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(6)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.HyperlinkLabel.setFont(font)
        self.HyperlinkLabel.setObjectName("HyperlinkLabel")
        self.gridLayout_7.addWidget(self.HyperlinkLabel, 0, 0, 1, 1)
        self.SmoothScrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.addWidget(self.SmoothScrollArea_2, 1, 0, 1, 3, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.gridLayout_3.addLayout(self.gridLayout_6, 2, 2, 1, 1)

        self.PixmapLabel_2 = PixmapLabel(self.widget)
        self.PixmapLabel_2.setObjectName("PixmapLabel_2")
        self.PixmapLabel_2.setMinimumSize(QtCore.QSize(280, 360))
        self.PixmapLabel_2.setMaximumSize(QtCore.QSize(280, 360))
        # 连接 LineEdit_2 的信号到槽函数，以便在文本改变时更新图片
        self.LineEdit_2.textChanged.connect(self.updatePixmap)
        pixmap = QPixmap(find_path("file-format(黑).png"))
        if not pixmap.isNull():
            self.PixmapLabel_2.setPixmap(pixmap.scaled(self.PixmapLabel_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.gridLayout_3.addWidget(self.PixmapLabel_2, 4, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.SubtitleLabel_1 = SubtitleLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SubtitleLabel_1.setFont(font)
        self.SubtitleLabel_1.setObjectName("SubtitleLabel_1")
        self.gridLayout_3.addWidget(self.SubtitleLabel_1, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.SubtitleLabel_2 = SubtitleLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SubtitleLabel_2.setFont(font)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.gridLayout_3.addWidget(self.SubtitleLabel_2, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.HorizontalSeparator_4 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_4.setObjectName("HorizontalSeparator_4")
        self.gridLayout_3.addWidget(self.HorizontalSeparator_4, 3, 2, 1, 1)

        self.VerticalSeparator_3 = VerticalSeparator(self.widget)
        self.VerticalSeparator_3.setObjectName("VerticalSeparator_3")
        self.gridLayout_3.addWidget(self.VerticalSeparator_3, 4, 1, 1, 1)

        self.HorizontalSeparator_3 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_3.setObjectName("HorizontalSeparator_3")
        self.gridLayout_3.addWidget(self.HorizontalSeparator_3, 3, 0, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_3, 4, 1, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 2, 1, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 6, 1, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 0, 1, 1, 1)

        self.TitleLabel = TitleLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout_4.addWidget(self.TitleLabel, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.HorizontalSeparator_9 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_9.setObjectName("HorizontalSeparator_9")
        self.gridLayout_4.addWidget(self.HorizontalSeparator_9, 5, 1, 1, 1)

        self.HorizontalSeparator_7 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_7.setObjectName("HorizontalSeparator_7")
        self.gridLayout_4.addWidget(self.HorizontalSeparator_7, 3, 1, 1, 1)

        self.VerticalSeparator_4 = VerticalSeparator(self.widget)
        self.VerticalSeparator_4.setObjectName("VerticalSeparator_4")
        self.gridLayout_4.addWidget(self.VerticalSeparator_4, 4, 0, 1, 1)

        self.VerticalSeparator_5 = VerticalSeparator(self.widget)
        self.VerticalSeparator_5.setObjectName("VerticalSeparator_5")
        self.gridLayout_4.addWidget(self.VerticalSeparator_5, 4, 2, 1, 1)

        self.setThemeBasedStyles()

        self.retranslateUi(Zui)
        QtCore.QMetaObject.connectSlotsByName(Zui)

    def retranslateUi(self, Zui):
        _translate = QtCore.QCoreApplication.translate
        Zui.setWindowTitle(_translate("Zui", "Form"))
        self.StrongBodyLabel_1.setText(_translate("Zui", "       K-Tree 采样率"))
        self.StrongBodyLabel_3.setText(_translate("Zui", "       抖动强度 (±%)"))
        self.RadioButton_1.setText(_translate("Zui", "ΔE误差算法"))
        self.RadioButton_2.setText(_translate("Zui", "色彩抖动算法"))
        self.SubtitleLabel_1.setText(_translate("Zui", "算法选择"))
        self.SubtitleLabel_2.setText(_translate("Zui", "图片选择"))
        self.TitleLabel.setText(_translate("Zui", "选择算法和参数"))
        self.StrongBodyLabel_2.setText(_translate("Zui", " 打开文件："))
        self.PushButton_2.setText(_translate("Zui", "浏览"))
        self.HyperlinkLabel.setText(_translate("Zui", "{}".format(" "*45+"文 件 拖 入 区 域")))
        self.TitleLabel.setText(_translate("Zui", "选择算法和参数"))

    def addSubInterface(self, widget: QLabel, objectName: str, text: str):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)

        # 使用全局唯一的 objectName 作为路由键
        self.segmentedWidget.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def updatePixmap(self):
        # 从 LineEdit_2 获取图片路径
        imagePath = self.LineEdit_2.text()
        if imagePath:
            pixmap = QPixmap(imagePath)
            if not pixmap.isNull():
                # 设置PixmapLabel_2的图片
                self.PixmapLabel_2.setPixmap(pixmap.scaled(self.PixmapLabel_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                QtWidgets.QMessageBox.warning(self, "错误", "无法加载图片")

    def openFileSelector(self):
        # 打开文件选择对话框
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "", "Image Files (*.png *.jpg *.jpeg)")
        if filePath:
            # 检查文件格式
            if self.isValidImage(filePath):
                self.LineEdit_2.setText(filePath)
            else:
                print("这还限不了你是吧")

    def isValidImage(self, filePath):
        # 检查文件扩展名是否为 PNG 或 JPG
        return filePath.lower().endswith(('.png', '.jpg', '.jpeg'))

    def setThemeBasedStyles(self):
        # 设置初始样式
        StyleSheet.WINDOW.apply(self)
        # 根据当前主题更新复选框样式
        currentTheme = qconfig.theme

        if currentTheme == Theme.LIGHT:
            self.updateCheckBoxStyles(re.sub(r'\*\*\*', qconfig.themeColor.value.name(), '''
RadioButton {
    min-height: 24px;
    max-height: 24px;
    background-color: transparent;
    font: 15px \'萝莉体\';
    color: black;
}

RadioButton::indicator {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: rgba(0, 0, 0, 5);
    margin-right: 3px;
}

RadioButton::indicator:hover {
    background-color: rgba(0, 0, 0, 0);
}

RadioButton::indicator:pressed {
    border: 2px solid #bbbbbb;
    background-color: ***;
}

RadioButton::indicator:checked {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: ***;
}

RadioButton::indicator:checked:hover {
    background-color: ***;
}

RadioButton::indicator:checked:pressed {
    background-color: ***;
}

RadioButton:disabled {
    color: rgba(0, 0, 0, 110);
}

RadioButton::indicator:disabled {
    border: 2px solid #bbbbbb;
    background-color: transparent;
}

RadioButton::indicator:disabled:checked {
    border: none;
    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
            stop:0 rgb(255, 255, 255),
            stop:0.5 rgb(255, 255, 255),
            stop:0.6 rgba(0, 0, 0, 0.2169),
            stop:1 rgba(0, 0, 0, 0.2169));
}'''))

        elif currentTheme == Theme.DARK:
            self.updateCheckBoxStyles(re.sub(r'\*\*\*', qconfig.themeColor.value.name(), '''
RadioButton {
    min-height: 24px;
    max-height: 24px;
    background-color: transparent;
    font: 15px \'萝莉体\';
    color: white;
}

RadioButton::indicator {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: rgba(0, 0, 0, 5);
    margin-right: 3px;
}

RadioButton::indicator:hover {
    background-color: rgba(0, 0, 0, 0);
}

RadioButton::indicator:pressed {
    border: 2px solid #bbbbbb;
    background-color: ***;
}

RadioButton::indicator:checked {
    width: 9px;
    height: 9px;
    border-radius: 6px;
    border: 2px solid #999999;
    background-color: ***;
}

RadioButton::indicator:checked:hover {
    background-color: ***;
}

RadioButton::indicator:checked:pressed {
    background-color: ***;
}

RadioButton:disabled {
    color: rgba(0, 0, 0, 110);
}

RadioButton::indicator:disabled {
    border: 2px solid #bbbbbb;
    background-color: transparent;
}

RadioButton::indicator:disabled:checked {
    border: none;
    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
            stop:0 rgb(255, 255, 255),
            stop:0.5 rgb(255, 255, 255),
            stop:0.6 rgba(0, 0, 0, 0.2169),
            stop:1 rgba(0, 0, 0, 0.2169));
}'''))

    def updateCheckBoxStyles(self, styleSheet):
        Radio_0 = self.findChildren(RadioButton)
        for Switch in Radio_0:
            Switch.setStyleSheet(styleSheet)

    def createInfoInfoBar(self):
        # 如果弹窗实例存在，则先关闭它
        if self.infoBarInstance:
            self.infoBarInstance.close()
            self.infoBarInstance = None

        self.infoBarInstance = InfoBar.success(
            title='Success',
            content="进入下一步",
            orient=Qt.Horizontal,  # vertical layout
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=-1,
            parent=self
        )

        self.infoBarInstance.addWidget(self.action_button)

from qfluentwidgets import SegmentedWidget, setFont, SubtitleLabel, StrongBodyLabel, RadioButton, \
    TitleLabel, PixmapLabel, HorizontalSeparator, VerticalSeparator, ListWidget, SpinBox, TeachingTipTailPosition, \
    InfoBarIcon, TeachingTip
