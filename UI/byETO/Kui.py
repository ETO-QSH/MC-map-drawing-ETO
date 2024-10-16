
import os
import ast
from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QCompleter
from qfluentwidgets.components.widgets.button import DropDownButtonBase

from qfluentwidgets import Theme, StyleSheetBase, qconfig, SpinBox, DropDownPushButton, EditableComboBox

# 定义 StyleSheet 类
class StyleSheet(StyleSheetBase, Enum):
    WINDOW = "window"
    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"qss/{theme.value.lower()}/{self.value}.qss"


class newDropDownPushButton(DropDownPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMenu(QMenu(self))
        self.selectedItem = None  # 用于存储当前选择的菜单项数据

    def mouseReleaseEvent(self, e):
        PushButton.mouseReleaseEvent(self, e)
        self._showMenu()

    def paintEvent(self, e):
        PushButton.paintEvent(self, e)
        DropDownButtonBase.paintEvent(self, e)

    def setMenu(self, menu):
        self._menu = menu
        self._menu.triggered.connect(self.onActionTriggered)

    def onActionTriggered(self, action):
        # 更新当前选择的菜单项数据
        self.selectedItem = action.data()


class CustomSpinBox(SpinBox):
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def textFromValue(self, value):
        # 调用父类的textFromValue方法获取基本的字符串表示
        base_text = super().textFromValue(value)
        # 返回修改后的文本，显示范围
        return f"{base_text} ~ {value + self.num}"

    def setValue(self, value):
        # 在设置值之前，确保值加上num不会超出范围
        max_val = self.maximum()
        if value + self.num > max_val:
            self.setMaximum(value + self.num)
        super().setValue(value)


class Ui_Kui(object):
    def setupUi(self, Kui, xx, yu, yd, zz):
        self.xx = xx
        self.yu = yu
        self.yd = yd
        self.zz = zz

        Kui.setObjectName("Kui")
        Kui.resize(450, 450)
        self.widget = QtWidgets.QWidget(Kui)
        self.widget.setGeometry(QtCore.QRect(92, 36, 286, 388))
        self.widget.setObjectName("widget")
        self.widget.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

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
        self.gridLayout_4.addWidget(self.PushButton_SFR, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.SpinBox_x = CustomSpinBox(self.xx)
        self.SpinBox_x.setValue(0)
        self.SpinBox_x.setRange(-32768, 32767)
        self.SpinBox_x.setReadOnly(True)
        self.SpinBox_x.setMinimumSize(QtCore.QSize(188, 36))
        self.SpinBox_x.setMaximumSize(QtCore.QSize(188, 36))
        self.SpinBox_x.setFocusPolicy(QtCore.Qt.ClickFocus)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SpinBox_x.setFont(font)
        self.SpinBox_x.setObjectName("SpinBox_x")
        self.gridLayout.addWidget(self.SpinBox_x, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.SpinBox_z = CustomSpinBox(self.zz)
        self.SpinBox_z.setValue(0)
        self.SpinBox_z.setRange(-32768, 32767)
        self.SpinBox_z.setReadOnly(True)
        self.SpinBox_z.setMinimumSize(QtCore.QSize(188, 36))
        self.SpinBox_z.setMaximumSize(QtCore.QSize(188, 36))
        self.SpinBox_z.setFocusPolicy(QtCore.Qt.ClickFocus)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SpinBox_z.setFont(font)
        self.SpinBox_z.setObjectName("SpinBox_z")
        self.gridLayout.addWidget(self.SpinBox_z, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.SpinBox_y = CustomSpinBox(self.yu - self.yd)
        self.SpinBox_y.setRange(-64, 319)
        self.SpinBox_y.setValue(128 + self.yd)
        self.SpinBox_y.setReadOnly(True)
        self.SpinBox_y.setMinimumSize(QtCore.QSize(188, 36))
        self.SpinBox_y.setMaximumSize(QtCore.QSize(188, 36))
        self.SpinBox_y.setFocusPolicy(QtCore.Qt.ClickFocus)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SpinBox_y.setFont(font)
        self.SpinBox_y.setObjectName("SpinBox_y")
        self.gridLayout.addWidget(self.SpinBox_y, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.BodyLabel_2 = BodyLabel(self.widget)
        self.BodyLabel_2.setMinimumSize(QtCore.QSize(60, 36))
        self.BodyLabel_2.setMaximumSize(QtCore.QSize(60, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BodyLabel_2.setFont(font)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.gridLayout.addWidget(self.BodyLabel_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.BodyLabel_3 = BodyLabel(self.widget)
        self.BodyLabel_3.setMinimumSize(QtCore.QSize(60, 36))
        self.BodyLabel_3.setMaximumSize(QtCore.QSize(60, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BodyLabel_3.setFont(font)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.gridLayout.addWidget(self.BodyLabel_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.BodyLabel_4 = BodyLabel(self.widget)
        self.BodyLabel_4.setMinimumSize(QtCore.QSize(60, 36))
        self.BodyLabel_4.setMaximumSize(QtCore.QSize(60, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BodyLabel_4.setFont(font)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.gridLayout.addWidget(self.BodyLabel_4, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.HorizontalSeparator_5 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_5.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_5.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_5.setObjectName("HorizontalSeparator_5")

        self.gridLayout_4.addWidget(self.HorizontalSeparator_5, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 3, 1, 1, 1)

        self.HorizontalSeparator_4 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_4.setMinimumSize(QtCore.QSize(256, 4))
        self.HorizontalSeparator_4.setMaximumSize(QtCore.QSize(256, 4))
        self.HorizontalSeparator_4.setObjectName("HorizontalSeparator_4")
        self.gridLayout_5.addWidget(self.HorizontalSeparator_4, 2, 1, 1, 1)

        self.VerticalSeparator = VerticalSeparator(self.widget)
        self.VerticalSeparator.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator.setObjectName("VerticalSeparator")
        self.gridLayout_5.addWidget(self.VerticalSeparator, 3, 2, 1, 1)

        self.VerticalSeparator_4 = VerticalSeparator(self.widget)
        self.VerticalSeparator_4.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_4.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_4.setObjectName("VerticalSeparator_4")
        self.gridLayout_5.addWidget(self.VerticalSeparator_4, 3, 0, 1, 1)

        self.VerticalSeparator_3 = VerticalSeparator(self.widget)
        self.VerticalSeparator_3.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_3.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_3.setObjectName("VerticalSeparator_3")
        self.gridLayout_5.addWidget(self.VerticalSeparator_3, 1, 0, 1, 1)

        self.VerticalSeparator_2 = VerticalSeparator(self.widget)
        self.VerticalSeparator_2.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_2.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_2.setObjectName("VerticalSeparator_2")
        self.gridLayout_5.addWidget(self.VerticalSeparator_2, 1, 2, 1, 1)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.LineEdit_R = LineEdit(self.widget)
        self.LineEdit_R.setText("-64:bedrock;-63:dirt;-62:dirt;-61:grass_block")
        self.LineEdit_R.setMinimumSize(QtCore.QSize(188, 36))
        self.LineEdit_R.setMaximumSize(QtCore.QSize(188, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit_R.setFont(font)
        self.LineEdit_R.setObjectName("LineEdit_R")
        self.gridLayout_2.addWidget(self.LineEdit_R, 0, 0, 1, 1)

        self.PushButton_K = PushButton(self.widget)
        self.PushButton_K.setMinimumSize(QtCore.QSize(60, 36))
        self.PushButton_K.setMaximumSize(QtCore.QSize(60, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton_K.setFont(font)
        self.PushButton_K.setObjectName("PushButton")
        self.gridLayout_2.addWidget(self.PushButton_K, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 1)

        self.RadioButton_1 = RadioButton(self.widget)
        self.RadioButton_1.setMinimumSize(QtCore.QSize(256, 36))
        self.RadioButton_1.setMaximumSize(QtCore.QSize(256, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RadioButton_1.setFont(font)
        self.RadioButton_1.setStyleSheet(
            "RadioButton {\n"
            "    min-height: 24px;\n"
            "    max-height: 24px;\n"
            "    background-color: transparent;\n"
            "    font: 15px \'萝莉体\';\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "RadioButton::indicator {\n"
            "    width: 9px;\n"
            "    height: 9px;\n"
            "    border-radius: 6px;\n"
            "    border: 2px solid #999999;\n"
            "    background-color: rgba(0, 0, 0, 5);\n"
            "    margin-right: 3px;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:hover {\n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "RadioButton::indicator:pressed {\n"
            "    border: 2px solid #bbbbbb;\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:checked {\n"
            "    width: 9px;\n"
            "    height: 9px;\n"
            "    border-radius: 6px;\n"
            "    border: 2px solid #999999;\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:checked:hover {\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:checked:pressed {\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton:disabled {\n"
            "    color: rgba(0, 0, 0, 110);\n"
            "}\n"
            "\n"
            "RadioButton::indicator:disabled {\n"
            "    border: 2px solid #bbbbbb;\n"
            "    background-color: transparent;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:disabled:checked {\n"
            "    border: none;\n"
            "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
            "            stop:0 rgb(255, 255, 255),\n"
            "            stop:0.5 rgb(255, 255, 255),\n"
            "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
            "            stop:1 rgba(0, 0, 0, 0.2169));\n"
            "}\n"
            "")
        self.RadioButton_1.setObjectName("RadioButton_1")
        self.gridLayout_3.addWidget(self.RadioButton_1, 1, 0, 1, 1)

        self.RadioButton_2 = RadioButton(self.widget)
        self.RadioButton_2.setMinimumSize(QtCore.QSize(256, 36))
        self.RadioButton_2.setMaximumSize(QtCore.QSize(256, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RadioButton_2.setFont(font)
        self.RadioButton_2.setStyleSheet(
            "RadioButton {\n"
            "    min-height: 24px;\n"
            "    max-height: 24px;\n"
            "    background-color: transparent;\n"
            "    font: 15px \'萝莉体\';\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "RadioButton::indicator {\n"
            "    width: 9px;\n"
            "    height: 9px;\n"
            "    border-radius: 6px;\n"
            "    border: 2px solid #999999;\n"
            "    background-color: rgba(0, 0, 0, 5);\n"
            "    margin-right: 3px;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:hover {\n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "RadioButton::indicator:pressed {\n"
            "    border: 2px solid #bbbbbb;\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:checked {\n"
            "    width: 9px;\n"
            "    height: 9px;\n"
            "    border-radius: 6px;\n"
            "    border: 2px solid #999999;\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:checked:hover {\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:checked:pressed {\n"
            "    background-color: #ffbfbf;\n"
            "}\n"
            "\n"
            "RadioButton:disabled {\n"
            "    color: rgba(0, 0, 0, 110);\n"
            "}\n"
            "\n"
            "RadioButton::indicator:disabled {\n"
            "    border: 2px solid #bbbbbb;\n"
            "    background-color: transparent;\n"
            "}\n"
            "\n"
            "RadioButton::indicator:disabled:checked {\n"
            "    border: none;\n"
            "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
            "            stop:0 rgb(255, 255, 255),\n"
            "            stop:0.5 rgb(255, 255, 255),\n"
            "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
            "            stop:1 rgba(0, 0, 0, 0.2169));\n"
            "}\n"
            "")
        self.RadioButton_2.setObjectName("RadioButton_2")
        self.gridLayout_3.addWidget(self.RadioButton_2, 3, 0, 1, 1)

        self.ComboBox = EditableComboBox(self.widget)
        self.ComboBox.setMinimumSize(QtCore.QSize(256, 36))
        self.ComboBox.setMaximumSize(QtCore.QSize(256, 36))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ComboBox.setFont(font)
        self.ComboBox.setObjectName("ComboBox")
        self.gridLayout_3.addWidget(self.ComboBox, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 1, 1, 1)

        with open('./data/BlockList.json', 'r', encoding="utf-8") as file:
            data = ast.literal_eval(file.read())["BlockList"]
        for i, item in enumerate(data):
            self.ComboBox.addItem(f'{item["name"]} ({item["id"].split(":")[1]})', userData=item["id"].split(':')[1])
            self.ComboBox.setItemIcon(i, QIcon(os.path.join('./icon', item["icon"])))
        self.ComboBox.currentIndexChanged.connect(lambda index: print(self.ComboBox.currentText())) # 当前选项的索引改变信号
        self.ComboBox.setCompleter(QCompleter([item["name"] for item in data], self.ComboBox)) # 设置补全器

        # 不生效的说 byETO
        # for item in self.ComboBox.items:
        #     item.setFont(QFont('萝莉体', 10))

        self.HorizontalSeparator_2 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_2.setMinimumSize(QtCore.QSize(256, 4))
        self.HorizontalSeparator_2.setMaximumSize(QtCore.QSize(256, 4))
        self.HorizontalSeparator_2.setObjectName("HorizontalSeparator_2")
        self.gridLayout_5.addWidget(self.HorizontalSeparator_2, 4, 1, 1, 1)

        self.HorizontalSeparator_3 = HorizontalSeparator(self.widget)
        self.HorizontalSeparator_3.setMinimumSize(QtCore.QSize(256, 4))
        self.HorizontalSeparator_3.setMaximumSize(QtCore.QSize(256, 4))
        self.HorizontalSeparator_3.setObjectName("HorizontalSeparator_3")
        self.gridLayout_5.addWidget(self.HorizontalSeparator_3, 0, 1, 1, 1)

        self.setThemeBasedStyles()

        self.retranslateUi(Kui)
        QtCore.QMetaObject.connectSlotsByName(Kui)

    def retranslateUi(self, Kui):
        _translate = QtCore.QCoreApplication.translate
        Kui.setWindowTitle(_translate("Kui", "Form"))
        self.PushButton_SFR.setText(_translate("Kui", "生 成 地 图 存 档 文 件"))
        self.BodyLabel_2.setText(_translate("Kui", "X-Chunk"))
        self.BodyLabel_3.setText(_translate("Kui", " Y-Block"))
        self.BodyLabel_4.setText(_translate("Kui", "Z-Chunk"))
        self.PushButton_K.setText(_translate("Kui", "重置"))
        self.RadioButton_1.setText(_translate("Kui", "选择背景层"))
        self.RadioButton_2.setText(_translate("Kui", "编辑所有层"))

    def setThemeBasedStyles(self):
        # 设置初始样式
        StyleSheet.WINDOW.apply(self)
        # 根据当前主题更新复选框样式
        currentTheme = qconfig.theme

        if currentTheme == Theme.LIGHT:
            self.updateCheckBoxStyles(
                "RadioButton {\n"
                "    min-height: 24px;\n"
                "    max-height: 24px;\n"
                "    background-color: transparent;\n"
                "    font: 15px \'萝莉体\';\n"
                "    color: black;\n"
                "}\n"
                "\n"
                "RadioButton::indicator {\n"
                "    width: 9px;\n"
                "    height: 9px;\n"
                "    border-radius: 6px;\n"
                "    border: 2px solid #999999;\n"
                "    background-color: rgba(0, 0, 0, 5);\n"
                "    margin-right: 3px;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:hover {\n"
                "    background-color: rgba(0, 0, 0, 0);\n"
                "}\n"
                "\n"
                "RadioButton::indicator:pressed {\n"
                "    border: 2px solid #bbbbbb;\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:checked {\n"
                "    width: 9px;\n"
                "    height: 9px;\n"
                "    border-radius: 6px;\n"
                "    border: 2px solid #999999;\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:checked:hover {\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:checked:pressed {\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton:disabled {\n"
                "    color: rgba(0, 0, 0, 110);\n"
                "}\n"
                "\n"
                "RadioButton::indicator:disabled {\n"
                "    border: 2px solid #bbbbbb;\n"
                "    background-color: transparent;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:disabled:checked {\n"
                "    border: none;\n"
                "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                "            stop:0 rgb(255, 255, 255),\n"
                "            stop:0.5 rgb(255, 255, 255),\n"
                "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
                "            stop:1 rgba(0, 0, 0, 0.2169));\n"
                "}\n"
                "")

        elif currentTheme == Theme.DARK:
            self.updateCheckBoxStyles(
                "RadioButton {\n"
                "    min-height: 24px;\n"
                "    max-height: 24px;\n"
                "    background-color: transparent;\n"
                "    font: 15px \'萝莉体\';\n"
                "    color: white;\n"
                "}\n"
                "\n"
                "RadioButton::indicator {\n"
                "    width: 9px;\n"
                "    height: 9px;\n"
                "    border-radius: 6px;\n"
                "    border: 2px solid #999999;\n"
                "    background-color: rgba(0, 0, 0, 5);\n"
                "    margin-right: 3px;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:hover {\n"
                "    background-color: rgba(0, 0, 0, 0);\n"
                "}\n"
                "\n"
                "RadioButton::indicator:pressed {\n"
                "    border: 2px solid #bbbbbb;\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:checked {\n"
                "    width: 9px;\n"
                "    height: 9px;\n"
                "    border-radius: 6px;\n"
                "    border: 2px solid #999999;\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:checked:hover {\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:checked:pressed {\n"
                "    background-color: #ffbfbf;\n"
                "}\n"
                "\n"
                "RadioButton:disabled {\n"
                "    color: rgba(0, 0, 0, 110);\n"
                "}\n"
                "\n"
                "RadioButton::indicator:disabled {\n"
                "    border: 2px solid #bbbbbb;\n"
                "    background-color: transparent;\n"
                "}\n"
                "\n"
                "RadioButton::indicator:disabled:checked {\n"
                "    border: none;\n"
                "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                "            stop:0 rgb(255, 255, 255),\n"
                "            stop:0.5 rgb(255, 255, 255),\n"
                "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
                "            stop:1 rgba(0, 0, 0, 0.2169));\n"
                "}\n"
                "")
    def updateCheckBoxStyles(self, styleSheet):
        Radio_0 = self.findChildren(RadioButton)
        for Switch in Radio_0:
            Switch.setStyleSheet(styleSheet)

from qfluentwidgets import BodyLabel, HorizontalSeparator, LineEdit, PushButton, RadioButton, VerticalSeparator
