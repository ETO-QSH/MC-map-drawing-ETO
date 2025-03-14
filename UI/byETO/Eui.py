
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Eui(object):
    def setupUi(self, Eui):
        Eui.setObjectName("Eui")
        Eui.resize(419, 371)
        self.layoutWidget = QtWidgets.QWidget(Eui)
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
        self.ListWidget.setObjectName("ListWidget_E")
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
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget.addItem(item)
        self.gridLayout_6.addWidget(self.ListWidget, 1, 0, 1, 1)
        self.StrongBodyLabel = StrongBodyLabel(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.StrongBodyLabel.setFont(font)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.gridLayout_6.addWidget(self.StrongBodyLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
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

        self.retranslateUi(Eui)
        QtCore.QMetaObject.connectSlotsByName(Eui)

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

    def retranslateUi(self, Eui):
        _translate = QtCore.QCoreApplication.translate
        Eui.setWindowTitle(_translate("Eui", "Form"))
        __sortingEnabled = self.ListWidget.isSortingEnabled()
        self.ListWidget.setSortingEnabled(False)
        item = self.ListWidget.item(0)
        item.setText(_translate("Eui", "ClusteredDot4x4"))
        item = self.ListWidget.item(1)
        item.setText(_translate("Eui", "ClusteredDotDiagonal8x8"))
        item = self.ListWidget.item(2)
        item.setText(_translate("Eui", "Vertical5x3"))
        item = self.ListWidget.item(3)
        item.setText(_translate("Eui", "Horizontal3x5"))
        item = self.ListWidget.item(4)
        item.setText(_translate("Eui", "ClusteredDotDiagonal6x6"))
        item = self.ListWidget.item(5)
        item.setText(_translate("Eui", "ClusteredDotDiagonal8x8_2"))
        item = self.ListWidget.item(6)
        item.setText(_translate("Eui", "ClusteredDotDiagonal16x16"))
        item = self.ListWidget.item(7)
        item.setText(_translate("Eui", "ClusteredDot6x6"))
        item = self.ListWidget.item(8)
        item.setText(_translate("Eui", "ClusteredDotSpiral5x5"))
        item = self.ListWidget.item(9)
        item.setText(_translate("Eui", "ClusteredDotHorizontalLine"))
        item = self.ListWidget.item(10)
        item.setText(_translate("Eui", "ClusteredDotVerticalLine"))
        item = self.ListWidget.item(11)
        item.setText(_translate("Eui", "ClusteredDot8x8"))
        item = self.ListWidget.item(12)
        item.setText(_translate("Eui", "ClusteredDot6x6_2"))
        item = self.ListWidget.item(13)
        item.setText(_translate("Eui", "ClusteredDot6x6_3"))
        item = self.ListWidget.item(14)
        item.setText(_translate("Eui", "ClusteredDotDiagonal8x8_3"))

        font = QtGui.QFont('萝莉体', 9)
        # 遍历 QListWidget 中的所有项并设置字体
        for i in range(self.ListWidget.count()):
            item = self.ListWidget.item(i)
            item.setFont(font)

        self.ListWidget.setSortingEnabled(__sortingEnabled)
        self.StrongBodyLabel.setText(_translate("Eui", "可选矩阵"))
        self.PushButton_SF.setText(_translate("Eui", "加 入 待 处 理 列 表"))
from qfluentwidgets import ListWidget, PushButton, SimpleCardWidget, StrongBodyLabel, InfoBar, InfoBarPosition
