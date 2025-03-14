
from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from qfluentwidgets import StyleSheetBase, Theme, InfoBar, InfoBarPosition


# 定义 StyleSheet 类
class StyleSheet(StyleSheetBase, Enum):
    WINDOW = "window"
    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"qss/{theme.value.lower()}/{self.value}.qss"

class Ui_Fui(object):
    def setupUi(self, Fui):
        Fui.setObjectName("Fui")
        Fui.resize(400, 367)
        self.layoutWidget = QtWidgets.QWidget(Fui)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 252, 303))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(self.layoutWidget)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(225, 270))
        self.SimpleCardWidget.setMaximumSize(QtCore.QSize(250, 270))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        self.SimpleCardWidget.setFont(font)
        self.SimpleCardWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.SimpleCardWidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ListWidget = ListWidget(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        self.ListWidget.setFont(font)
        self.ListWidget.setObjectName("ListWidget_F")
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        self.gridLayout_6.addWidget(self.ListWidget, 3, 0, 1, 1)
        self.StrongBodyLabel = StrongBodyLabel(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.StrongBodyLabel.setFont(font)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.gridLayout_6.addWidget(self.StrongBodyLabel, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SubtitleLabel = SubtitleLabel(self.SimpleCardWidget)
        self.SubtitleLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.SubtitleLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        self.SubtitleLabel.setFont(font)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.horizontalLayout.addWidget(self.SubtitleLabel, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.SwitchButton = SwitchButton(self.SimpleCardWidget)
        self.SwitchButton.setMinimumSize(QtCore.QSize(100, 25))
        self.SwitchButton.setMaximumSize(QtCore.QSize(100, 25))
        self.SwitchButton.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}\n"
"\n"
"SwitchButton {\n"
"    qproperty-spacing: 12;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"SwitchButton>QLabel {\n"
"    color: black;\n"
"    font: 12px \'萝莉体\';\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"SwitchButton>QLabel:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"\n"
"")
        self.SwitchButton.setChecked(True)
        self.SwitchButton.setObjectName("SwitchButton")
        self.horizontalLayout.addWidget(self.SwitchButton)

        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button = PushButton(" ? ", self)
        self.button.setFont(font)
        self.button.clicked.connect(self.showTeachingTip)
        self.horizontalLayout.addWidget(self.button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.gridLayout_6.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.SimpleCardWidget)
        self.PushButton_SF = PushButton(self.layoutWidget)
        self.PushButton_SF.setMinimumSize(QtCore.QSize(250, 25))
        self.PushButton_SF.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton_SF.setFont(font)
        self.PushButton_SF.setObjectName("PushButton_SF")
        self.verticalLayout_2.addWidget(self.PushButton_SF)

        self.setThemeBasedStyles()

        self.retranslateUi(Fui)
        QtCore.QMetaObject.connectSlotsByName(Fui)

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Success',
            content="信息已录入",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createWarningInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="无效提交",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createRepeatInfoBar(self):
        InfoBar.warning(
            title='Warning',
            content="重复提交",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def createWarningInfoBar2(self):
        InfoBar.warning(
            title='Warning',
            content="请勾选单选框",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self
        )

    def showTeachingTip(self):
        TeachingTip.create(
            target=self.button,
            icon=InfoBarIcon.INFORMATION,
            title='蛇形抖动',
            content="启用蛇形抖动，当向下移动图像时，它会来回“蛇形”\n而不是每次都从左到右。这可以减少噪声中的伪影或图案。",
            isClosable=True,
            tailPosition=TeachingTipTailPosition.BOTTOM,
            duration=2500,
            parent=self
        )

    def retranslateUi(self, Fui):
        _translate = QtCore.QCoreApplication.translate
        Fui.setWindowTitle(_translate("Fui", "Form"))
        __sortingEnabled = self.ListWidget.isSortingEnabled()
        self.ListWidget.setSortingEnabled(False)
        item = self.ListWidget.item(0)
        item.setText(_translate("Fui", "Simple2D"))
        item = self.ListWidget.item(1)
        item.setText(_translate("Fui", "FloydSteinberg"))
        item = self.ListWidget.item(2)
        item.setText(_translate("Fui", "FalseFloydSteinberg"))
        item = self.ListWidget.item(3)
        item.setText(_translate("Fui", "JarvisJudiceNinke"))
        item = self.ListWidget.item(4)
        item.setText(_translate("Fui", "Atkinson"))
        item = self.ListWidget.item(5)
        item.setText(_translate("Fui", "Stucki"))
        item = self.ListWidget.item(6)
        item.setText(_translate("Fui", "Burkes"))
        item = self.ListWidget.item(7)
        item.setText(_translate("Fui", "Sierra"))
        item = self.ListWidget.item(8)
        item.setText(_translate("Fui", "TwoRowSierra"))
        item = self.ListWidget.item(9)
        item.setText(_translate("Fui", "SierraLite"))
        item = self.ListWidget.item(10)
        item.setText(_translate("Fui", "StevenPigeon"))

        font = QtGui.QFont('萝莉体', 9)
        # 遍历 QListWidget 中的所有项并设置字体
        for i in range(self.ListWidget.count()):
            item = self.ListWidget.item(i)
            item.setFont(font)

        self.ListWidget.setSortingEnabled(__sortingEnabled)
        self.StrongBodyLabel.setText(_translate("Fui", "可选矩阵"))
        self.SubtitleLabel.setText(_translate("Fui", "Snakes"))
        self.SwitchButton.setOnText(_translate("Fui", "ON"))
        self.SwitchButton.setOffText(_translate("Fui", "OFF"))
        self.PushButton_SF.setText(_translate("Fui", "加 入 待 处 理 列 表"))

    def setThemeBasedStyles(self):
        # 设置初始样式
        StyleSheet.WINDOW.apply(self)
        # 根据当前主题更新复选框样式
        currentTheme = qconfig.theme

        if currentTheme == Theme.LIGHT:
            self.updateCheckBoxStyles("QWidget {\n"
"    background-color: black;\n"
"}\n"
"\n"
"SwitchButton {\n"
"    qproperty-spacing: 12;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"SwitchButton>QLabel {\n"
"    color: black;\n"
"    font: 12px \'萝莉体\';\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"SwitchButton>QLabel:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"\n"
"")

        elif currentTheme == Theme.DARK:
            self.updateCheckBoxStyles("QWidget {\n"
"    background-color: white;\n"
"}\n"
"\n"
"SwitchButton {\n"
"    qproperty-spacing: 12;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"SwitchButton>QLabel {\n"
"    color: white;\n"
"    font: 12px \'萝莉体\';\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"SwitchButton>QLabel:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"\n"
"")

    def updateCheckBoxStyles(self, styleSheet):
        Switch_0 = self.findChildren(SwitchButton)
        for Switch in Switch_0:
            Switch.setStyleSheet(styleSheet)


from qfluentwidgets import ListWidget, PushButton, SimpleCardWidget, StrongBodyLabel, SubtitleLabel, SwitchButton, \
    TeachingTip, TeachingTipTailPosition, InfoBarIcon, Theme, qconfig
