
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Dui(object):
    def setupUi(self, Dui):
        Dui.setObjectName("Dui")
        Dui.resize(426, 405)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        Dui.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Dui)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 252, 303))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(self.layoutWidget)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(225, 270))
        self.SimpleCardWidget.setMaximumSize(QtCore.QSize(250, 270))
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
"    color: rgb(225, 225, 225);\n"
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
        self.TreeWidget.setDragEnabled(False)
        self.TreeWidget.setAutoExpandDelay(-1)
        self.TreeWidget.setIndentation(5)
        self.TreeWidget.setRootIsDecorated(True)
        self.TreeWidget.setUniformRowHeights(False)
        self.TreeWidget.setAnimated(True)
        self.TreeWidget.setAllColumnsShowFocus(False)
        self.TreeWidget.setWordWrap(False)
        self.TreeWidget.setHeaderHidden(False)
        self.TreeWidget.setColumnCount(1)
        self.TreeWidget.setObjectName("TreeWidget")
        self.TreeWidget.headerItem().setText(0, "可选矩阵")
        item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.TreeWidget.header().setVisible(False)
        self.TreeWidget.header().setCascadingSectionResizes(False)
        self.TreeWidget.header().setHighlightSections(False)
        self.gridLayout_6.addWidget(self.TreeWidget, 0, 1, 1, 1)
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

        self.retranslateUi(Dui)
        QtCore.QMetaObject.connectSlotsByName(Dui)

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Success',
            content="信息已录入",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
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

    def retranslateUi(self, Dui):
        _translate = QtCore.QCoreApplication.translate
        Dui.setWindowTitle(_translate("Dui", "Form"))
        self.TreeWidget.setSortingEnabled(False)
        __sortingEnabled = self.TreeWidget.isSortingEnabled()
        self.TreeWidget.setSortingEnabled(False)
        self.TreeWidget.topLevelItem(0).setText(0, _translate("Dui", "1. 特殊矩阵"))
        self.TreeWidget.topLevelItem(0).child(0).setText(0, _translate("Dui", "  3x5"))
        self.TreeWidget.topLevelItem(0).child(1).setText(0, _translate("Dui", "  5x3"))
        self.TreeWidget.topLevelItem(0).child(2).setText(0, _translate("Dui", "  5x5"))
        self.TreeWidget.topLevelItem(1).setText(0, _translate("Dui", "2. 二幂矩阵"))
        self.TreeWidget.topLevelItem(1).child(0).setText(0, _translate("Dui", "  2x2"))
        self.TreeWidget.topLevelItem(1).child(1).setText(0, _translate("Dui", "  4x4"))
        self.TreeWidget.topLevelItem(1).child(2).setText(0, _translate("Dui", "  8x8"))
        self.TreeWidget.topLevelItem(1).child(3).setText(0, _translate("Dui", "16x16"))
        self.TreeWidget.topLevelItem(1).child(4).setText(0, _translate("Dui", "32x32"))
        self.TreeWidget.topLevelItem(1).child(5).setText(0, _translate("Dui", "64x64"))

        font = QtGui.QFont('萝莉体', 9)
        self.TreeWidget.topLevelItem(0).setFont(0, font)
        self.TreeWidget.topLevelItem(1).setFont(0, font)
        self.TreeWidget.topLevelItem(0).child(0).setFont(0, font)
        self.TreeWidget.topLevelItem(0).child(1).setFont(0, font)
        self.TreeWidget.topLevelItem(0).child(2).setFont(0, font)
        self.TreeWidget.topLevelItem(1).child(0).setFont(0, font)
        self.TreeWidget.topLevelItem(1).child(1).setFont(0, font)
        self.TreeWidget.topLevelItem(1).child(2).setFont(0, font)
        self.TreeWidget.topLevelItem(1).child(3).setFont(0, font)
        self.TreeWidget.topLevelItem(1).child(4).setFont(0, font)
        self.TreeWidget.topLevelItem(1).child(5).setFont(0, font)
        self.TreeWidget.setSortingEnabled(__sortingEnabled)

        # 在初始化时调用
        for i in range(self.TreeWidget.topLevelItemCount()):
            item = self.TreeWidget.topLevelItem(i)
            self.expandAll(item)

        self.PushButton_SF.setText(_translate("Dui", "加 入 待 处 理 列 表"))

    def expandAll(self, item):
        item.setExpanded(True)
        for i in range(item.childCount()):
            self.expandAll(item.child(i))

from qfluentwidgets import PushButton, SimpleCardWidget, TreeWidget, InfoBar, InfoBarPosition
