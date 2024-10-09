
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bui(object):
    def setupUi(self, Bui):
        Bui.setObjectName("Bui")
        Bui.resize(960, 750)
        Bui.setMinimumSize(QtCore.QSize(0, 0))
        Bui.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        Bui.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Bui)
        self.layoutWidget.setGeometry(QtCore.QRect(143, 33, 675, 575))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.TitleLabel = TitleLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setTabletTracking(False)
        self.TitleLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.SimpleCardWidget = SimpleCardWidget(self.layoutWidget)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(660, 80))
        self.SimpleCardWidget.setMaximumSize(QtCore.QSize(660, 80))
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.SimpleCardWidget)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.BodyLabel = BodyLabel(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.BodyLabel.setFont(font)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridLayout_16.addWidget(self.BodyLabel, 0, 0, 1, 1)
        self.PushButton = PushButton(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton.setFont(font)
        self.PushButton.setObjectName("PushButton")
        self.gridLayout_16.addWidget(self.PushButton, 0, 1, 1, 1)
        self.CaptionLabel = CaptionLabel(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel.setFont(font)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.gridLayout_16.addWidget(self.CaptionLabel, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.SimpleCardWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.SingleDirectionScrollArea = SingleDirectionScrollArea(self.layoutWidget)
        self.SingleDirectionScrollArea.setMinimumSize(QtCore.QSize(665, 360))
        self.SingleDirectionScrollArea.setMaximumSize(QtCore.QSize(665, 4925))
        self.SingleDirectionScrollArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.SingleDirectionScrollArea.setStyleSheet("background-color: transparent;")
        self.SingleDirectionScrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.SingleDirectionScrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SingleDirectionScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.SingleDirectionScrollArea.setWidgetResizable(True)
        self.SingleDirectionScrollArea.setObjectName("SingleDirectionScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -1290, 650, 4925))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(650, 4925))
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(650, 4925))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 650, 4924))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.VerticalSeparator_28 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_28.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_28.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_28.setObjectName("VerticalSeparator_28")
        self.gridLayout_15.addWidget(self.VerticalSeparator_28, 69, 2, 1, 1)
        self.HorizontalSeparator_92 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_92.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_92.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_92.setObjectName("HorizontalSeparator_92")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_92, 94, 1, 1, 1)
        self.gridLayout_56 = QtWidgets.QGridLayout()
        self.gridLayout_56.setObjectName("gridLayout_56")
        spacerItem3 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_56.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_56.addItem(spacerItem4, 1, 2, 1, 1)
        self.CardWidget_295 = CardWidget(self.layoutWidget1)
        self.CardWidget_295.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_295.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_295.setObjectName("CardWidget_295")
        self.black_terracotta = CheckBox(self.CardWidget_295)
        self.black_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.black_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.black_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.black_terracotta.setFont(font)
        self.black_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/black_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.black_terracotta.setIcon(icon)
        self.black_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.black_terracotta.setChecked(True)
        self.black_terracotta.setTristate(False)
        self.black_terracotta.setObjectName("black_terracotta")
        self.gridLayout_56.addWidget(self.CardWidget_295, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_56.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_56.addItem(spacerItem6, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_56, 103, 3, 1, 1)
        self.VerticalSeparator_8 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_8.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_8.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_8.setObjectName("VerticalSeparator_8")
        self.gridLayout_15.addWidget(self.VerticalSeparator_8, 109, 2, 1, 1)
        self.CardWidget_54 = CardWidget(self.layoutWidget1)
        self.CardWidget_54.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_54.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_54.setObjectName("CardWidget_54")
        self.layoutWidget_103 = QtWidgets.QWidget(self.CardWidget_54)
        self.layoutWidget_103.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_103.setObjectName("layoutWidget_103")
        self.horizontalLayout_111 = QtWidgets.QHBoxLayout(self.layoutWidget_103)
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_111.setObjectName("horizontalLayout_111")
        self.PixmapLabel_60 = PixmapLabel(self.layoutWidget_103)
        self.PixmapLabel_60.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_60.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_60.setObjectName("PixmapLabel_60")
        self.horizontalLayout_111.addWidget(self.PixmapLabel_60)
        self.CheckBox_B42 = CheckBox(self.layoutWidget_103)
        self.CheckBox_B42.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B42.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B42.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B42.setChecked(True)
        self.CheckBox_B42.setObjectName("CheckBox_B42")
        self.horizontalLayout_111.addWidget(self.CheckBox_B42)
        self.gridLayout_15.addWidget(self.CardWidget_54, 85, 1, 1, 1)
        self.CardWidget_46 = CardWidget(self.layoutWidget1)
        self.CardWidget_46.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_46.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_46.setObjectName("CardWidget_46")
        self.layoutWidget_87 = QtWidgets.QWidget(self.CardWidget_46)
        self.layoutWidget_87.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_87.setObjectName("layoutWidget_87")
        self.horizontalLayout_95 = QtWidgets.QHBoxLayout(self.layoutWidget_87)
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_95.setObjectName("horizontalLayout_95")
        self.PixmapLabel_52 = PixmapLabel(self.layoutWidget_87)
        self.PixmapLabel_52.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_52.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_52.setObjectName("PixmapLabel_52")
        self.horizontalLayout_95.addWidget(self.PixmapLabel_52)
        self.CheckBox_B34 = CheckBox(self.layoutWidget_87)
        self.CheckBox_B34.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B34.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B34.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B34.setChecked(True)
        self.CheckBox_B34.setObjectName("CheckBox_B34")
        self.horizontalLayout_95.addWidget(self.CheckBox_B34)
        self.gridLayout_15.addWidget(self.CardWidget_46, 69, 1, 1, 1)
        self.VerticalSeparator_21 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_21.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_21.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_21.setObjectName("VerticalSeparator_21")
        self.gridLayout_15.addWidget(self.VerticalSeparator_21, 83, 2, 1, 1)
        self.VerticalSeparator_4 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_4.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_4.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_4.setObjectName("VerticalSeparator_4")
        self.gridLayout_15.addWidget(self.VerticalSeparator_4, 119, 2, 1, 1)
        self.CardWidget_60 = CardWidget(self.layoutWidget1)
        self.CardWidget_60.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_60.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_60.setObjectName("CardWidget_60")
        self.layoutWidget_115 = QtWidgets.QWidget(self.CardWidget_60)
        self.layoutWidget_115.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_115.setObjectName("layoutWidget_115")
        self.horizontalLayout_123 = QtWidgets.QHBoxLayout(self.layoutWidget_115)
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_123.setObjectName("horizontalLayout_123")
        self.PixmapLabel_66 = PixmapLabel(self.layoutWidget_115)
        self.PixmapLabel_66.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_66.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_66.setObjectName("PixmapLabel_66")
        self.horizontalLayout_123.addWidget(self.PixmapLabel_66)
        self.CheckBox_B48 = CheckBox(self.layoutWidget_115)
        self.CheckBox_B48.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B48.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B48.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B48.setChecked(True)
        self.CheckBox_B48.setObjectName("CheckBox_B48")
        self.horizontalLayout_123.addWidget(self.CheckBox_B48)
        self.gridLayout_15.addWidget(self.CardWidget_60, 97, 1, 1, 1)
        self.VerticalSeparator_40 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_40.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_40.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_40.setObjectName("VerticalSeparator_40")
        self.gridLayout_15.addWidget(self.VerticalSeparator_40, 45, 2, 1, 1)
        self.HorizontalSeparator_40 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_40.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_40.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_40.setObjectName("HorizontalSeparator_40")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_40, 40, 3, 1, 1)
        self.HorizontalSeparator_90 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_90.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_90.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_90.setObjectName("HorizontalSeparator_90")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_90, 92, 1, 1, 1)
        self.VerticalSeparator = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator.setObjectName("VerticalSeparator")
        self.gridLayout_15.addWidget(self.VerticalSeparator, 113, 2, 1, 1)
        self.VerticalSeparator_33 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_33.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_33.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_33.setObjectName("VerticalSeparator_33")
        self.gridLayout_15.addWidget(self.VerticalSeparator_33, 59, 2, 1, 1)
        self.HorizontalSeparator_8 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_8.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_8.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_8.setObjectName("HorizontalSeparator_8")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_8, 8, 3, 1, 1)
        self.CardWidget_37 = CardWidget(self.layoutWidget1)
        self.CardWidget_37.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_37.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_37.setObjectName("CardWidget_37")
        self.layoutWidget_69 = QtWidgets.QWidget(self.CardWidget_37)
        self.layoutWidget_69.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_69.setObjectName("layoutWidget_69")
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout(self.layoutWidget_69)
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.PixmapLabel_43 = PixmapLabel(self.layoutWidget_69)
        self.PixmapLabel_43.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_43.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_43.setObjectName("PixmapLabel_43")
        self.horizontalLayout_77.addWidget(self.PixmapLabel_43)
        self.CheckBox_B25 = CheckBox(self.layoutWidget_69)
        self.CheckBox_B25.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B25.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B25.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B25.setChecked(True)
        self.CheckBox_B25.setObjectName("CheckBox_B25")
        self.horizontalLayout_77.addWidget(self.CheckBox_B25)
        self.gridLayout_15.addWidget(self.CardWidget_37, 51, 1, 1, 1)
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.CardWidget_216 = CardWidget(self.layoutWidget1)
        self.CardWidget_216.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_216.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_216.setObjectName("CardWidget_216")
        self.light_blue_concrete = CheckBox(self.CardWidget_216)
        self.light_blue_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_blue_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.light_blue_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_blue_concrete.setFont(font)
        self.light_blue_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/light_blue_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_blue_concrete.setIcon(icon1)
        self.light_blue_concrete.setIconSize(QtCore.QSize(16, 16))
        self.light_blue_concrete.setChecked(True)
        self.light_blue_concrete.setTristate(False)
        self.light_blue_concrete.setObjectName("light_blue_concrete")
        self.gridLayout_27.addWidget(self.CardWidget_216, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_27.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_27.addItem(spacerItem8, 0, 1, 1, 1)
        self.CardWidget_217 = CardWidget(self.layoutWidget1)
        self.CardWidget_217.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_217.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_217.setObjectName("CardWidget_217")
        self.light_blue_wool = CheckBox(self.CardWidget_217)
        self.light_blue_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_blue_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.light_blue_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_blue_wool.setFont(font)
        self.light_blue_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/light_blue_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_blue_wool.setIcon(icon2)
        self.light_blue_wool.setIconSize(QtCore.QSize(16, 16))
        self.light_blue_wool.setTristate(False)
        self.light_blue_wool.setObjectName("light_blue_wool")
        self.gridLayout_27.addWidget(self.CardWidget_217, 1, 1, 1, 1)
        self.CardWidget_218 = CardWidget(self.layoutWidget1)
        self.CardWidget_218.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_218.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_218.setObjectName("CardWidget_218")
        self.light_blue_stained_glass = CheckBox(self.CardWidget_218)
        self.light_blue_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_blue_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.light_blue_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_blue_stained_glass.setFont(font)
        self.light_blue_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/light_blue_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_blue_stained_glass.setIcon(icon3)
        self.light_blue_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.light_blue_stained_glass.setTristate(False)
        self.light_blue_stained_glass.setObjectName("light_blue_stained_glass")
        self.gridLayout_27.addWidget(self.CardWidget_218, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_27, 35, 3, 1, 1)
        self.gridLayout_39 = QtWidgets.QGridLayout()
        self.gridLayout_39.setObjectName("gridLayout_39")
        spacerItem9 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_39.addItem(spacerItem9, 1, 2, 1, 1)
        self.CardWidget_198 = CardWidget(self.layoutWidget1)
        self.CardWidget_198.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_198.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_198.setObjectName("CardWidget_198")
        self.spruce_planks = CheckBox(self.CardWidget_198)
        self.spruce_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.spruce_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.spruce_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spruce_planks.setFont(font)
        self.spruce_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/spruce_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spruce_planks.setIcon(icon4)
        self.spruce_planks.setIconSize(QtCore.QSize(16, 16))
        self.spruce_planks.setTristate(False)
        self.spruce_planks.setObjectName("spruce_planks")
        self.gridLayout_39.addWidget(self.CardWidget_198, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_39.addItem(spacerItem10, 2, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_39.addItem(spacerItem11, 0, 1, 1, 1)
        self.CardWidget_199 = CardWidget(self.layoutWidget1)
        self.CardWidget_199.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_199.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_199.setObjectName("CardWidget_199")
        self.podzol = CheckBox(self.CardWidget_199)
        self.podzol.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.podzol.setMinimumSize(QtCore.QSize(17, 16))
        self.podzol.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.podzol.setFont(font)
        self.podzol.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/podzol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.podzol.setIcon(icon5)
        self.podzol.setIconSize(QtCore.QSize(16, 16))
        self.podzol.setChecked(True)
        self.podzol.setTristate(False)
        self.podzol.setObjectName("podzol")
        self.gridLayout_39.addWidget(self.CardWidget_199, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_39, 69, 3, 1, 1)
        self.gridLayout_57 = QtWidgets.QGridLayout()
        self.gridLayout_57.setObjectName("gridLayout_57")
        spacerItem12 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_57.addItem(spacerItem12, 1, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_57.addItem(spacerItem13, 1, 2, 1, 1)
        self.CardWidget_296 = CardWidget(self.layoutWidget1)
        self.CardWidget_296.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_296.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_296.setObjectName("CardWidget_296")
        self.crimson_nylium = CheckBox(self.CardWidget_296)
        self.crimson_nylium.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.crimson_nylium.setMinimumSize(QtCore.QSize(17, 16))
        self.crimson_nylium.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.crimson_nylium.setFont(font)
        self.crimson_nylium.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/crimson_nylium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crimson_nylium.setIcon(icon6)
        self.crimson_nylium.setIconSize(QtCore.QSize(16, 16))
        self.crimson_nylium.setChecked(True)
        self.crimson_nylium.setTristate(False)
        self.crimson_nylium.setObjectName("crimson_nylium")
        self.gridLayout_57.addWidget(self.CardWidget_296, 1, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_57.addItem(spacerItem14, 2, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_57.addItem(spacerItem15, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_57, 105, 3, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.CardWidget_233 = CardWidget(self.layoutWidget1)
        self.CardWidget_233.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_233.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_233.setObjectName("CardWidget_233")
        self.cyan_concrete = CheckBox(self.CardWidget_233)
        self.cyan_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.cyan_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.cyan_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cyan_concrete.setFont(font)
        self.cyan_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/cyan_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cyan_concrete.setIcon(icon7)
        self.cyan_concrete.setIconSize(QtCore.QSize(16, 16))
        self.cyan_concrete.setChecked(True)
        self.cyan_concrete.setTristate(False)
        self.cyan_concrete.setObjectName("cyan_concrete")
        self.gridLayout_19.addWidget(self.CardWidget_233, 1, 0, 1, 1)
        self.CardWidget_234 = CardWidget(self.layoutWidget1)
        self.CardWidget_234.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_234.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_234.setObjectName("CardWidget_234")
        self.cyan_stained_glass = CheckBox(self.CardWidget_234)
        self.cyan_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.cyan_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.cyan_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cyan_stained_glass.setFont(font)
        self.cyan_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/cyan_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cyan_stained_glass.setIcon(icon8)
        self.cyan_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.cyan_stained_glass.setTristate(False)
        self.cyan_stained_glass.setObjectName("cyan_stained_glass")
        self.gridLayout_19.addWidget(self.CardWidget_234, 1, 2, 1, 1)
        self.CardWidget_235 = CardWidget(self.layoutWidget1)
        self.CardWidget_235.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_235.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_235.setObjectName("CardWidget_235")
        self.prismarine = CheckBox(self.CardWidget_235)
        self.prismarine.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.prismarine.setMinimumSize(QtCore.QSize(17, 16))
        self.prismarine.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prismarine.setFont(font)
        self.prismarine.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/prismarine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prismarine.setIcon(icon9)
        self.prismarine.setIconSize(QtCore.QSize(16, 16))
        self.prismarine.setTristate(False)
        self.prismarine.setObjectName("prismarine")
        self.gridLayout_19.addWidget(self.CardWidget_235, 3, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem16, 4, 1, 1, 1)
        self.CardWidget_236 = CardWidget(self.layoutWidget1)
        self.CardWidget_236.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_236.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_236.setObjectName("CardWidget_236")
        self.cyan_wool = CheckBox(self.CardWidget_236)
        self.cyan_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.cyan_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.cyan_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cyan_wool.setFont(font)
        self.cyan_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/cyan_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cyan_wool.setIcon(icon10)
        self.cyan_wool.setIconSize(QtCore.QSize(16, 16))
        self.cyan_wool.setTristate(False)
        self.cyan_wool.setObjectName("cyan_wool")
        self.gridLayout_19.addWidget(self.CardWidget_236, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem17, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_19, 47, 3, 1, 1)
        self.HorizontalSeparator_33 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_33.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_33.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_33.setObjectName("HorizontalSeparator_33")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_33, 34, 1, 1, 1)
        self.HorizontalSeparator_122 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_122.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_122.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_122.setObjectName("HorizontalSeparator_122")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_122, 122, 3, 1, 1)
        self.gridLayout_43 = QtWidgets.QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        spacerItem18 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_43.addItem(spacerItem18, 1, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_43.addItem(spacerItem19, 1, 2, 1, 1)
        self.CardWidget_201 = CardWidget(self.layoutWidget1)
        self.CardWidget_201.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_201.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_201.setObjectName("CardWidget_201")
        self.magenta_terracotta = CheckBox(self.CardWidget_201)
        self.magenta_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.magenta_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.magenta_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.magenta_terracotta.setFont(font)
        self.magenta_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/magenta_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.magenta_terracotta.setIcon(icon11)
        self.magenta_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.magenta_terracotta.setChecked(True)
        self.magenta_terracotta.setTristate(False)
        self.magenta_terracotta.setObjectName("magenta_terracotta")
        self.gridLayout_43.addWidget(self.CardWidget_201, 1, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_43.addItem(spacerItem20, 2, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_43.addItem(spacerItem21, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_43, 77, 3, 1, 1)
        self.gridLayout_59 = QtWidgets.QGridLayout()
        self.gridLayout_59.setObjectName("gridLayout_59")
        spacerItem22 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_59.addItem(spacerItem22, 1, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_59.addItem(spacerItem23, 1, 2, 1, 1)
        self.CardWidget_298 = CardWidget(self.layoutWidget1)
        self.CardWidget_298.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_298.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_298.setObjectName("CardWidget_298")
        self.stripped_crimson_hyphae = CheckBox(self.CardWidget_298)
        self.stripped_crimson_hyphae.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.stripped_crimson_hyphae.setMinimumSize(QtCore.QSize(17, 16))
        self.stripped_crimson_hyphae.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stripped_crimson_hyphae.setFont(font)
        self.stripped_crimson_hyphae.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/stripped_crimson_hyphae.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stripped_crimson_hyphae.setIcon(icon12)
        self.stripped_crimson_hyphae.setIconSize(QtCore.QSize(16, 16))
        self.stripped_crimson_hyphae.setChecked(True)
        self.stripped_crimson_hyphae.setTristate(False)
        self.stripped_crimson_hyphae.setObjectName("stripped_crimson_hyphae")
        self.gridLayout_59.addWidget(self.CardWidget_298, 1, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_59.addItem(spacerItem24, 2, 1, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_59.addItem(spacerItem25, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_59, 109, 3, 1, 1)
        self.VerticalSeparator_24 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_24.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_24.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_24.setObjectName("VerticalSeparator_24")
        self.gridLayout_15.addWidget(self.VerticalSeparator_24, 77, 2, 1, 1)
        self.HorizontalSeparator_61 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_61.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_61.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_61.setObjectName("HorizontalSeparator_61")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_61, 62, 3, 1, 1)
        self.VerticalSeparator_48 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_48.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_48.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_48.setObjectName("VerticalSeparator_48")
        self.gridLayout_15.addWidget(self.VerticalSeparator_48, 29, 2, 1, 1)
        self.HorizontalSeparator_22 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_22.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_22.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_22.setObjectName("HorizontalSeparator_22")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_22, 22, 3, 1, 1)
        self.HorizontalSeparator_77 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_77.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_77.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_77.setObjectName("HorizontalSeparator_77")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_77, 78, 3, 1, 1)
        self.gridLayout_32 = QtWidgets.QGridLayout()
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.CardWidget_244 = CardWidget(self.layoutWidget1)
        self.CardWidget_244.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_244.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_244.setObjectName("CardWidget_244")
        self.green_concrete = CheckBox(self.CardWidget_244)
        self.green_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.green_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.green_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.green_concrete.setFont(font)
        self.green_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/green_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_concrete.setIcon(icon13)
        self.green_concrete.setIconSize(QtCore.QSize(16, 16))
        self.green_concrete.setChecked(True)
        self.green_concrete.setTristate(False)
        self.green_concrete.setObjectName("green_concrete")
        self.gridLayout_32.addWidget(self.CardWidget_244, 1, 0, 1, 1)
        self.CardWidget_245 = CardWidget(self.layoutWidget1)
        self.CardWidget_245.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_245.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_245.setObjectName("CardWidget_245")
        self.green_stained_glass = CheckBox(self.CardWidget_245)
        self.green_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.green_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.green_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.green_stained_glass.setFont(font)
        self.green_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon/green_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_stained_glass.setIcon(icon14)
        self.green_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.green_stained_glass.setTristate(False)
        self.green_stained_glass.setObjectName("green_stained_glass")
        self.gridLayout_32.addWidget(self.CardWidget_245, 1, 2, 1, 1)
        self.CardWidget_246 = CardWidget(self.layoutWidget1)
        self.CardWidget_246.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_246.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_246.setObjectName("CardWidget_246")
        self.dried_kelp_block = CheckBox(self.CardWidget_246)
        self.dried_kelp_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.dried_kelp_block.setMinimumSize(QtCore.QSize(17, 16))
        self.dried_kelp_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dried_kelp_block.setFont(font)
        self.dried_kelp_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icon/dried_kelp_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dried_kelp_block.setIcon(icon15)
        self.dried_kelp_block.setIconSize(QtCore.QSize(16, 16))
        self.dried_kelp_block.setTristate(False)
        self.dried_kelp_block.setObjectName("dried_kelp_block")
        self.gridLayout_32.addWidget(self.CardWidget_246, 3, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_32.addItem(spacerItem26, 4, 1, 1, 1)
        self.CardWidget_247 = CardWidget(self.layoutWidget1)
        self.CardWidget_247.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_247.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_247.setObjectName("CardWidget_247")
        self.green_wool = CheckBox(self.CardWidget_247)
        self.green_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.green_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.green_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.green_wool.setFont(font)
        self.green_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icon/green_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_wool.setIcon(icon16)
        self.green_wool.setIconSize(QtCore.QSize(16, 16))
        self.green_wool.setTristate(False)
        self.green_wool.setObjectName("green_wool")
        self.gridLayout_32.addWidget(self.CardWidget_247, 1, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_32.addItem(spacerItem27, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_32, 55, 3, 1, 1)
        self.CardWidget_24 = CardWidget(self.layoutWidget1)
        self.CardWidget_24.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_24.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_24.setObjectName("CardWidget_24")
        self.layoutWidget_43 = QtWidgets.QWidget(self.CardWidget_24)
        self.layoutWidget_43.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_43.setObjectName("layoutWidget_43")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.layoutWidget_43)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.PixmapLabel_30 = PixmapLabel(self.layoutWidget_43)
        self.PixmapLabel_30.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_30.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_30.setObjectName("PixmapLabel_30")
        self.horizontalLayout_51.addWidget(self.PixmapLabel_30)
        self.CheckBox_B12 = CheckBox(self.layoutWidget_43)
        self.CheckBox_B12.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B12.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B12.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B12.setChecked(True)
        self.CheckBox_B12.setObjectName("CheckBox_B12")
        self.horizontalLayout_51.addWidget(self.CheckBox_B12)
        self.gridLayout_15.addWidget(self.CardWidget_24, 25, 1, 1, 1)
        self.HorizontalSeparator_101 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_101.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_101.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_101.setObjectName("HorizontalSeparator_101")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_101, 102, 3, 1, 1)
        self.HorizontalSeparator_14 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_14.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_14.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_14.setObjectName("HorizontalSeparator_14")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_14, 14, 3, 1, 1)
        self.HorizontalSeparator_113 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_113.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_113.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_113.setObjectName("HorizontalSeparator_113")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_113, 114, 3, 1, 1)
        self.HorizontalSeparator_16 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_16.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_16.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_16.setObjectName("HorizontalSeparator_16")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_16, 16, 3, 1, 1)
        self.HorizontalSeparator_65 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_65.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_65.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_65.setObjectName("HorizontalSeparator_65")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_65, 66, 3, 1, 1)
        self.CardWidget_40 = CardWidget(self.layoutWidget1)
        self.CardWidget_40.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_40.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_40.setObjectName("CardWidget_40")
        self.layoutWidget_75 = QtWidgets.QWidget(self.CardWidget_40)
        self.layoutWidget_75.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_75.setObjectName("layoutWidget_75")
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout(self.layoutWidget_75)
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.PixmapLabel_46 = PixmapLabel(self.layoutWidget_75)
        self.PixmapLabel_46.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_46.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_46.setObjectName("PixmapLabel_46")
        self.horizontalLayout_83.addWidget(self.PixmapLabel_46)
        self.CheckBox_B28 = CheckBox(self.layoutWidget_75)
        self.CheckBox_B28.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B28.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B28.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B28.setChecked(True)
        self.CheckBox_B28.setObjectName("CheckBox_B28")
        self.horizontalLayout_83.addWidget(self.CheckBox_B28)
        self.gridLayout_15.addWidget(self.CardWidget_40, 57, 1, 1, 1)
        self.HorizontalSeparator_66 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_66.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_66.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_66.setObjectName("HorizontalSeparator_66")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_66, 68, 1, 1, 1)
        self.VerticalSeparator_38 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_38.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_38.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_38.setObjectName("VerticalSeparator_38")
        self.gridLayout_15.addWidget(self.VerticalSeparator_38, 49, 2, 1, 1)
        self.CardWidget_38 = CardWidget(self.layoutWidget1)
        self.CardWidget_38.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_38.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_38.setObjectName("CardWidget_38")
        self.layoutWidget_71 = QtWidgets.QWidget(self.CardWidget_38)
        self.layoutWidget_71.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_71.setObjectName("layoutWidget_71")
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout(self.layoutWidget_71)
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.PixmapLabel_44 = PixmapLabel(self.layoutWidget_71)
        self.PixmapLabel_44.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_44.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_44.setObjectName("PixmapLabel_44")
        self.horizontalLayout_79.addWidget(self.PixmapLabel_44)
        self.CheckBox_B26 = CheckBox(self.layoutWidget_71)
        self.CheckBox_B26.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B26.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B26.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B26.setChecked(True)
        self.CheckBox_B26.setObjectName("CheckBox_B26")
        self.horizontalLayout_79.addWidget(self.CheckBox_B26)
        self.gridLayout_15.addWidget(self.CardWidget_38, 53, 1, 1, 1)
        self.HorizontalSeparator_81 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_81.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_81.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_81.setObjectName("HorizontalSeparator_81")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_81, 82, 3, 1, 1)
        self.HorizontalSeparator_78 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_78.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_78.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_78.setObjectName("HorizontalSeparator_78")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_78, 80, 1, 1, 1)
        self.VerticalSeparator_63 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_63.setObjectName("VerticalSeparator_63")
        self.gridLayout_15.addWidget(self.VerticalSeparator_63, 1, 0, 123, 1)
        self.HorizontalSeparator_45 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_45.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_45.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_45.setObjectName("HorizontalSeparator_45")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_45, 46, 1, 1, 1)
        self.VerticalSeparator_43 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_43.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_43.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_43.setObjectName("VerticalSeparator_43")
        self.gridLayout_15.addWidget(self.VerticalSeparator_43, 39, 2, 1, 1)
        self.CardWidget_48 = CardWidget(self.layoutWidget1)
        self.CardWidget_48.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_48.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_48.setObjectName("CardWidget_48")
        self.layoutWidget_91 = QtWidgets.QWidget(self.CardWidget_48)
        self.layoutWidget_91.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_91.setObjectName("layoutWidget_91")
        self.horizontalLayout_99 = QtWidgets.QHBoxLayout(self.layoutWidget_91)
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_99.setObjectName("horizontalLayout_99")
        self.PixmapLabel_54 = PixmapLabel(self.layoutWidget_91)
        self.PixmapLabel_54.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_54.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_54.setObjectName("PixmapLabel_54")
        self.horizontalLayout_99.addWidget(self.PixmapLabel_54)
        self.CheckBox_B36 = CheckBox(self.layoutWidget_91)
        self.CheckBox_B36.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B36.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B36.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B36.setChecked(True)
        self.CheckBox_B36.setObjectName("CheckBox_B36")
        self.horizontalLayout_99.addWidget(self.CheckBox_B36)
        self.gridLayout_15.addWidget(self.CardWidget_48, 73, 1, 1, 1)
        self.HorizontalSeparator_15 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_15.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_15.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_15.setObjectName("HorizontalSeparator_15")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_15, 16, 1, 1, 1)
        self.HorizontalSeparator_84 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_84.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_84.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_84.setObjectName("HorizontalSeparator_84")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_84, 86, 1, 1, 1)
        self.VerticalSeparator_3 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_3.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_3.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_3.setObjectName("VerticalSeparator_3")
        self.gridLayout_15.addWidget(self.VerticalSeparator_3, 121, 2, 1, 1)
        self.CardWidget_27 = CardWidget(self.layoutWidget1)
        self.CardWidget_27.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_27.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_27.setObjectName("CardWidget_27")
        self.layoutWidget_49 = QtWidgets.QWidget(self.CardWidget_27)
        self.layoutWidget_49.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_49.setObjectName("layoutWidget_49")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.layoutWidget_49)
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.PixmapLabel_33 = PixmapLabel(self.layoutWidget_49)
        self.PixmapLabel_33.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_33.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_33.setObjectName("PixmapLabel_33")
        self.horizontalLayout_57.addWidget(self.PixmapLabel_33)
        self.CheckBox_B15 = CheckBox(self.layoutWidget_49)
        self.CheckBox_B15.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B15.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B15.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B15.setChecked(True)
        self.CheckBox_B15.setObjectName("CheckBox_B15")
        self.horizontalLayout_57.addWidget(self.CheckBox_B15)
        self.gridLayout_15.addWidget(self.CardWidget_27, 31, 1, 1, 1)
        self.CardWidget_39 = CardWidget(self.layoutWidget1)
        self.CardWidget_39.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_39.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_39.setObjectName("CardWidget_39")
        self.layoutWidget_73 = QtWidgets.QWidget(self.CardWidget_39)
        self.layoutWidget_73.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_73.setObjectName("layoutWidget_73")
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout(self.layoutWidget_73)
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.PixmapLabel_45 = PixmapLabel(self.layoutWidget_73)
        self.PixmapLabel_45.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_45.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_45.setObjectName("PixmapLabel_45")
        self.horizontalLayout_81.addWidget(self.PixmapLabel_45)
        self.CheckBox_B27 = CheckBox(self.layoutWidget_73)
        self.CheckBox_B27.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B27.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B27.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B27.setChecked(True)
        self.CheckBox_B27.setObjectName("CheckBox_B27")
        self.horizontalLayout_81.addWidget(self.CheckBox_B27)
        self.gridLayout_15.addWidget(self.CardWidget_39, 55, 1, 1, 1)
        self.CardWidget_63 = CardWidget(self.layoutWidget1)
        self.CardWidget_63.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_63.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_63.setObjectName("CardWidget_63")
        self.layoutWidget_121 = QtWidgets.QWidget(self.CardWidget_63)
        self.layoutWidget_121.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_121.setObjectName("layoutWidget_121")
        self.horizontalLayout_129 = QtWidgets.QHBoxLayout(self.layoutWidget_121)
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_129.setObjectName("horizontalLayout_129")
        self.PixmapLabel_69 = PixmapLabel(self.layoutWidget_121)
        self.PixmapLabel_69.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_69.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_69.setObjectName("PixmapLabel_69")
        self.horizontalLayout_129.addWidget(self.PixmapLabel_69)
        self.CheckBox_B51 = CheckBox(self.layoutWidget_121)
        self.CheckBox_B51.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B51.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B51.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B51.setChecked(True)
        self.CheckBox_B51.setObjectName("CheckBox_B51")
        self.horizontalLayout_129.addWidget(self.CheckBox_B51)
        self.gridLayout_15.addWidget(self.CardWidget_63, 103, 1, 1, 1)
        self.HorizontalSeparator_103 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_103.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_103.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_103.setObjectName("HorizontalSeparator_103")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_103, 104, 3, 1, 1)
        self.HorizontalSeparator_87 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_87.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_87.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_87.setObjectName("HorizontalSeparator_87")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_87, 88, 3, 1, 1)
        self.CardWidget_57 = CardWidget(self.layoutWidget1)
        self.CardWidget_57.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_57.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_57.setObjectName("CardWidget_57")
        self.layoutWidget_109 = QtWidgets.QWidget(self.CardWidget_57)
        self.layoutWidget_109.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_109.setObjectName("layoutWidget_109")
        self.horizontalLayout_117 = QtWidgets.QHBoxLayout(self.layoutWidget_109)
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_117.setObjectName("horizontalLayout_117")
        self.PixmapLabel_63 = PixmapLabel(self.layoutWidget_109)
        self.PixmapLabel_63.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_63.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_63.setObjectName("PixmapLabel_63")
        self.horizontalLayout_117.addWidget(self.PixmapLabel_63)
        self.CheckBox_B45 = CheckBox(self.layoutWidget_109)
        self.CheckBox_B45.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B45.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B45.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B45.setChecked(True)
        self.CheckBox_B45.setObjectName("CheckBox_B45")
        self.horizontalLayout_117.addWidget(self.CheckBox_B45)
        self.gridLayout_15.addWidget(self.CardWidget_57, 91, 1, 1, 1)
        self.gridLayout_33 = QtWidgets.QGridLayout()
        self.gridLayout_33.setObjectName("gridLayout_33")
        spacerItem28 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem28, 0, 1, 1, 1)
        self.CardWidget_251 = CardWidget(self.layoutWidget1)
        self.CardWidget_251.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_251.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_251.setObjectName("CardWidget_251")
        self.red_concrete = CheckBox(self.CardWidget_251)
        self.red_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.red_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.red_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.red_concrete.setFont(font)
        self.red_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icon/red_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.red_concrete.setIcon(icon17)
        self.red_concrete.setIconSize(QtCore.QSize(16, 16))
        self.red_concrete.setChecked(True)
        self.red_concrete.setTristate(False)
        self.red_concrete.setObjectName("red_concrete")
        self.gridLayout_33.addWidget(self.CardWidget_251, 1, 0, 1, 1)
        self.CardWidget_256 = CardWidget(self.layoutWidget1)
        self.CardWidget_256.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_256.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_256.setObjectName("CardWidget_256")
        self.red_wool = CheckBox(self.CardWidget_256)
        self.red_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.red_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.red_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.red_wool.setFont(font)
        self.red_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icon/red_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.red_wool.setIcon(icon18)
        self.red_wool.setIconSize(QtCore.QSize(16, 16))
        self.red_wool.setTristate(False)
        self.red_wool.setObjectName("red_wool")
        self.gridLayout_33.addWidget(self.CardWidget_256, 1, 1, 1, 1)
        self.CardWidget_254 = CardWidget(self.layoutWidget1)
        self.CardWidget_254.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_254.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_254.setObjectName("CardWidget_254")
        self.red_stained_glass = CheckBox(self.CardWidget_254)
        self.red_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.red_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.red_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.red_stained_glass.setFont(font)
        self.red_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icon/red_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.red_stained_glass.setIcon(icon19)
        self.red_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.red_stained_glass.setTristate(False)
        self.red_stained_glass.setObjectName("red_stained_glass")
        self.gridLayout_33.addWidget(self.CardWidget_254, 1, 2, 1, 1)
        self.CardWidget_248 = CardWidget(self.layoutWidget1)
        self.CardWidget_248.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_248.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_248.setObjectName("CardWidget_248")
        self.bricks = CheckBox(self.CardWidget_248)
        self.bricks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.bricks.setMinimumSize(QtCore.QSize(17, 16))
        self.bricks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bricks.setFont(font)
        self.bricks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icon/bricks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bricks.setIcon(icon20)
        self.bricks.setIconSize(QtCore.QSize(16, 16))
        self.bricks.setTristate(False)
        self.bricks.setObjectName("bricks")
        self.gridLayout_33.addWidget(self.CardWidget_248, 2, 0, 1, 1)
        self.CardWidget_249 = CardWidget(self.layoutWidget1)
        self.CardWidget_249.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_249.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_249.setObjectName("CardWidget_249")
        self.red_mushroom_block = CheckBox(self.CardWidget_249)
        self.red_mushroom_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.red_mushroom_block.setMinimumSize(QtCore.QSize(17, 16))
        self.red_mushroom_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.red_mushroom_block.setFont(font)
        self.red_mushroom_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icon/red_mushroom_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.red_mushroom_block.setIcon(icon21)
        self.red_mushroom_block.setIconSize(QtCore.QSize(16, 16))
        self.red_mushroom_block.setTristate(False)
        self.red_mushroom_block.setObjectName("red_mushroom_block")
        self.gridLayout_33.addWidget(self.CardWidget_249, 2, 1, 1, 1)
        self.CardWidget_250 = CardWidget(self.layoutWidget1)
        self.CardWidget_250.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_250.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_250.setObjectName("CardWidget_250")
        self.nether_wart_block = CheckBox(self.CardWidget_250)
        self.nether_wart_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.nether_wart_block.setMinimumSize(QtCore.QSize(17, 16))
        self.nether_wart_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nether_wart_block.setFont(font)
        self.nether_wart_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icon/nether_wart_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nether_wart_block.setIcon(icon22)
        self.nether_wart_block.setIconSize(QtCore.QSize(16, 16))
        self.nether_wart_block.setTristate(False)
        self.nether_wart_block.setObjectName("nether_wart_block")
        self.gridLayout_33.addWidget(self.CardWidget_250, 2, 2, 1, 1)
        self.CardWidget_252 = CardWidget(self.layoutWidget1)
        self.CardWidget_252.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_252.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_252.setObjectName("CardWidget_252")
        self.shroomlight = CheckBox(self.CardWidget_252)
        self.shroomlight.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.shroomlight.setMinimumSize(QtCore.QSize(17, 16))
        self.shroomlight.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.shroomlight.setFont(font)
        self.shroomlight.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icon/shroomlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shroomlight.setIcon(icon23)
        self.shroomlight.setIconSize(QtCore.QSize(16, 16))
        self.shroomlight.setTristate(False)
        self.shroomlight.setObjectName("shroomlight")
        self.gridLayout_33.addWidget(self.CardWidget_252, 3, 0, 1, 1)
        self.CardWidget_253 = CardWidget(self.layoutWidget1)
        self.CardWidget_253.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_253.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_253.setObjectName("CardWidget_253")
        self.mangrove_planks = CheckBox(self.CardWidget_253)
        self.mangrove_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.mangrove_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.mangrove_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mangrove_planks.setFont(font)
        self.mangrove_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icon/mangrove_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mangrove_planks.setIcon(icon24)
        self.mangrove_planks.setIconSize(QtCore.QSize(16, 16))
        self.mangrove_planks.setTristate(False)
        self.mangrove_planks.setObjectName("mangrove_planks")
        self.gridLayout_33.addWidget(self.CardWidget_253, 3, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem29, 4, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_33, 57, 3, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem30 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem30, 1, 1, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem31, 1, 2, 1, 1)
        self.CardWidget_165 = CardWidget(self.layoutWidget1)
        self.CardWidget_165.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_165.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_165.setObjectName("CardWidget_165")
        self.mushroom_stem = CheckBox(self.CardWidget_165)
        self.mushroom_stem.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.mushroom_stem.setMinimumSize(QtCore.QSize(17, 16))
        self.mushroom_stem.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mushroom_stem.setFont(font)
        self.mushroom_stem.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("icon/mushroom_stem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mushroom_stem.setIcon(icon25)
        self.mushroom_stem.setIconSize(QtCore.QSize(16, 16))
        self.mushroom_stem.setChecked(True)
        self.mushroom_stem.setTristate(False)
        self.mushroom_stem.setObjectName("mushroom_stem")
        self.gridLayout_10.addWidget(self.CardWidget_165, 1, 0, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem32, 2, 1, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem33, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_10, 7, 3, 1, 1)
        self.gridLayout_37 = QtWidgets.QGridLayout()
        self.gridLayout_37.setObjectName("gridLayout_37")
        spacerItem34 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem34, 1, 1, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem35, 1, 2, 1, 1)
        self.CardWidget_196 = CardWidget(self.layoutWidget1)
        self.CardWidget_196.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_196.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_196.setObjectName("CardWidget_196")
        self.lapis_block = CheckBox(self.CardWidget_196)
        self.lapis_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.lapis_block.setMinimumSize(QtCore.QSize(17, 16))
        self.lapis_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lapis_block.setFont(font)
        self.lapis_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("icon/lapis_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lapis_block.setIcon(icon26)
        self.lapis_block.setIconSize(QtCore.QSize(16, 16))
        self.lapis_block.setChecked(True)
        self.lapis_block.setTristate(False)
        self.lapis_block.setObjectName("lapis_block")
        self.gridLayout_37.addWidget(self.CardWidget_196, 1, 0, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_37.addItem(spacerItem36, 2, 1, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_37.addItem(spacerItem37, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_37, 65, 3, 1, 1)
        self.gridLayout_31 = QtWidgets.QGridLayout()
        self.gridLayout_31.setObjectName("gridLayout_31")
        spacerItem38 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_31.addItem(spacerItem38, 0, 1, 1, 1)
        self.CardWidget_181 = CardWidget(self.layoutWidget1)
        self.CardWidget_181.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_181.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_181.setObjectName("CardWidget_181")
        self.brown_concrete = CheckBox(self.CardWidget_181)
        self.brown_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.brown_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.brown_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.brown_concrete.setFont(font)
        self.brown_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("icon/brown_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brown_concrete.setIcon(icon27)
        self.brown_concrete.setIconSize(QtCore.QSize(16, 16))
        self.brown_concrete.setChecked(True)
        self.brown_concrete.setTristate(False)
        self.brown_concrete.setObjectName("brown_concrete")
        self.gridLayout_31.addWidget(self.CardWidget_181, 1, 0, 1, 1)
        self.CardWidget_182 = CardWidget(self.layoutWidget1)
        self.CardWidget_182.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_182.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_182.setObjectName("CardWidget_182")
        self.brown_wool = CheckBox(self.CardWidget_182)
        self.brown_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.brown_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.brown_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.brown_wool.setFont(font)
        self.brown_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("icon/brown_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brown_wool.setIcon(icon28)
        self.brown_wool.setIconSize(QtCore.QSize(16, 16))
        self.brown_wool.setTristate(False)
        self.brown_wool.setObjectName("brown_wool")
        self.gridLayout_31.addWidget(self.CardWidget_182, 1, 1, 1, 1)
        self.CardWidget_183 = CardWidget(self.layoutWidget1)
        self.CardWidget_183.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_183.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_183.setObjectName("CardWidget_183")
        self.brown_stained_glass = CheckBox(self.CardWidget_183)
        self.brown_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.brown_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.brown_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.brown_stained_glass.setFont(font)
        self.brown_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("icon/brown_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brown_stained_glass.setIcon(icon29)
        self.brown_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.brown_stained_glass.setTristate(False)
        self.brown_stained_glass.setObjectName("brown_stained_glass")
        self.gridLayout_31.addWidget(self.CardWidget_183, 1, 2, 1, 1)
        self.CardWidget_184 = CardWidget(self.layoutWidget1)
        self.CardWidget_184.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_184.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_184.setObjectName("CardWidget_184")
        self.dark_oak_planks = CheckBox(self.CardWidget_184)
        self.dark_oak_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.dark_oak_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.dark_oak_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dark_oak_planks.setFont(font)
        self.dark_oak_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("icon/dark_oak_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dark_oak_planks.setIcon(icon30)
        self.dark_oak_planks.setIconSize(QtCore.QSize(16, 16))
        self.dark_oak_planks.setTristate(False)
        self.dark_oak_planks.setObjectName("dark_oak_planks")
        self.gridLayout_31.addWidget(self.CardWidget_184, 3, 0, 1, 1)
        self.CardWidget_185 = CardWidget(self.layoutWidget1)
        self.CardWidget_185.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_185.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_185.setObjectName("CardWidget_185")
        self.soul_soil = CheckBox(self.CardWidget_185)
        self.soul_soil.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.soul_soil.setMinimumSize(QtCore.QSize(17, 16))
        self.soul_soil.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.soul_soil.setFont(font)
        self.soul_soil.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("icon/soul_soil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soul_soil.setIcon(icon31)
        self.soul_soil.setIconSize(QtCore.QSize(16, 16))
        self.soul_soil.setTristate(False)
        self.soul_soil.setObjectName("soul_soil")
        self.gridLayout_31.addWidget(self.CardWidget_185, 3, 1, 1, 1)
        spacerItem39 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_31.addItem(spacerItem39, 4, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_31, 53, 3, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem40 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem40, 0, 1, 1, 1)
        self.CardWidget_175 = CardWidget(self.layoutWidget1)
        self.CardWidget_175.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_175.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_175.setObjectName("CardWidget_175")
        self.yellow_concrete = CheckBox(self.CardWidget_175)
        self.yellow_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.yellow_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.yellow_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.yellow_concrete.setFont(font)
        self.yellow_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("icon/yellow_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_concrete.setIcon(icon32)
        self.yellow_concrete.setIconSize(QtCore.QSize(16, 16))
        self.yellow_concrete.setChecked(True)
        self.yellow_concrete.setTristate(False)
        self.yellow_concrete.setObjectName("yellow_concrete")
        self.gridLayout_5.addWidget(self.CardWidget_175, 1, 0, 1, 1)
        self.CardWidget_176 = CardWidget(self.layoutWidget1)
        self.CardWidget_176.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_176.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_176.setObjectName("CardWidget_176")
        self.yellow_wool = CheckBox(self.CardWidget_176)
        self.yellow_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.yellow_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.yellow_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.yellow_wool.setFont(font)
        self.yellow_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("icon/yellow_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_wool.setIcon(icon33)
        self.yellow_wool.setIconSize(QtCore.QSize(16, 16))
        self.yellow_wool.setTristate(False)
        self.yellow_wool.setObjectName("yellow_wool")
        self.gridLayout_5.addWidget(self.CardWidget_176, 1, 1, 1, 1)
        self.CardWidget_177 = CardWidget(self.layoutWidget1)
        self.CardWidget_177.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_177.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_177.setObjectName("CardWidget_177")
        self.yellow_stained_glass = CheckBox(self.CardWidget_177)
        self.yellow_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.yellow_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.yellow_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.yellow_stained_glass.setFont(font)
        self.yellow_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("icon/yellow_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_stained_glass.setIcon(icon34)
        self.yellow_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.yellow_stained_glass.setTristate(False)
        self.yellow_stained_glass.setObjectName("yellow_stained_glass")
        self.gridLayout_5.addWidget(self.CardWidget_177, 1, 2, 1, 1)
        self.CardWidget_179 = CardWidget(self.layoutWidget1)
        self.CardWidget_179.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_179.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_179.setObjectName("CardWidget_179")
        self.hay_block = CheckBox(self.CardWidget_179)
        self.hay_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.hay_block.setMinimumSize(QtCore.QSize(17, 16))
        self.hay_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hay_block.setFont(font)
        self.hay_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("icon/hay_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hay_block.setIcon(icon35)
        self.hay_block.setIconSize(QtCore.QSize(16, 16))
        self.hay_block.setTristate(False)
        self.hay_block.setObjectName("hay_block")
        self.gridLayout_5.addWidget(self.CardWidget_179, 3, 0, 1, 1)
        self.CardWidget_180 = CardWidget(self.layoutWidget1)
        self.CardWidget_180.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_180.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_180.setObjectName("CardWidget_180")
        self.bamboo_planks = CheckBox(self.CardWidget_180)
        self.bamboo_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.bamboo_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.bamboo_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bamboo_planks.setFont(font)
        self.bamboo_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("icon/bamboo_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bamboo_planks.setIcon(icon36)
        self.bamboo_planks.setIconSize(QtCore.QSize(16, 16))
        self.bamboo_planks.setTristate(False)
        self.bamboo_planks.setObjectName("bamboo_planks")
        self.gridLayout_5.addWidget(self.CardWidget_180, 3, 1, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem41, 4, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_5, 37, 3, 1, 1)
        self.VerticalSeparator_37 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_37.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_37.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_37.setObjectName("VerticalSeparator_37")
        self.gridLayout_15.addWidget(self.VerticalSeparator_37, 51, 2, 1, 1)
        self.HorizontalSeparator_110 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_110.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_110.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_110.setObjectName("HorizontalSeparator_110")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_110, 112, 1, 1, 1)
        self.VerticalSeparator_31 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_31.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_31.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_31.setObjectName("VerticalSeparator_31")
        self.gridLayout_15.addWidget(self.VerticalSeparator_31, 63, 2, 1, 1)
        self.CardWidget_31 = CardWidget(self.layoutWidget1)
        self.CardWidget_31.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_31.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_31.setObjectName("CardWidget_31")
        self.layoutWidget_57 = QtWidgets.QWidget(self.CardWidget_31)
        self.layoutWidget_57.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_57.setObjectName("layoutWidget_57")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout(self.layoutWidget_57)
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.PixmapLabel_37 = PixmapLabel(self.layoutWidget_57)
        self.PixmapLabel_37.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_37.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_37.setObjectName("PixmapLabel_37")
        self.horizontalLayout_65.addWidget(self.PixmapLabel_37)
        self.CheckBox_B19 = CheckBox(self.layoutWidget_57)
        self.CheckBox_B19.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B19.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B19.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B19.setChecked(True)
        self.CheckBox_B19.setObjectName("CheckBox_B19")
        self.horizontalLayout_65.addWidget(self.CheckBox_B19)
        self.gridLayout_15.addWidget(self.CardWidget_31, 39, 1, 1, 1)
        self.HorizontalSeparator_123 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_123.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_123.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_123.setObjectName("HorizontalSeparator_123")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_123, 124, 1, 1, 1)
        self.HorizontalSeparator_120 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_120.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_120.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_120.setObjectName("HorizontalSeparator_120")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_120, 56, 3, 1, 1)
        self.VerticalSeparator_2 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_2.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_2.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_2.setObjectName("VerticalSeparator_2")
        self.gridLayout_15.addWidget(self.VerticalSeparator_2, 123, 2, 1, 1)
        self.HorizontalSeparator_17 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_17.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_17.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_17.setObjectName("HorizontalSeparator_17")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_17, 18, 1, 1, 1)
        self.HorizontalSeparator_53 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_53.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_53.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_53.setObjectName("HorizontalSeparator_53")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_53, 54, 1, 1, 1)
        self.VerticalSeparator_13 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_13.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_13.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_13.setObjectName("VerticalSeparator_13")
        self.gridLayout_15.addWidget(self.VerticalSeparator_13, 99, 2, 1, 1)
        self.gridLayout_67 = QtWidgets.QGridLayout()
        self.gridLayout_67.setObjectName("gridLayout_67")
        spacerItem42 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_67.addItem(spacerItem42, 1, 1, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_67.addItem(spacerItem43, 1, 2, 1, 1)
        self.CardWidget_308 = CardWidget(self.layoutWidget1)
        self.CardWidget_308.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_308.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_308.setObjectName("CardWidget_308")
        self.verdant_froglight_top = CheckBox(self.CardWidget_308)
        self.verdant_froglight_top.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.verdant_froglight_top.setMinimumSize(QtCore.QSize(17, 16))
        self.verdant_froglight_top.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.verdant_froglight_top.setFont(font)
        self.verdant_froglight_top.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("icon/verdant_froglight_top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.verdant_froglight_top.setIcon(icon37)
        self.verdant_froglight_top.setIconSize(QtCore.QSize(16, 16))
        self.verdant_froglight_top.setChecked(True)
        self.verdant_froglight_top.setTristate(False)
        self.verdant_froglight_top.setObjectName("verdant_froglight_top")
        self.gridLayout_67.addWidget(self.CardWidget_308, 1, 0, 1, 1)
        spacerItem44 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_67.addItem(spacerItem44, 2, 1, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_67.addItem(spacerItem45, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_67, 123, 3, 1, 1)
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        spacerItem46 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem46, 1, 1, 1, 1)
        spacerItem47 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem47, 1, 2, 1, 1)
        self.CardWidget_192 = CardWidget(self.layoutWidget1)
        self.CardWidget_192.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_192.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_192.setObjectName("CardWidget_192")
        self.gold_block = CheckBox(self.CardWidget_192)
        self.gold_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.gold_block.setMinimumSize(QtCore.QSize(17, 16))
        self.gold_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gold_block.setFont(font)
        self.gold_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("icon/gold_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gold_block.setIcon(icon38)
        self.gold_block.setIconSize(QtCore.QSize(16, 16))
        self.gold_block.setChecked(True)
        self.gold_block.setTristate(False)
        self.gold_block.setObjectName("gold_block")
        self.gridLayout_26.addWidget(self.CardWidget_192, 1, 0, 1, 1)
        spacerItem48 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem48, 2, 1, 1, 1)
        spacerItem49 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem49, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_26, 61, 3, 1, 1)
        self.VerticalSeparator_15 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_15.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_15.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_15.setObjectName("VerticalSeparator_15")
        self.gridLayout_15.addWidget(self.VerticalSeparator_15, 95, 2, 1, 1)
        self.VerticalSeparator_9 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_9.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_9.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_9.setObjectName("VerticalSeparator_9")
        self.gridLayout_15.addWidget(self.VerticalSeparator_9, 107, 2, 1, 1)
        self.HorizontalSeparator_60 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_60.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_60.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_60.setObjectName("HorizontalSeparator_60")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_60, 62, 1, 1, 1)
        self.CardWidget_44 = CardWidget(self.layoutWidget1)
        self.CardWidget_44.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_44.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_44.setObjectName("CardWidget_44")
        self.layoutWidget_83 = QtWidgets.QWidget(self.CardWidget_44)
        self.layoutWidget_83.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_83.setObjectName("layoutWidget_83")
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout(self.layoutWidget_83)
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.PixmapLabel_50 = PixmapLabel(self.layoutWidget_83)
        self.PixmapLabel_50.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_50.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_50.setObjectName("PixmapLabel_50")
        self.horizontalLayout_91.addWidget(self.PixmapLabel_50)
        self.CheckBox_B32 = CheckBox(self.layoutWidget_83)
        self.CheckBox_B32.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B32.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B32.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B32.setChecked(True)
        self.CheckBox_B32.setObjectName("CheckBox_B32")
        self.horizontalLayout_91.addWidget(self.CheckBox_B32)
        self.gridLayout_15.addWidget(self.CardWidget_44, 65, 1, 1, 1)
        self.CardWidget_35 = CardWidget(self.layoutWidget1)
        self.CardWidget_35.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_35.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_35.setObjectName("CardWidget_35")
        self.layoutWidget_65 = QtWidgets.QWidget(self.CardWidget_35)
        self.layoutWidget_65.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_65.setObjectName("layoutWidget_65")
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout(self.layoutWidget_65)
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.PixmapLabel_41 = PixmapLabel(self.layoutWidget_65)
        self.PixmapLabel_41.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_41.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_41.setObjectName("PixmapLabel_41")
        self.horizontalLayout_73.addWidget(self.PixmapLabel_41)
        self.CheckBox_B23 = CheckBox(self.layoutWidget_65)
        self.CheckBox_B23.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B23.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B23.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B23.setChecked(True)
        self.CheckBox_B23.setObjectName("CheckBox_B23")
        self.horizontalLayout_73.addWidget(self.CheckBox_B23)
        self.gridLayout_15.addWidget(self.CardWidget_35, 47, 1, 1, 1)
        self.HorizontalSeparator_118 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_118.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_118.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_118.setObjectName("HorizontalSeparator_118")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_118, 120, 1, 1, 1)
        self.gridLayout_51 = QtWidgets.QGridLayout()
        self.gridLayout_51.setObjectName("gridLayout_51")
        spacerItem50 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_51.addItem(spacerItem50, 1, 1, 1, 1)
        spacerItem51 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_51.addItem(spacerItem51, 1, 2, 1, 1)
        self.CardWidget_290 = CardWidget(self.layoutWidget1)
        self.CardWidget_290.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_290.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_290.setObjectName("CardWidget_290")
        self.purple_terracotta = CheckBox(self.CardWidget_290)
        self.purple_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.purple_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.purple_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.purple_terracotta.setFont(font)
        self.purple_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("icon/purple_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.purple_terracotta.setIcon(icon39)
        self.purple_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.purple_terracotta.setChecked(True)
        self.purple_terracotta.setTristate(False)
        self.purple_terracotta.setObjectName("purple_terracotta")
        self.gridLayout_51.addWidget(self.CardWidget_290, 1, 0, 1, 1)
        spacerItem52 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_51.addItem(spacerItem52, 2, 1, 1, 1)
        spacerItem53 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_51.addItem(spacerItem53, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_51, 93, 3, 1, 1)
        self.VerticalSeparator_26 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_26.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_26.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_26.setObjectName("VerticalSeparator_26")
        self.gridLayout_15.addWidget(self.VerticalSeparator_26, 73, 2, 1, 1)
        self.VerticalSeparator_42 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_42.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_42.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_42.setObjectName("VerticalSeparator_42")
        self.gridLayout_15.addWidget(self.VerticalSeparator_42, 41, 2, 1, 1)
        self.HorizontalSeparator_116 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_116.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_116.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_116.setObjectName("HorizontalSeparator_116")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_116, 118, 1, 1, 1)
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.CardWidget_241 = CardWidget(self.layoutWidget1)
        self.CardWidget_241.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_241.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_241.setObjectName("CardWidget_241")
        self.blue_concrete = CheckBox(self.CardWidget_241)
        self.blue_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.blue_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.blue_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.blue_concrete.setFont(font)
        self.blue_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("icon/blue_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blue_concrete.setIcon(icon40)
        self.blue_concrete.setIconSize(QtCore.QSize(16, 16))
        self.blue_concrete.setChecked(True)
        self.blue_concrete.setTristate(False)
        self.blue_concrete.setObjectName("blue_concrete")
        self.gridLayout_30.addWidget(self.CardWidget_241, 1, 0, 1, 1)
        spacerItem54 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_30.addItem(spacerItem54, 2, 1, 1, 1)
        spacerItem55 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_30.addItem(spacerItem55, 0, 1, 1, 1)
        self.CardWidget_242 = CardWidget(self.layoutWidget1)
        self.CardWidget_242.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_242.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_242.setObjectName("CardWidget_242")
        self.blue_wool = CheckBox(self.CardWidget_242)
        self.blue_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.blue_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.blue_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.blue_wool.setFont(font)
        self.blue_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("icon/blue_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blue_wool.setIcon(icon41)
        self.blue_wool.setIconSize(QtCore.QSize(16, 16))
        self.blue_wool.setTristate(False)
        self.blue_wool.setObjectName("blue_wool")
        self.gridLayout_30.addWidget(self.CardWidget_242, 1, 1, 1, 1)
        self.CardWidget_243 = CardWidget(self.layoutWidget1)
        self.CardWidget_243.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_243.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_243.setObjectName("CardWidget_243")
        self.blue_stained_glass = CheckBox(self.CardWidget_243)
        self.blue_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.blue_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.blue_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.blue_stained_glass.setFont(font)
        self.blue_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("icon/blue_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blue_stained_glass.setIcon(icon42)
        self.blue_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.blue_stained_glass.setTristate(False)
        self.blue_stained_glass.setObjectName("blue_stained_glass")
        self.gridLayout_30.addWidget(self.CardWidget_243, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_30, 51, 3, 1, 1)
        self.VerticalSeparator_11 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_11.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_11.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_11.setObjectName("VerticalSeparator_11")
        self.gridLayout_15.addWidget(self.VerticalSeparator_11, 103, 2, 1, 1)
        self.HorizontalSeparator_83 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_83.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_83.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_83.setObjectName("HorizontalSeparator_83")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_83, 84, 3, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem56 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem56, 1, 1, 1, 1)
        spacerItem57 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem57, 1, 2, 1, 1)
        self.CardWidget_178 = CardWidget(self.layoutWidget1)
        self.CardWidget_178.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_178.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_178.setObjectName("CardWidget_178")
        self.clay = CheckBox(self.CardWidget_178)
        self.clay.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.clay.setMinimumSize(QtCore.QSize(17, 16))
        self.clay.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clay.setFont(font)
        self.clay.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("icon/clay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clay.setIcon(icon43)
        self.clay.setIconSize(QtCore.QSize(16, 16))
        self.clay.setChecked(True)
        self.clay.setTristate(False)
        self.clay.setObjectName("clay")
        self.gridLayout_20.addWidget(self.CardWidget_178, 1, 0, 1, 1)
        spacerItem58 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem58, 2, 1, 1, 1)
        spacerItem59 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem59, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_20, 19, 3, 1, 1)
        self.HorizontalSeparator_4 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_4.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_4.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_4.setObjectName("HorizontalSeparator_4")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_4, 4, 3, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.CardWidget_208 = CardWidget(self.layoutWidget1)
        self.CardWidget_208.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_208.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_208.setObjectName("CardWidget_208")
        self.white_concrete = CheckBox(self.CardWidget_208)
        self.white_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.white_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.white_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.white_concrete.setFont(font)
        self.white_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("icon/white_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.white_concrete.setIcon(icon44)
        self.white_concrete.setIconSize(QtCore.QSize(16, 16))
        self.white_concrete.setChecked(True)
        self.white_concrete.setTristate(False)
        self.white_concrete.setObjectName("white_concrete")
        self.gridLayout_3.addWidget(self.CardWidget_208, 1, 0, 1, 1)
        self.CardWidget_209 = CardWidget(self.layoutWidget1)
        self.CardWidget_209.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_209.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_209.setObjectName("CardWidget_209")
        self.white_stained_glass = CheckBox(self.CardWidget_209)
        self.white_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.white_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.white_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.white_stained_glass.setFont(font)
        self.white_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("icon/white_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.white_stained_glass.setIcon(icon45)
        self.white_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.white_stained_glass.setTristate(False)
        self.white_stained_glass.setObjectName("white_stained_glass")
        self.gridLayout_3.addWidget(self.CardWidget_209, 1, 2, 1, 1)
        self.CardWidget_210 = CardWidget(self.layoutWidget1)
        self.CardWidget_210.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_210.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_210.setObjectName("CardWidget_210")
        self.snow_block = CheckBox(self.CardWidget_210)
        self.snow_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.snow_block.setMinimumSize(QtCore.QSize(17, 16))
        self.snow_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.snow_block.setFont(font)
        self.snow_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("icon/snow_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snow_block.setIcon(icon46)
        self.snow_block.setIconSize(QtCore.QSize(16, 16))
        self.snow_block.setTristate(False)
        self.snow_block.setObjectName("snow_block")
        self.gridLayout_3.addWidget(self.CardWidget_210, 3, 0, 1, 1)
        spacerItem60 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem60, 4, 1, 1, 1)
        self.CardWidget_212 = CardWidget(self.layoutWidget1)
        self.CardWidget_212.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_212.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_212.setObjectName("CardWidget_212")
        self.white_wool = CheckBox(self.CardWidget_212)
        self.white_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.white_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.white_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.white_wool.setFont(font)
        self.white_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("icon/white_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.white_wool.setIcon(icon47)
        self.white_wool.setIconSize(QtCore.QSize(16, 16))
        self.white_wool.setTristate(False)
        self.white_wool.setObjectName("white_wool")
        self.gridLayout_3.addWidget(self.CardWidget_212, 1, 1, 1, 1)
        spacerItem61 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem61, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_3, 17, 3, 1, 1)
        self.HorizontalSeparator_27 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_27.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_27.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_27.setObjectName("HorizontalSeparator_27")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_27, 28, 1, 1, 1)
        self.VerticalSeparator_20 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_20.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_20.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_20.setObjectName("VerticalSeparator_20")
        self.gridLayout_15.addWidget(self.VerticalSeparator_20, 85, 2, 1, 1)
        self.HorizontalSeparator_115 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_115.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_115.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_115.setObjectName("HorizontalSeparator_115")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_115, 116, 3, 1, 1)
        self.HorizontalSeparator_6 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_6.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_6.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_6.setObjectName("HorizontalSeparator_6")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_6, 6, 3, 1, 1)
        self.HorizontalSeparator_32 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_32.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_32.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_32.setObjectName("HorizontalSeparator_32")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_32, 32, 3, 1, 1)
        self.CardWidget_66 = CardWidget(self.layoutWidget1)
        self.CardWidget_66.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_66.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_66.setObjectName("CardWidget_66")
        self.layoutWidget_127 = QtWidgets.QWidget(self.CardWidget_66)
        self.layoutWidget_127.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_127.setObjectName("layoutWidget_127")
        self.horizontalLayout_135 = QtWidgets.QHBoxLayout(self.layoutWidget_127)
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_135.setObjectName("horizontalLayout_135")
        self.PixmapLabel_72 = PixmapLabel(self.layoutWidget_127)
        self.PixmapLabel_72.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_72.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_72.setObjectName("PixmapLabel_72")
        self.horizontalLayout_135.addWidget(self.PixmapLabel_72)
        self.CheckBox_B54 = CheckBox(self.layoutWidget_127)
        self.CheckBox_B54.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B54.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B54.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B54.setChecked(True)
        self.CheckBox_B54.setObjectName("CheckBox_B54")
        self.horizontalLayout_135.addWidget(self.CheckBox_B54)
        self.gridLayout_15.addWidget(self.CardWidget_66, 109, 1, 1, 1)
        self.VerticalSeparator_50 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_50.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_50.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_50.setObjectName("VerticalSeparator_50")
        self.gridLayout_15.addWidget(self.VerticalSeparator_50, 25, 2, 1, 1)
        self.HorizontalSeparator_43 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_43.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_43.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_43.setObjectName("HorizontalSeparator_43")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_43, 44, 1, 1, 1)
        self.HorizontalSeparator_88 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_88.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_88.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_88.setObjectName("HorizontalSeparator_88")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_88, 90, 1, 1, 1)
        self.CardWidget_67 = CardWidget(self.layoutWidget1)
        self.CardWidget_67.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_67.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_67.setObjectName("CardWidget_67")
        self.layoutWidget_129 = QtWidgets.QWidget(self.CardWidget_67)
        self.layoutWidget_129.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_129.setObjectName("layoutWidget_129")
        self.horizontalLayout_137 = QtWidgets.QHBoxLayout(self.layoutWidget_129)
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_137.setObjectName("horizontalLayout_137")
        self.PixmapLabel_73 = PixmapLabel(self.layoutWidget_129)
        self.PixmapLabel_73.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_73.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_73.setObjectName("PixmapLabel_73")
        self.horizontalLayout_137.addWidget(self.PixmapLabel_73)
        self.CheckBox_B55 = CheckBox(self.layoutWidget_129)
        self.CheckBox_B55.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B55.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B55.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B55.setChecked(True)
        self.CheckBox_B55.setObjectName("CheckBox_B55")
        self.horizontalLayout_137.addWidget(self.CheckBox_B55)
        self.gridLayout_15.addWidget(self.CardWidget_67, 111, 1, 1, 1)
        self.VerticalSeparator_34 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_34.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_34.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_34.setObjectName("VerticalSeparator_34")
        self.gridLayout_15.addWidget(self.VerticalSeparator_34, 57, 2, 1, 1)
        self.CardWidget_61 = CardWidget(self.layoutWidget1)
        self.CardWidget_61.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_61.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_61.setObjectName("CardWidget_61")
        self.layoutWidget_117 = QtWidgets.QWidget(self.CardWidget_61)
        self.layoutWidget_117.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_117.setObjectName("layoutWidget_117")
        self.horizontalLayout_125 = QtWidgets.QHBoxLayout(self.layoutWidget_117)
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_125.setObjectName("horizontalLayout_125")
        self.PixmapLabel_67 = PixmapLabel(self.layoutWidget_117)
        self.PixmapLabel_67.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_67.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_67.setObjectName("PixmapLabel_67")
        self.horizontalLayout_125.addWidget(self.PixmapLabel_67)
        self.CheckBox_B49 = CheckBox(self.layoutWidget_117)
        self.CheckBox_B49.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B49.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B49.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B49.setChecked(True)
        self.CheckBox_B49.setObjectName("CheckBox_B49")
        self.horizontalLayout_125.addWidget(self.CheckBox_B49)
        self.gridLayout_15.addWidget(self.CardWidget_61, 99, 1, 1, 1)
        self.HorizontalSeparator_23 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_23.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_23.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_23.setObjectName("HorizontalSeparator_23")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_23, 24, 1, 1, 1)
        self.VerticalSeparator_49 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_49.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_49.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_49.setObjectName("VerticalSeparator_49")
        self.gridLayout_15.addWidget(self.VerticalSeparator_49, 27, 2, 1, 1)
        self.VerticalSeparator_35 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_35.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_35.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_35.setObjectName("VerticalSeparator_35")
        self.gridLayout_15.addWidget(self.VerticalSeparator_35, 55, 2, 1, 1)
        self.VerticalSeparator_6 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_6.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_6.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_6.setObjectName("VerticalSeparator_6")
        self.gridLayout_15.addWidget(self.VerticalSeparator_6, 115, 2, 1, 1)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.CardWidget_191 = CardWidget(self.layoutWidget1)
        self.CardWidget_191.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_191.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_191.setObjectName("CardWidget_191")
        self.quartz_block = CheckBox(self.CardWidget_191)
        self.quartz_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.quartz_block.setMinimumSize(QtCore.QSize(17, 16))
        self.quartz_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.quartz_block.setFont(font)
        self.quartz_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("icon/quartz_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quartz_block.setIcon(icon48)
        self.quartz_block.setIconSize(QtCore.QSize(16, 16))
        self.quartz_block.setChecked(True)
        self.quartz_block.setTristate(False)
        self.quartz_block.setObjectName("quartz_block")
        self.gridLayout_25.addWidget(self.CardWidget_191, 1, 0, 1, 1)
        spacerItem62 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_25.addItem(spacerItem62, 2, 1, 1, 1)
        spacerItem63 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_25.addItem(spacerItem63, 0, 1, 1, 1)
        self.CardWidget_190 = CardWidget(self.layoutWidget1)
        self.CardWidget_190.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_190.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_190.setObjectName("CardWidget_190")
        self.sea_lantern = CheckBox(self.CardWidget_190)
        self.sea_lantern.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.sea_lantern.setMinimumSize(QtCore.QSize(17, 16))
        self.sea_lantern.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sea_lantern.setFont(font)
        self.sea_lantern.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("icon/sea_lantern.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sea_lantern.setIcon(icon49)
        self.sea_lantern.setIconSize(QtCore.QSize(16, 16))
        self.sea_lantern.setTristate(False)
        self.sea_lantern.setObjectName("sea_lantern")
        self.gridLayout_25.addWidget(self.CardWidget_190, 1, 1, 1, 1)
        self.CardWidget_193 = CardWidget(self.layoutWidget1)
        self.CardWidget_193.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_193.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_193.setObjectName("CardWidget_193")
        self.target = CheckBox(self.CardWidget_193)
        self.target.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.target.setMinimumSize(QtCore.QSize(17, 16))
        self.target.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.target.setFont(font)
        self.target.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("icon/target.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.target.setIcon(icon50)
        self.target.setIconSize(QtCore.QSize(16, 16))
        self.target.setTristate(False)
        self.target.setObjectName("target")
        self.gridLayout_25.addWidget(self.CardWidget_193, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_25, 29, 3, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem64 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem64, 1, 1, 1, 1)
        spacerItem65 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem65, 1, 2, 1, 1)
        self.CardWidget_159 = CardWidget(self.layoutWidget1)
        self.CardWidget_159.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_159.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_159.setObjectName("CardWidget_159")
        self.glass = CheckBox(self.CardWidget_159)
        self.glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.glass.setMinimumSize(QtCore.QSize(17, 16))
        self.glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.glass.setFont(font)
        self.glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("icon/glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.glass.setIcon(icon51)
        self.glass.setIconSize(QtCore.QSize(16, 16))
        self.glass.setCheckable(True)
        self.glass.setChecked(True)
        self.glass.setAutoRepeat(False)
        self.glass.setAutoExclusive(True)
        self.glass.setTristate(False)
        self.glass.setObjectName("glass")
        self.gridLayout_7.addWidget(self.CardWidget_159, 1, 0, 1, 1)
        spacerItem66 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem66, 2, 1, 1, 1)
        spacerItem67 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem67, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_7, 1, 3, 1, 1)
        self.VerticalSeparator_60 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_60.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_60.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_60.setObjectName("VerticalSeparator_60")
        self.gridLayout_15.addWidget(self.VerticalSeparator_60, 5, 2, 1, 1)
        self.VerticalSeparator_61 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_61.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_61.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_61.setObjectName("VerticalSeparator_61")
        self.gridLayout_15.addWidget(self.VerticalSeparator_61, 3, 2, 1, 1)
        self.HorizontalSeparator_119 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_119.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_119.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_119.setObjectName("HorizontalSeparator_119")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_119, 120, 3, 1, 1)
        self.HorizontalSeparator_2 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_2.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_2.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_2.setObjectName("HorizontalSeparator_2")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_2, 2, 3, 1, 1)
        self.CardWidget_20 = CardWidget(self.layoutWidget1)
        self.CardWidget_20.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_20.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_20.setObjectName("CardWidget_20")
        self.layoutWidget_32 = QtWidgets.QWidget(self.CardWidget_20)
        self.layoutWidget_32.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_32.setObjectName("layoutWidget_32")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.layoutWidget_32)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.PixmapLabel_26 = PixmapLabel(self.layoutWidget_32)
        self.PixmapLabel_26.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_26.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_26.setObjectName("PixmapLabel_26")
        self.horizontalLayout_43.addWidget(self.PixmapLabel_26)
        self.CheckBox_B8 = CheckBox(self.layoutWidget_32)
        self.CheckBox_B8.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B8.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B8.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B8.setChecked(True)
        self.CheckBox_B8.setObjectName("CheckBox_B8")
        self.horizontalLayout_43.addWidget(self.CheckBox_B8)
        self.gridLayout_15.addWidget(self.CardWidget_20, 17, 1, 1, 1)
        self.HorizontalSeparator_12 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_12.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_12.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_12.setObjectName("HorizontalSeparator_12")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_12, 12, 3, 1, 1)
        self.HorizontalSeparator_124 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_124.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_124.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_124.setObjectName("HorizontalSeparator_124")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_124, 124, 3, 1, 1)
        self.VerticalSeparator_51 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_51.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_51.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_51.setObjectName("VerticalSeparator_51")
        self.gridLayout_15.addWidget(self.VerticalSeparator_51, 23, 2, 1, 1)
        self.HorizontalSeparator_44 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_44.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_44.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_44.setObjectName("HorizontalSeparator_44")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_44, 44, 3, 1, 1)
        self.CardWidget_53 = CardWidget(self.layoutWidget1)
        self.CardWidget_53.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_53.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_53.setObjectName("CardWidget_53")
        self.layoutWidget_101 = QtWidgets.QWidget(self.CardWidget_53)
        self.layoutWidget_101.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_101.setObjectName("layoutWidget_101")
        self.horizontalLayout_109 = QtWidgets.QHBoxLayout(self.layoutWidget_101)
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_109.setObjectName("horizontalLayout_109")
        self.PixmapLabel_59 = PixmapLabel(self.layoutWidget_101)
        self.PixmapLabel_59.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_59.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_59.setObjectName("PixmapLabel_59")
        self.horizontalLayout_109.addWidget(self.PixmapLabel_59)
        self.CheckBox_B41 = CheckBox(self.layoutWidget_101)
        self.CheckBox_B41.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B41.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B41.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B41.setChecked(True)
        self.CheckBox_B41.setObjectName("CheckBox_B41")
        self.horizontalLayout_109.addWidget(self.CheckBox_B41)
        self.gridLayout_15.addWidget(self.CardWidget_53, 83, 1, 1, 1)
        self.HorizontalSeparator_47 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_47.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_47.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_47.setObjectName("HorizontalSeparator_47")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_47, 48, 1, 1, 1)
        self.HorizontalSeparator_72 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_72.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_72.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_72.setObjectName("HorizontalSeparator_72")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_72, 74, 1, 1, 1)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        spacerItem68 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem68, 1, 1, 1, 1)
        spacerItem69 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem69, 1, 2, 1, 1)
        self.CardWidget_189 = CardWidget(self.layoutWidget1)
        self.CardWidget_189.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_189.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_189.setObjectName("CardWidget_189")
        self.oak_planks = CheckBox(self.CardWidget_189)
        self.oak_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.oak_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.oak_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.oak_planks.setFont(font)
        self.oak_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("icon/oak_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oak_planks.setIcon(icon52)
        self.oak_planks.setIconSize(QtCore.QSize(16, 16))
        self.oak_planks.setChecked(True)
        self.oak_planks.setTristate(False)
        self.oak_planks.setObjectName("oak_planks")
        self.gridLayout_24.addWidget(self.CardWidget_189, 1, 0, 1, 1)
        spacerItem70 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_24.addItem(spacerItem70, 2, 1, 1, 1)
        spacerItem71 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_24.addItem(spacerItem71, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_24, 27, 3, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.CardWidget_237 = CardWidget(self.layoutWidget1)
        self.CardWidget_237.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_237.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_237.setObjectName("CardWidget_237")
        self.purple_concrete = CheckBox(self.CardWidget_237)
        self.purple_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.purple_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.purple_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.purple_concrete.setFont(font)
        self.purple_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap("icon/purple_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.purple_concrete.setIcon(icon53)
        self.purple_concrete.setIconSize(QtCore.QSize(16, 16))
        self.purple_concrete.setChecked(True)
        self.purple_concrete.setTristate(False)
        self.purple_concrete.setObjectName("purple_concrete")
        self.gridLayout_21.addWidget(self.CardWidget_237, 1, 0, 1, 1)
        self.CardWidget_238 = CardWidget(self.layoutWidget1)
        self.CardWidget_238.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_238.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_238.setObjectName("CardWidget_238")
        self.purple_stained_glass = CheckBox(self.CardWidget_238)
        self.purple_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.purple_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.purple_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.purple_stained_glass.setFont(font)
        self.purple_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap("icon/purple_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.purple_stained_glass.setIcon(icon54)
        self.purple_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.purple_stained_glass.setTristate(False)
        self.purple_stained_glass.setObjectName("purple_stained_glass")
        self.gridLayout_21.addWidget(self.CardWidget_238, 1, 2, 1, 1)
        self.CardWidget_239 = CardWidget(self.layoutWidget1)
        self.CardWidget_239.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_239.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_239.setObjectName("CardWidget_239")
        self.amethyst_block = CheckBox(self.CardWidget_239)
        self.amethyst_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.amethyst_block.setMinimumSize(QtCore.QSize(17, 16))
        self.amethyst_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.amethyst_block.setFont(font)
        self.amethyst_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("icon/amethyst_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.amethyst_block.setIcon(icon55)
        self.amethyst_block.setIconSize(QtCore.QSize(16, 16))
        self.amethyst_block.setTristate(False)
        self.amethyst_block.setObjectName("amethyst_block")
        self.gridLayout_21.addWidget(self.CardWidget_239, 3, 0, 1, 1)
        spacerItem72 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem72, 4, 1, 1, 1)
        self.CardWidget_240 = CardWidget(self.layoutWidget1)
        self.CardWidget_240.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_240.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_240.setObjectName("CardWidget_240")
        self.purple_wool = CheckBox(self.CardWidget_240)
        self.purple_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.purple_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.purple_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.purple_wool.setFont(font)
        self.purple_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap("icon/purple_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.purple_wool.setIcon(icon56)
        self.purple_wool.setIconSize(QtCore.QSize(16, 16))
        self.purple_wool.setTristate(False)
        self.purple_wool.setObjectName("purple_wool")
        self.gridLayout_21.addWidget(self.CardWidget_240, 1, 1, 1, 1)
        spacerItem73 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem73, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_21, 49, 3, 1, 1)
        self.gridLayout_66 = QtWidgets.QGridLayout()
        self.gridLayout_66.setObjectName("gridLayout_66")
        spacerItem74 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_66.addItem(spacerItem74, 1, 1, 1, 1)
        spacerItem75 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_66.addItem(spacerItem75, 1, 2, 1, 1)
        self.CardWidget_307 = CardWidget(self.layoutWidget1)
        self.CardWidget_307.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_307.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_307.setObjectName("CardWidget_307")
        self.raw_iron_block = CheckBox(self.CardWidget_307)
        self.raw_iron_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.raw_iron_block.setMinimumSize(QtCore.QSize(17, 16))
        self.raw_iron_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.raw_iron_block.setFont(font)
        self.raw_iron_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap("icon/raw_iron_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.raw_iron_block.setIcon(icon57)
        self.raw_iron_block.setIconSize(QtCore.QSize(16, 16))
        self.raw_iron_block.setChecked(True)
        self.raw_iron_block.setTristate(False)
        self.raw_iron_block.setObjectName("raw_iron_block")
        self.gridLayout_66.addWidget(self.CardWidget_307, 1, 0, 1, 1)
        spacerItem76 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_66.addItem(spacerItem76, 2, 1, 1, 1)
        spacerItem77 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_66.addItem(spacerItem77, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_66, 121, 3, 1, 1)
        self.VerticalSeparator_47 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_47.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_47.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_47.setObjectName("VerticalSeparator_47")
        self.gridLayout_15.addWidget(self.VerticalSeparator_47, 31, 2, 1, 1)
        self.CardWidget_73 = CardWidget(self.layoutWidget1)
        self.CardWidget_73.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_73.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_73.setObjectName("CardWidget_73")
        self.layoutWidget_140 = QtWidgets.QWidget(self.CardWidget_73)
        self.layoutWidget_140.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_140.setObjectName("layoutWidget_140")
        self.horizontalLayout_149 = QtWidgets.QHBoxLayout(self.layoutWidget_140)
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_149.setObjectName("horizontalLayout_149")
        self.PixmapLabel_79 = PixmapLabel(self.layoutWidget_140)
        self.PixmapLabel_79.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_79.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_79.setObjectName("PixmapLabel_79")
        self.horizontalLayout_149.addWidget(self.PixmapLabel_79)
        self.CheckBox_B60 = CheckBox(self.layoutWidget_140)
        self.CheckBox_B60.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B60.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B60.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B60.setChecked(True)
        self.CheckBox_B60.setObjectName("CheckBox_B60")
        self.horizontalLayout_149.addWidget(self.CheckBox_B60)
        self.gridLayout_15.addWidget(self.CardWidget_73, 121, 1, 1, 1)
        self.HorizontalSeparator_20 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_20.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_20.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_20.setObjectName("HorizontalSeparator_20")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_20, 20, 3, 1, 1)
        self.VerticalSeparator_12 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_12.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_12.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_12.setObjectName("VerticalSeparator_12")
        self.gridLayout_15.addWidget(self.VerticalSeparator_12, 101, 2, 1, 1)
        self.HorizontalSeparator_105 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_105.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_105.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_105.setObjectName("HorizontalSeparator_105")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_105, 106, 3, 1, 1)
        self.CardWidget_55 = CardWidget(self.layoutWidget1)
        self.CardWidget_55.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_55.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_55.setObjectName("CardWidget_55")
        self.layoutWidget_105 = QtWidgets.QWidget(self.CardWidget_55)
        self.layoutWidget_105.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_105.setObjectName("layoutWidget_105")
        self.horizontalLayout_113 = QtWidgets.QHBoxLayout(self.layoutWidget_105)
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_113.setObjectName("horizontalLayout_113")
        self.PixmapLabel_61 = PixmapLabel(self.layoutWidget_105)
        self.PixmapLabel_61.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_61.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_61.setObjectName("PixmapLabel_61")
        self.horizontalLayout_113.addWidget(self.PixmapLabel_61)
        self.CheckBox_B43 = CheckBox(self.layoutWidget_105)
        self.CheckBox_B43.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B43.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B43.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B43.setChecked(True)
        self.CheckBox_B43.setObjectName("CheckBox_B43")
        self.horizontalLayout_113.addWidget(self.CheckBox_B43)
        self.gridLayout_15.addWidget(self.CardWidget_55, 87, 1, 1, 1)
        self.HorizontalSeparator_36 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_36.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_36.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_36.setObjectName("HorizontalSeparator_36")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_36, 36, 3, 1, 1)
        self.gridLayout_38 = QtWidgets.QGridLayout()
        self.gridLayout_38.setObjectName("gridLayout_38")
        spacerItem78 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem78, 1, 1, 1, 1)
        spacerItem79 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem79, 1, 2, 1, 1)
        self.CardWidget_197 = CardWidget(self.layoutWidget1)
        self.CardWidget_197.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_197.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_197.setObjectName("CardWidget_197")
        self.emerald_block = CheckBox(self.CardWidget_197)
        self.emerald_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.emerald_block.setMinimumSize(QtCore.QSize(17, 16))
        self.emerald_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.emerald_block.setFont(font)
        self.emerald_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap("icon/emerald_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emerald_block.setIcon(icon58)
        self.emerald_block.setIconSize(QtCore.QSize(16, 16))
        self.emerald_block.setChecked(True)
        self.emerald_block.setTristate(False)
        self.emerald_block.setObjectName("emerald_block")
        self.gridLayout_38.addWidget(self.CardWidget_197, 1, 0, 1, 1)
        spacerItem80 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_38.addItem(spacerItem80, 2, 1, 1, 1)
        spacerItem81 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_38.addItem(spacerItem81, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_38, 67, 3, 1, 1)
        self.HorizontalSeparator_19 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_19.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_19.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_19.setObjectName("HorizontalSeparator_19")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_19, 20, 1, 1, 1)
        self.HorizontalSeparator_5 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_5.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_5.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_5.setObjectName("HorizontalSeparator_5")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_5, 6, 1, 1, 1)
        self.VerticalSeparator_22 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_22.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_22.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_22.setObjectName("VerticalSeparator_22")
        self.gridLayout_15.addWidget(self.VerticalSeparator_22, 81, 2, 1, 1)
        self.CardWidget_33 = CardWidget(self.layoutWidget1)
        self.CardWidget_33.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_33.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_33.setObjectName("CardWidget_33")
        self.layoutWidget_61 = QtWidgets.QWidget(self.CardWidget_33)
        self.layoutWidget_61.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_61.setObjectName("layoutWidget_61")
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout(self.layoutWidget_61)
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.PixmapLabel_39 = PixmapLabel(self.layoutWidget_61)
        self.PixmapLabel_39.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_39.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_39.setObjectName("PixmapLabel_39")
        self.horizontalLayout_69.addWidget(self.PixmapLabel_39)
        self.CheckBox_B21 = CheckBox(self.layoutWidget_61)
        self.CheckBox_B21.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B21.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B21.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B21.setChecked(True)
        self.CheckBox_B21.setObjectName("CheckBox_B21")
        self.horizontalLayout_69.addWidget(self.CheckBox_B21)
        self.gridLayout_15.addWidget(self.CardWidget_33, 43, 1, 1, 1)
        self.HorizontalSeparator_98 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_98.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_98.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_98.setObjectName("HorizontalSeparator_98")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_98, 100, 1, 1, 1)
        self.VerticalSeparator_36 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_36.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_36.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_36.setObjectName("VerticalSeparator_36")
        self.gridLayout_15.addWidget(self.VerticalSeparator_36, 53, 2, 1, 1)
        self.CardWidget_65 = CardWidget(self.layoutWidget1)
        self.CardWidget_65.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_65.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_65.setObjectName("CardWidget_65")
        self.layoutWidget_125 = QtWidgets.QWidget(self.CardWidget_65)
        self.layoutWidget_125.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_125.setObjectName("layoutWidget_125")
        self.horizontalLayout_133 = QtWidgets.QHBoxLayout(self.layoutWidget_125)
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_133.setObjectName("horizontalLayout_133")
        self.PixmapLabel_71 = PixmapLabel(self.layoutWidget_125)
        self.PixmapLabel_71.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_71.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_71.setObjectName("PixmapLabel_71")
        self.horizontalLayout_133.addWidget(self.PixmapLabel_71)
        self.CheckBox_B53 = CheckBox(self.layoutWidget_125)
        self.CheckBox_B53.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B53.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B53.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B53.setChecked(True)
        self.CheckBox_B53.setObjectName("CheckBox_B53")
        self.horizontalLayout_133.addWidget(self.CheckBox_B53)
        self.gridLayout_15.addWidget(self.CardWidget_65, 107, 1, 1, 1)
        self.CardWidget_64 = CardWidget(self.layoutWidget1)
        self.CardWidget_64.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_64.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_64.setObjectName("CardWidget_64")
        self.layoutWidget_123 = QtWidgets.QWidget(self.CardWidget_64)
        self.layoutWidget_123.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_123.setObjectName("layoutWidget_123")
        self.horizontalLayout_131 = QtWidgets.QHBoxLayout(self.layoutWidget_123)
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_131.setObjectName("horizontalLayout_131")
        self.PixmapLabel_70 = PixmapLabel(self.layoutWidget_123)
        self.PixmapLabel_70.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_70.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_70.setObjectName("PixmapLabel_70")
        self.horizontalLayout_131.addWidget(self.PixmapLabel_70)
        self.CheckBox_B52 = CheckBox(self.layoutWidget_123)
        self.CheckBox_B52.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B52.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B52.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B52.setChecked(True)
        self.CheckBox_B52.setObjectName("CheckBox_B52")
        self.horizontalLayout_131.addWidget(self.CheckBox_B52)
        self.gridLayout_15.addWidget(self.CardWidget_64, 105, 1, 1, 1)
        self.CardWidget_69 = CardWidget(self.layoutWidget1)
        self.CardWidget_69.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_69.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_69.setObjectName("CardWidget_69")
        self.layoutWidget_133 = QtWidgets.QWidget(self.CardWidget_69)
        self.layoutWidget_133.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_133.setObjectName("layoutWidget_133")
        self.horizontalLayout_141 = QtWidgets.QHBoxLayout(self.layoutWidget_133)
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_141.setObjectName("horizontalLayout_141")
        self.PixmapLabel_75 = PixmapLabel(self.layoutWidget_133)
        self.PixmapLabel_75.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_75.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_75.setObjectName("PixmapLabel_75")
        self.horizontalLayout_141.addWidget(self.PixmapLabel_75)
        self.CheckBox_B57 = CheckBox(self.layoutWidget_133)
        self.CheckBox_B57.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B57.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B57.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B57.setChecked(True)
        self.CheckBox_B57.setObjectName("CheckBox_B57")
        self.horizontalLayout_141.addWidget(self.CheckBox_B57)
        self.gridLayout_15.addWidget(self.CardWidget_69, 115, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CardWidget_202 = CardWidget(self.layoutWidget1)
        self.CardWidget_202.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_202.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_202.setObjectName("CardWidget_202")
        self.coarse_dirt = CheckBox(self.CardWidget_202)
        self.coarse_dirt.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.coarse_dirt.setMinimumSize(QtCore.QSize(17, 16))
        self.coarse_dirt.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.coarse_dirt.setFont(font)
        self.coarse_dirt.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon59 = QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap("icon/coarse_dirt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.coarse_dirt.setIcon(icon59)
        self.coarse_dirt.setIconSize(QtCore.QSize(16, 16))
        self.coarse_dirt.setChecked(True)
        self.coarse_dirt.setTristate(False)
        self.coarse_dirt.setObjectName("coarse_dirt")
        self.gridLayout_2.addWidget(self.CardWidget_202, 1, 0, 1, 1)
        self.CardWidget_204 = CardWidget(self.layoutWidget1)
        self.CardWidget_204.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_204.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_204.setObjectName("CardWidget_204")
        self.jungle_planks = CheckBox(self.CardWidget_204)
        self.jungle_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.jungle_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.jungle_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jungle_planks.setFont(font)
        self.jungle_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon60 = QtGui.QIcon()
        icon60.addPixmap(QtGui.QPixmap("icon/jungle_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jungle_planks.setIcon(icon60)
        self.jungle_planks.setIconSize(QtCore.QSize(16, 16))
        self.jungle_planks.setTristate(False)
        self.jungle_planks.setObjectName("jungle_planks")
        self.gridLayout_2.addWidget(self.CardWidget_204, 1, 2, 1, 1)
        self.CardWidget_205 = CardWidget(self.layoutWidget1)
        self.CardWidget_205.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_205.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_205.setObjectName("CardWidget_205")
        self.brown_mushroom_block = CheckBox(self.CardWidget_205)
        self.brown_mushroom_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.brown_mushroom_block.setMinimumSize(QtCore.QSize(17, 16))
        self.brown_mushroom_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.brown_mushroom_block.setFont(font)
        self.brown_mushroom_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon61 = QtGui.QIcon()
        icon61.addPixmap(QtGui.QPixmap("icon/brown_mushroom_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brown_mushroom_block.setIcon(icon61)
        self.brown_mushroom_block.setIconSize(QtCore.QSize(16, 16))
        self.brown_mushroom_block.setTristate(False)
        self.brown_mushroom_block.setObjectName("brown_mushroom_block")
        self.gridLayout_2.addWidget(self.CardWidget_205, 3, 0, 1, 1)
        spacerItem82 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem82, 4, 1, 1, 1)
        self.CardWidget_206 = CardWidget(self.layoutWidget1)
        self.CardWidget_206.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_206.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_206.setObjectName("CardWidget_206")
        self.dirt = CheckBox(self.CardWidget_206)
        self.dirt.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.dirt.setMinimumSize(QtCore.QSize(17, 16))
        self.dirt.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dirt.setFont(font)
        self.dirt.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon62 = QtGui.QIcon()
        icon62.addPixmap(QtGui.QPixmap("icon/dirt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dirt.setIcon(icon62)
        self.dirt.setIconSize(QtCore.QSize(16, 16))
        self.dirt.setTristate(False)
        self.dirt.setObjectName("dirt")
        self.gridLayout_2.addWidget(self.CardWidget_206, 3, 1, 1, 1)
        self.CardWidget_203 = CardWidget(self.layoutWidget1)
        self.CardWidget_203.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_203.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_203.setObjectName("CardWidget_203")
        self.polished_granite = CheckBox(self.CardWidget_203)
        self.polished_granite.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.polished_granite.setMinimumSize(QtCore.QSize(17, 16))
        self.polished_granite.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.polished_granite.setFont(font)
        self.polished_granite.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon63 = QtGui.QIcon()
        icon63.addPixmap(QtGui.QPixmap("icon/polished_granite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polished_granite.setIcon(icon63)
        self.polished_granite.setIconSize(QtCore.QSize(16, 16))
        self.polished_granite.setTristate(False)
        self.polished_granite.setObjectName("polished_granite")
        self.gridLayout_2.addWidget(self.CardWidget_203, 1, 1, 1, 1)
        spacerItem83 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem83, 0, 1, 1, 1)
        self.CardWidget_207 = CardWidget(self.layoutWidget1)
        self.CardWidget_207.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_207.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_207.setObjectName("CardWidget_207")
        self.packed_mud = CheckBox(self.CardWidget_207)
        self.packed_mud.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.packed_mud.setMinimumSize(QtCore.QSize(17, 16))
        self.packed_mud.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.packed_mud.setFont(font)
        self.packed_mud.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon64 = QtGui.QIcon()
        icon64.addPixmap(QtGui.QPixmap("icon/packed_mud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.packed_mud.setIcon(icon64)
        self.packed_mud.setIconSize(QtCore.QSize(16, 16))
        self.packed_mud.setTristate(False)
        self.packed_mud.setObjectName("packed_mud")
        self.gridLayout_2.addWidget(self.CardWidget_207, 3, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_2, 21, 3, 1, 1)
        self.gridLayout_64 = QtWidgets.QGridLayout()
        self.gridLayout_64.setObjectName("gridLayout_64")
        spacerItem84 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_64.addItem(spacerItem84, 1, 1, 1, 1)
        spacerItem85 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_64.addItem(spacerItem85, 1, 2, 1, 1)
        self.CardWidget_305 = CardWidget(self.layoutWidget1)
        self.CardWidget_305.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_305.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_305.setObjectName("CardWidget_305")
        self.warped_wart_block = CheckBox(self.CardWidget_305)
        self.warped_wart_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.warped_wart_block.setMinimumSize(QtCore.QSize(17, 16))
        self.warped_wart_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.warped_wart_block.setFont(font)
        self.warped_wart_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon65 = QtGui.QIcon()
        icon65.addPixmap(QtGui.QPixmap("icon/warped_wart_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.warped_wart_block.setIcon(icon65)
        self.warped_wart_block.setIconSize(QtCore.QSize(16, 16))
        self.warped_wart_block.setChecked(True)
        self.warped_wart_block.setTristate(False)
        self.warped_wart_block.setObjectName("warped_wart_block")
        self.gridLayout_64.addWidget(self.CardWidget_305, 1, 0, 1, 1)
        spacerItem86 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_64.addItem(spacerItem86, 2, 1, 1, 1)
        spacerItem87 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_64.addItem(spacerItem87, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_64, 117, 3, 1, 1)
        self.gridLayout_52 = QtWidgets.QGridLayout()
        self.gridLayout_52.setObjectName("gridLayout_52")
        spacerItem88 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_52.addItem(spacerItem88, 1, 1, 1, 1)
        spacerItem89 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_52.addItem(spacerItem89, 1, 2, 1, 1)
        self.CardWidget_291 = CardWidget(self.layoutWidget1)
        self.CardWidget_291.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_291.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_291.setObjectName("CardWidget_291")
        self.blue_terracotta = CheckBox(self.CardWidget_291)
        self.blue_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.blue_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.blue_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.blue_terracotta.setFont(font)
        self.blue_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon66 = QtGui.QIcon()
        icon66.addPixmap(QtGui.QPixmap("icon/blue_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blue_terracotta.setIcon(icon66)
        self.blue_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.blue_terracotta.setChecked(True)
        self.blue_terracotta.setTristate(False)
        self.blue_terracotta.setObjectName("blue_terracotta")
        self.gridLayout_52.addWidget(self.CardWidget_291, 1, 0, 1, 1)
        spacerItem90 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_52.addItem(spacerItem90, 2, 1, 1, 1)
        spacerItem91 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_52.addItem(spacerItem91, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_52, 95, 3, 1, 1)
        self.HorizontalSeparator_89 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_89.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_89.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_89.setObjectName("HorizontalSeparator_89")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_89, 90, 3, 1, 1)
        self.gridLayout_55 = QtWidgets.QGridLayout()
        self.gridLayout_55.setObjectName("gridLayout_55")
        spacerItem92 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_55.addItem(spacerItem92, 1, 1, 1, 1)
        spacerItem93 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_55.addItem(spacerItem93, 1, 2, 1, 1)
        self.CardWidget_294 = CardWidget(self.layoutWidget1)
        self.CardWidget_294.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_294.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_294.setObjectName("CardWidget_294")
        self.red_terracotta = CheckBox(self.CardWidget_294)
        self.red_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.red_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.red_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.red_terracotta.setFont(font)
        self.red_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon67 = QtGui.QIcon()
        icon67.addPixmap(QtGui.QPixmap("icon/red_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.red_terracotta.setIcon(icon67)
        self.red_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.red_terracotta.setChecked(True)
        self.red_terracotta.setTristate(False)
        self.red_terracotta.setObjectName("red_terracotta")
        self.gridLayout_55.addWidget(self.CardWidget_294, 1, 0, 1, 1)
        spacerItem94 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_55.addItem(spacerItem94, 2, 1, 1, 1)
        spacerItem95 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_55.addItem(spacerItem95, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_55, 101, 3, 1, 1)
        self.HorizontalSeparator_104 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_104.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_104.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_104.setObjectName("HorizontalSeparator_104")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_104, 106, 1, 1, 1)
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.CardWidget_273 = CardWidget(self.layoutWidget1)
        self.CardWidget_273.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_273.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_273.setObjectName("CardWidget_273")
        self.netherrack = CheckBox(self.CardWidget_273)
        self.netherrack.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.netherrack.setMinimumSize(QtCore.QSize(17, 16))
        self.netherrack.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.netherrack.setFont(font)
        self.netherrack.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon68 = QtGui.QIcon()
        icon68.addPixmap(QtGui.QPixmap("icon/netherrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.netherrack.setIcon(icon68)
        self.netherrack.setIconSize(QtCore.QSize(16, 16))
        self.netherrack.setChecked(True)
        self.netherrack.setTristate(False)
        self.netherrack.setObjectName("netherrack")
        self.gridLayout_40.addWidget(self.CardWidget_273, 1, 0, 1, 1)
        spacerItem96 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_40.addItem(spacerItem96, 2, 1, 1, 1)
        spacerItem97 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_40.addItem(spacerItem97, 0, 1, 1, 1)
        self.CardWidget_274 = CardWidget(self.layoutWidget1)
        self.CardWidget_274.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_274.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_274.setObjectName("CardWidget_274")
        self.nether_bricks = CheckBox(self.CardWidget_274)
        self.nether_bricks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.nether_bricks.setMinimumSize(QtCore.QSize(17, 16))
        self.nether_bricks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nether_bricks.setFont(font)
        self.nether_bricks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon69 = QtGui.QIcon()
        icon69.addPixmap(QtGui.QPixmap("icon/nether_bricks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nether_bricks.setIcon(icon69)
        self.nether_bricks.setIconSize(QtCore.QSize(16, 16))
        self.nether_bricks.setTristate(False)
        self.nether_bricks.setObjectName("nether_bricks")
        self.gridLayout_40.addWidget(self.CardWidget_274, 1, 1, 1, 1)
        self.CardWidget_275 = CardWidget(self.layoutWidget1)
        self.CardWidget_275.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_275.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_275.setObjectName("CardWidget_275")
        self.magma_block = CheckBox(self.CardWidget_275)
        self.magma_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.magma_block.setMinimumSize(QtCore.QSize(17, 16))
        self.magma_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.magma_block.setFont(font)
        self.magma_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon70 = QtGui.QIcon()
        icon70.addPixmap(QtGui.QPixmap("icon/magma_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.magma_block.setIcon(icon70)
        self.magma_block.setIconSize(QtCore.QSize(16, 16))
        self.magma_block.setTristate(False)
        self.magma_block.setObjectName("magma_block")
        self.gridLayout_40.addWidget(self.CardWidget_275, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_40, 71, 3, 1, 1)
        self.HorizontalSeparator_108 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_108.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_108.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_108.setObjectName("HorizontalSeparator_108")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_108, 110, 1, 1, 1)
        self.HorizontalSeparator_55 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_55.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_55.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_55.setObjectName("HorizontalSeparator_55")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_55, 56, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.CardWidget_222 = CardWidget(self.layoutWidget1)
        self.CardWidget_222.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_222.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_222.setObjectName("CardWidget_222")
        self.pink_concrete = CheckBox(self.CardWidget_222)
        self.pink_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.pink_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.pink_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pink_concrete.setFont(font)
        self.pink_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon71 = QtGui.QIcon()
        icon71.addPixmap(QtGui.QPixmap("icon/pink_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pink_concrete.setIcon(icon71)
        self.pink_concrete.setIconSize(QtCore.QSize(16, 16))
        self.pink_concrete.setChecked(True)
        self.pink_concrete.setTristate(False)
        self.pink_concrete.setObjectName("pink_concrete")
        self.gridLayout_6.addWidget(self.CardWidget_222, 1, 0, 1, 1)
        self.CardWidget_223 = CardWidget(self.layoutWidget1)
        self.CardWidget_223.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_223.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_223.setObjectName("CardWidget_223")
        self.pink_stained_glass = CheckBox(self.CardWidget_223)
        self.pink_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.pink_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.pink_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pink_stained_glass.setFont(font)
        self.pink_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon72 = QtGui.QIcon()
        icon72.addPixmap(QtGui.QPixmap("icon/pink_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pink_stained_glass.setIcon(icon72)
        self.pink_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.pink_stained_glass.setTristate(False)
        self.pink_stained_glass.setObjectName("pink_stained_glass")
        self.gridLayout_6.addWidget(self.CardWidget_223, 1, 2, 1, 1)
        self.CardWidget_224 = CardWidget(self.layoutWidget1)
        self.CardWidget_224.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_224.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_224.setObjectName("CardWidget_224")
        self.pearlescent_froglight_top = CheckBox(self.CardWidget_224)
        self.pearlescent_froglight_top.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.pearlescent_froglight_top.setMinimumSize(QtCore.QSize(17, 16))
        self.pearlescent_froglight_top.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pearlescent_froglight_top.setFont(font)
        self.pearlescent_froglight_top.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon73 = QtGui.QIcon()
        icon73.addPixmap(QtGui.QPixmap("icon/pearlescent_froglight_top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pearlescent_froglight_top.setIcon(icon73)
        self.pearlescent_froglight_top.setIconSize(QtCore.QSize(16, 16))
        self.pearlescent_froglight_top.setTristate(False)
        self.pearlescent_froglight_top.setObjectName("pearlescent_froglight_top")
        self.gridLayout_6.addWidget(self.CardWidget_224, 3, 0, 1, 1)
        spacerItem98 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem98, 4, 1, 1, 1)
        self.CardWidget_225 = CardWidget(self.layoutWidget1)
        self.CardWidget_225.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_225.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_225.setObjectName("CardWidget_225")
        self.pink_wool = CheckBox(self.CardWidget_225)
        self.pink_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.pink_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.pink_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pink_wool.setFont(font)
        self.pink_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon74 = QtGui.QIcon()
        icon74.addPixmap(QtGui.QPixmap("icon/pink_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pink_wool.setIcon(icon74)
        self.pink_wool.setIconSize(QtCore.QSize(16, 16))
        self.pink_wool.setTristate(False)
        self.pink_wool.setObjectName("pink_wool")
        self.gridLayout_6.addWidget(self.CardWidget_225, 1, 1, 1, 1)
        spacerItem99 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem99, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_6, 41, 3, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem100 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem100, 1, 1, 1, 1)
        spacerItem101 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem101, 1, 2, 1, 1)
        self.CardWidget_166 = CardWidget(self.layoutWidget1)
        self.CardWidget_166.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_166.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_166.setObjectName("CardWidget_166")
        self.redstone_block = CheckBox(self.CardWidget_166)
        self.redstone_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.redstone_block.setMinimumSize(QtCore.QSize(17, 16))
        self.redstone_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.redstone_block.setFont(font)
        self.redstone_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon75 = QtGui.QIcon()
        icon75.addPixmap(QtGui.QPixmap("icon/redstone_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redstone_block.setIcon(icon75)
        self.redstone_block.setIconSize(QtCore.QSize(16, 16))
        self.redstone_block.setChecked(True)
        self.redstone_block.setTristate(False)
        self.redstone_block.setObjectName("redstone_block")
        self.gridLayout_11.addWidget(self.CardWidget_166, 1, 0, 1, 1)
        spacerItem102 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem102, 2, 1, 1, 1)
        spacerItem103 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem103, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_11, 9, 3, 1, 1)
        self.HorizontalSeparator_41 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_41.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_41.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_41.setObjectName("HorizontalSeparator_41")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_41, 42, 1, 1, 1)
        self.HorizontalSeparator_50 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_50.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_50.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_50.setObjectName("HorizontalSeparator_50")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_50, 50, 3, 1, 1)
        self.VerticalSeparator_55 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_55.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_55.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_55.setObjectName("VerticalSeparator_55")
        self.gridLayout_15.addWidget(self.VerticalSeparator_55, 15, 2, 1, 1)
        self.CardWidget_45 = CardWidget(self.layoutWidget1)
        self.CardWidget_45.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_45.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_45.setObjectName("CardWidget_45")
        self.layoutWidget_85 = QtWidgets.QWidget(self.CardWidget_45)
        self.layoutWidget_85.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_85.setObjectName("layoutWidget_85")
        self.horizontalLayout_93 = QtWidgets.QHBoxLayout(self.layoutWidget_85)
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")
        self.PixmapLabel_51 = PixmapLabel(self.layoutWidget_85)
        self.PixmapLabel_51.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_51.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_51.setObjectName("PixmapLabel_51")
        self.horizontalLayout_93.addWidget(self.PixmapLabel_51)
        self.CheckBox_B33 = CheckBox(self.layoutWidget_85)
        self.CheckBox_B33.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B33.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B33.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B33.setChecked(True)
        self.CheckBox_B33.setObjectName("CheckBox_B33")
        self.horizontalLayout_93.addWidget(self.CheckBox_B33)
        self.gridLayout_15.addWidget(self.CardWidget_45, 67, 1, 1, 1)
        self.VerticalSeparator_23 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_23.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_23.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_23.setObjectName("VerticalSeparator_23")
        self.gridLayout_15.addWidget(self.VerticalSeparator_23, 79, 2, 1, 1)
        self.VerticalSeparator_14 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_14.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_14.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_14.setObjectName("VerticalSeparator_14")
        self.gridLayout_15.addWidget(self.VerticalSeparator_14, 97, 2, 1, 1)
        self.HorizontalSeparator_35 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_35.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_35.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_35.setObjectName("HorizontalSeparator_35")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_35, 36, 1, 1, 1)
        self.gridLayout_42 = QtWidgets.QGridLayout()
        self.gridLayout_42.setObjectName("gridLayout_42")
        spacerItem104 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_42.addItem(spacerItem104, 1, 1, 1, 1)
        spacerItem105 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_42.addItem(spacerItem105, 1, 2, 1, 1)
        self.CardWidget_200 = CardWidget(self.layoutWidget1)
        self.CardWidget_200.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_200.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_200.setObjectName("CardWidget_200")
        self.orange_terracotta = CheckBox(self.CardWidget_200)
        self.orange_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.orange_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.orange_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.orange_terracotta.setFont(font)
        self.orange_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon76 = QtGui.QIcon()
        icon76.addPixmap(QtGui.QPixmap("icon/orange_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.orange_terracotta.setIcon(icon76)
        self.orange_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.orange_terracotta.setChecked(True)
        self.orange_terracotta.setTristate(False)
        self.orange_terracotta.setObjectName("orange_terracotta")
        self.gridLayout_42.addWidget(self.CardWidget_200, 1, 0, 1, 1)
        spacerItem106 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_42.addItem(spacerItem106, 2, 1, 1, 1)
        spacerItem107 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_42.addItem(spacerItem107, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_42, 75, 3, 1, 1)
        self.VerticalSeparator_30 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_30.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_30.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_30.setObjectName("VerticalSeparator_30")
        self.gridLayout_15.addWidget(self.VerticalSeparator_30, 65, 2, 1, 1)
        self.gridLayout_50 = QtWidgets.QGridLayout()
        self.gridLayout_50.setObjectName("gridLayout_50")
        spacerItem108 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_50.addItem(spacerItem108, 1, 2, 1, 1)
        self.CardWidget_288 = CardWidget(self.layoutWidget1)
        self.CardWidget_288.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_288.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_288.setObjectName("CardWidget_288")
        self.mud = CheckBox(self.CardWidget_288)
        self.mud.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.mud.setMinimumSize(QtCore.QSize(17, 16))
        self.mud.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mud.setFont(font)
        self.mud.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon77 = QtGui.QIcon()
        icon77.addPixmap(QtGui.QPixmap("icon/mud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mud.setIcon(icon77)
        self.mud.setIconSize(QtCore.QSize(16, 16))
        self.mud.setTristate(False)
        self.mud.setObjectName("mud")
        self.gridLayout_50.addWidget(self.CardWidget_288, 1, 1, 1, 1)
        spacerItem109 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_50.addItem(spacerItem109, 2, 1, 1, 1)
        spacerItem110 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_50.addItem(spacerItem110, 0, 1, 1, 1)
        self.CardWidget_289 = CardWidget(self.layoutWidget1)
        self.CardWidget_289.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_289.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_289.setObjectName("CardWidget_289")
        self.cyan_terracotta = CheckBox(self.CardWidget_289)
        self.cyan_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.cyan_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.cyan_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cyan_terracotta.setFont(font)
        self.cyan_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon78 = QtGui.QIcon()
        icon78.addPixmap(QtGui.QPixmap("icon/cyan_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cyan_terracotta.setIcon(icon78)
        self.cyan_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.cyan_terracotta.setChecked(True)
        self.cyan_terracotta.setTristate(False)
        self.cyan_terracotta.setObjectName("cyan_terracotta")
        self.gridLayout_50.addWidget(self.CardWidget_289, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_50, 91, 3, 1, 1)
        self.HorizontalSeparator_75 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_75.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_75.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_75.setObjectName("HorizontalSeparator_75")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_75, 76, 3, 1, 1)
        self.HorizontalSeparator_102 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_102.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_102.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_102.setObjectName("HorizontalSeparator_102")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_102, 104, 1, 1, 1)
        self.CardWidget_49 = CardWidget(self.layoutWidget1)
        self.CardWidget_49.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_49.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_49.setObjectName("CardWidget_49")
        self.layoutWidget_93 = QtWidgets.QWidget(self.CardWidget_49)
        self.layoutWidget_93.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_93.setObjectName("layoutWidget_93")
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout(self.layoutWidget_93)
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.PixmapLabel_55 = PixmapLabel(self.layoutWidget_93)
        self.PixmapLabel_55.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_55.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_55.setObjectName("PixmapLabel_55")
        self.horizontalLayout_101.addWidget(self.PixmapLabel_55)
        self.CheckBox_B37 = CheckBox(self.layoutWidget_93)
        self.CheckBox_B37.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B37.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B37.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B37.setChecked(True)
        self.CheckBox_B37.setObjectName("CheckBox_B37")
        self.horizontalLayout_101.addWidget(self.CheckBox_B37)
        self.gridLayout_15.addWidget(self.CardWidget_49, 75, 1, 1, 1)
        self.HorizontalSeparator_30 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_30.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_30.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_30.setObjectName("HorizontalSeparator_30")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_30, 30, 3, 1, 1)
        self.HorizontalSeparator_49 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_49.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_49.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_49.setObjectName("HorizontalSeparator_49")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_49, 50, 1, 1, 1)
        self.VerticalSeparator_10 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_10.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_10.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_10.setObjectName("VerticalSeparator_10")
        self.gridLayout_15.addWidget(self.VerticalSeparator_10, 105, 2, 1, 1)
        self.HorizontalSeparator_69 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_69.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_69.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_69.setObjectName("HorizontalSeparator_69")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_69, 70, 3, 1, 1)
        self.CardWidget_51 = CardWidget(self.layoutWidget1)
        self.CardWidget_51.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_51.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_51.setObjectName("CardWidget_51")
        self.layoutWidget_97 = QtWidgets.QWidget(self.CardWidget_51)
        self.layoutWidget_97.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_97.setObjectName("layoutWidget_97")
        self.horizontalLayout_105 = QtWidgets.QHBoxLayout(self.layoutWidget_97)
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_105.setObjectName("horizontalLayout_105")
        self.PixmapLabel_57 = PixmapLabel(self.layoutWidget_97)
        self.PixmapLabel_57.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_57.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_57.setObjectName("PixmapLabel_57")
        self.horizontalLayout_105.addWidget(self.PixmapLabel_57)
        self.CheckBox_B39 = CheckBox(self.layoutWidget_97)
        self.CheckBox_B39.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B39.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B39.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B39.setChecked(True)
        self.CheckBox_B39.setObjectName("CheckBox_B39")
        self.horizontalLayout_105.addWidget(self.CheckBox_B39)
        self.gridLayout_15.addWidget(self.CardWidget_51, 79, 1, 1, 1)
        self.VerticalSeparator_57 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_57.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_57.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_57.setObjectName("VerticalSeparator_57")
        self.gridLayout_15.addWidget(self.VerticalSeparator_57, 11, 2, 1, 1)
        self.gridLayout_54 = QtWidgets.QGridLayout()
        self.gridLayout_54.setObjectName("gridLayout_54")
        spacerItem111 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem111, 1, 1, 1, 1)
        spacerItem112 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem112, 1, 2, 1, 1)
        self.CardWidget_293 = CardWidget(self.layoutWidget1)
        self.CardWidget_293.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_293.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_293.setObjectName("CardWidget_293")
        self.green_terracotta = CheckBox(self.CardWidget_293)
        self.green_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.green_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.green_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.green_terracotta.setFont(font)
        self.green_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon79 = QtGui.QIcon()
        icon79.addPixmap(QtGui.QPixmap("icon/green_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_terracotta.setIcon(icon79)
        self.green_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.green_terracotta.setChecked(True)
        self.green_terracotta.setTristate(False)
        self.green_terracotta.setObjectName("green_terracotta")
        self.gridLayout_54.addWidget(self.CardWidget_293, 1, 0, 1, 1)
        spacerItem113 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_54.addItem(spacerItem113, 2, 1, 1, 1)
        spacerItem114 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_54.addItem(spacerItem114, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_54, 99, 3, 1, 1)
        self.VerticalSeparator_46 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_46.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_46.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_46.setObjectName("VerticalSeparator_46")
        self.gridLayout_15.addWidget(self.VerticalSeparator_46, 33, 2, 1, 1)
        self.HorizontalSeparator_25 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_25.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_25.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_25.setObjectName("HorizontalSeparator_25")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_25, 26, 1, 1, 1)
        self.HorizontalSeparator_21 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_21.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_21.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_21.setObjectName("HorizontalSeparator_21")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_21, 22, 1, 1, 1)
        self.CardWidget_74 = CardWidget(self.layoutWidget1)
        self.CardWidget_74.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_74.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_74.setObjectName("CardWidget_74")
        self.layoutWidget_142 = QtWidgets.QWidget(self.CardWidget_74)
        self.layoutWidget_142.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_142.setObjectName("layoutWidget_142")
        self.horizontalLayout_151 = QtWidgets.QHBoxLayout(self.layoutWidget_142)
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_151.setObjectName("horizontalLayout_151")
        self.PixmapLabel_80 = PixmapLabel(self.layoutWidget_142)
        self.PixmapLabel_80.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_80.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_80.setObjectName("PixmapLabel_80")
        self.horizontalLayout_151.addWidget(self.PixmapLabel_80)
        self.CheckBox_B61 = CheckBox(self.layoutWidget_142)
        self.CheckBox_B61.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B61.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B61.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B61.setChecked(True)
        self.CheckBox_B61.setObjectName("CheckBox_B61")
        self.horizontalLayout_151.addWidget(self.CheckBox_B61)
        self.gridLayout_15.addWidget(self.CardWidget_74, 123, 1, 1, 1)
        self.HorizontalSeparator_24 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_24.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_24.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_24.setObjectName("HorizontalSeparator_24")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_24, 24, 3, 1, 1)
        self.HorizontalSeparator_121 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_121.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_121.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_121.setObjectName("HorizontalSeparator_121")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_121, 122, 1, 1, 1)
        self.HorizontalSeparator_10 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_10.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_10.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_10.setObjectName("HorizontalSeparator_10")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_10, 10, 3, 1, 1)
        self.HorizontalSeparator_86 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_86.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_86.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_86.setObjectName("HorizontalSeparator_86")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_86, 88, 1, 1, 1)
        self.CardWidget_15 = CardWidget(self.layoutWidget1)
        self.CardWidget_15.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_15.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_15.setObjectName("CardWidget_15")
        self.layoutWidget_29 = QtWidgets.QWidget(self.CardWidget_15)
        self.layoutWidget_29.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_29.setObjectName("layoutWidget_29")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.layoutWidget_29)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.PixmapLabel_21 = PixmapLabel(self.layoutWidget_29)
        self.PixmapLabel_21.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_21.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_21.setObjectName("PixmapLabel_21")
        self.horizontalLayout_33.addWidget(self.PixmapLabel_21)
        self.CheckBox_B7 = CheckBox(self.layoutWidget_29)
        self.CheckBox_B7.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B7.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B7.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B7.setChecked(True)
        self.CheckBox_B7.setObjectName("CheckBox_B7")
        self.horizontalLayout_33.addWidget(self.CheckBox_B7)
        self.gridLayout_15.addWidget(self.CardWidget_15, 15, 1, 1, 1)
        self.VerticalSeparator_29 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_29.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_29.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_29.setObjectName("VerticalSeparator_29")
        self.gridLayout_15.addWidget(self.VerticalSeparator_29, 67, 2, 1, 1)
        self.HorizontalSeparator_31 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_31.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_31.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_31.setObjectName("HorizontalSeparator_31")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_31, 32, 1, 1, 1)
        self.gridLayout_62 = QtWidgets.QGridLayout()
        self.gridLayout_62.setObjectName("gridLayout_62")
        spacerItem115 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_62.addItem(spacerItem115, 1, 1, 1, 1)
        spacerItem116 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_62.addItem(spacerItem116, 1, 2, 1, 1)
        self.CardWidget_303 = CardWidget(self.layoutWidget1)
        self.CardWidget_303.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_303.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_303.setObjectName("CardWidget_303")
        self.stripped_warped_hyphae = CheckBox(self.CardWidget_303)
        self.stripped_warped_hyphae.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.stripped_warped_hyphae.setMinimumSize(QtCore.QSize(17, 16))
        self.stripped_warped_hyphae.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stripped_warped_hyphae.setFont(font)
        self.stripped_warped_hyphae.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon80 = QtGui.QIcon()
        icon80.addPixmap(QtGui.QPixmap("icon/stripped_warped_hyphae.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stripped_warped_hyphae.setIcon(icon80)
        self.stripped_warped_hyphae.setIconSize(QtCore.QSize(16, 16))
        self.stripped_warped_hyphae.setChecked(True)
        self.stripped_warped_hyphae.setTristate(False)
        self.stripped_warped_hyphae.setObjectName("stripped_warped_hyphae")
        self.gridLayout_62.addWidget(self.CardWidget_303, 1, 0, 1, 1)
        spacerItem117 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_62.addItem(spacerItem117, 2, 1, 1, 1)
        spacerItem118 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_62.addItem(spacerItem118, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_62, 115, 3, 1, 1)
        self.HorizontalSeparator_11 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_11.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_11.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_11.setObjectName("HorizontalSeparator_11")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_11, 12, 1, 1, 1)
        self.gridLayout_53 = QtWidgets.QGridLayout()
        self.gridLayout_53.setObjectName("gridLayout_53")
        spacerItem119 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_53.addItem(spacerItem119, 1, 1, 1, 1)
        spacerItem120 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_53.addItem(spacerItem120, 1, 2, 1, 1)
        self.CardWidget_292 = CardWidget(self.layoutWidget1)
        self.CardWidget_292.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_292.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_292.setObjectName("CardWidget_292")
        self.brown_terracotta = CheckBox(self.CardWidget_292)
        self.brown_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.brown_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.brown_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.brown_terracotta.setFont(font)
        self.brown_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon81 = QtGui.QIcon()
        icon81.addPixmap(QtGui.QPixmap("icon/brown_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brown_terracotta.setIcon(icon81)
        self.brown_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.brown_terracotta.setChecked(True)
        self.brown_terracotta.setTristate(False)
        self.brown_terracotta.setObjectName("brown_terracotta")
        self.gridLayout_53.addWidget(self.CardWidget_292, 1, 0, 1, 1)
        spacerItem121 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_53.addItem(spacerItem121, 2, 1, 1, 1)
        spacerItem122 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_53.addItem(spacerItem122, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_53, 97, 3, 1, 1)
        self.CardWidget_71 = CardWidget(self.layoutWidget1)
        self.CardWidget_71.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_71.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_71.setObjectName("CardWidget_71")
        self.layoutWidget_136 = QtWidgets.QWidget(self.CardWidget_71)
        self.layoutWidget_136.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_136.setObjectName("layoutWidget_136")
        self.horizontalLayout_145 = QtWidgets.QHBoxLayout(self.layoutWidget_136)
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_145.setObjectName("horizontalLayout_145")
        self.PixmapLabel_77 = PixmapLabel(self.layoutWidget_136)
        self.PixmapLabel_77.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_77.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_77.setObjectName("PixmapLabel_77")
        self.horizontalLayout_145.addWidget(self.PixmapLabel_77)
        self.CheckBox_B58 = CheckBox(self.layoutWidget_136)
        self.CheckBox_B58.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B58.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B58.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B58.setChecked(True)
        self.CheckBox_B58.setObjectName("CheckBox_B58")
        self.horizontalLayout_145.addWidget(self.CheckBox_B58)
        self.gridLayout_15.addWidget(self.CardWidget_71, 117, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CardWidget_211 = CardWidget(self.layoutWidget1)
        self.CardWidget_211.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_211.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_211.setObjectName("CardWidget_211")
        self.magenta_concrete = CheckBox(self.CardWidget_211)
        self.magenta_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.magenta_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.magenta_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.magenta_concrete.setFont(font)
        self.magenta_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon82 = QtGui.QIcon()
        icon82.addPixmap(QtGui.QPixmap("icon/magenta_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.magenta_concrete.setIcon(icon82)
        self.magenta_concrete.setIconSize(QtCore.QSize(16, 16))
        self.magenta_concrete.setChecked(True)
        self.magenta_concrete.setTristate(False)
        self.magenta_concrete.setObjectName("magenta_concrete")
        self.gridLayout_4.addWidget(self.CardWidget_211, 1, 0, 1, 1)
        self.CardWidget_213 = CardWidget(self.layoutWidget1)
        self.CardWidget_213.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_213.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_213.setObjectName("CardWidget_213")
        self.magenta_stained_glass = CheckBox(self.CardWidget_213)
        self.magenta_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.magenta_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.magenta_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.magenta_stained_glass.setFont(font)
        self.magenta_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon83 = QtGui.QIcon()
        icon83.addPixmap(QtGui.QPixmap("icon/magenta_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.magenta_stained_glass.setIcon(icon83)
        self.magenta_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.magenta_stained_glass.setTristate(False)
        self.magenta_stained_glass.setObjectName("magenta_stained_glass")
        self.gridLayout_4.addWidget(self.CardWidget_213, 1, 2, 1, 1)
        self.CardWidget_214 = CardWidget(self.layoutWidget1)
        self.CardWidget_214.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_214.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_214.setObjectName("CardWidget_214")
        self.purpur_block = CheckBox(self.CardWidget_214)
        self.purpur_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.purpur_block.setMinimumSize(QtCore.QSize(17, 16))
        self.purpur_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.purpur_block.setFont(font)
        self.purpur_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon84 = QtGui.QIcon()
        icon84.addPixmap(QtGui.QPixmap("icon/purpur_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.purpur_block.setIcon(icon84)
        self.purpur_block.setIconSize(QtCore.QSize(16, 16))
        self.purpur_block.setTristate(False)
        self.purpur_block.setObjectName("purpur_block")
        self.gridLayout_4.addWidget(self.CardWidget_214, 3, 0, 1, 1)
        spacerItem123 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem123, 4, 1, 1, 1)
        self.CardWidget_215 = CardWidget(self.layoutWidget1)
        self.CardWidget_215.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_215.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_215.setObjectName("CardWidget_215")
        self.magenta_wool = CheckBox(self.CardWidget_215)
        self.magenta_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.magenta_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.magenta_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.magenta_wool.setFont(font)
        self.magenta_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon85 = QtGui.QIcon()
        icon85.addPixmap(QtGui.QPixmap("icon/magenta_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.magenta_wool.setIcon(icon85)
        self.magenta_wool.setIconSize(QtCore.QSize(16, 16))
        self.magenta_wool.setTristate(False)
        self.magenta_wool.setObjectName("magenta_wool")
        self.gridLayout_4.addWidget(self.CardWidget_215, 1, 1, 1, 1)
        spacerItem124 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem124, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_4, 33, 3, 1, 1)
        self.gridLayout_46 = QtWidgets.QGridLayout()
        self.gridLayout_46.setObjectName("gridLayout_46")
        spacerItem125 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_46.addItem(spacerItem125, 1, 1, 1, 1)
        spacerItem126 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_46.addItem(spacerItem126, 1, 2, 1, 1)
        self.CardWidget_281 = CardWidget(self.layoutWidget1)
        self.CardWidget_281.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_281.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_281.setObjectName("CardWidget_281")
        self.lime_terracotta = CheckBox(self.CardWidget_281)
        self.lime_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.lime_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.lime_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lime_terracotta.setFont(font)
        self.lime_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon86 = QtGui.QIcon()
        icon86.addPixmap(QtGui.QPixmap("icon/lime_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lime_terracotta.setIcon(icon86)
        self.lime_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.lime_terracotta.setChecked(True)
        self.lime_terracotta.setTristate(False)
        self.lime_terracotta.setObjectName("lime_terracotta")
        self.gridLayout_46.addWidget(self.CardWidget_281, 1, 0, 1, 1)
        spacerItem127 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_46.addItem(spacerItem127, 2, 1, 1, 1)
        spacerItem128 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_46.addItem(spacerItem128, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_46, 83, 3, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        spacerItem129 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem129, 1, 1, 1, 1)
        spacerItem130 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem130, 1, 2, 1, 1)
        self.CardWidget_188 = CardWidget(self.layoutWidget1)
        self.CardWidget_188.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_188.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_188.setObjectName("CardWidget_188")
        self.water = CheckBox(self.CardWidget_188)
        self.water.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.water.setMinimumSize(QtCore.QSize(17, 16))
        self.water.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.water.setFont(font)
        self.water.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon87 = QtGui.QIcon()
        icon87.addPixmap(QtGui.QPixmap("icon/water.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.water.setIcon(icon87)
        self.water.setIconSize(QtCore.QSize(16, 16))
        self.water.setChecked(True)
        self.water.setTristate(False)
        self.water.setObjectName("water")
        self.gridLayout_23.addWidget(self.CardWidget_188, 1, 0, 1, 1)
        spacerItem131 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem131, 2, 1, 1, 1)
        spacerItem132 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem132, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_23, 25, 3, 1, 1)
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        spacerItem133 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_35.addItem(spacerItem133, 0, 1, 1, 1)
        self.CardWidget_255 = CardWidget(self.layoutWidget1)
        self.CardWidget_255.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_255.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_255.setObjectName("CardWidget_255")
        self.black_concrete = CheckBox(self.CardWidget_255)
        self.black_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.black_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.black_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.black_concrete.setFont(font)
        self.black_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon88 = QtGui.QIcon()
        icon88.addPixmap(QtGui.QPixmap("icon/black_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.black_concrete.setIcon(icon88)
        self.black_concrete.setIconSize(QtCore.QSize(16, 16))
        self.black_concrete.setChecked(True)
        self.black_concrete.setTristate(False)
        self.black_concrete.setObjectName("black_concrete")
        self.gridLayout_35.addWidget(self.CardWidget_255, 1, 0, 1, 1)
        self.CardWidget_266 = CardWidget(self.layoutWidget1)
        self.CardWidget_266.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_266.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_266.setObjectName("CardWidget_266")
        self.black_wool = CheckBox(self.CardWidget_266)
        self.black_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.black_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.black_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.black_wool.setFont(font)
        self.black_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon89 = QtGui.QIcon()
        icon89.addPixmap(QtGui.QPixmap("icon/black_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.black_wool.setIcon(icon89)
        self.black_wool.setIconSize(QtCore.QSize(16, 16))
        self.black_wool.setTristate(False)
        self.black_wool.setObjectName("black_wool")
        self.gridLayout_35.addWidget(self.CardWidget_266, 1, 1, 1, 1)
        self.CardWidget_267 = CardWidget(self.layoutWidget1)
        self.CardWidget_267.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_267.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_267.setObjectName("CardWidget_267")
        self.black_stained_glass = CheckBox(self.CardWidget_267)
        self.black_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.black_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.black_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.black_stained_glass.setFont(font)
        self.black_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon90 = QtGui.QIcon()
        icon90.addPixmap(QtGui.QPixmap("icon/black_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.black_stained_glass.setIcon(icon90)
        self.black_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.black_stained_glass.setTristate(False)
        self.black_stained_glass.setObjectName("black_stained_glass")
        self.gridLayout_35.addWidget(self.CardWidget_267, 1, 2, 1, 1)
        self.CardWidget_268 = CardWidget(self.layoutWidget1)
        self.CardWidget_268.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_268.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_268.setObjectName("CardWidget_268")
        self.obsidian = CheckBox(self.CardWidget_268)
        self.obsidian.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.obsidian.setMinimumSize(QtCore.QSize(17, 16))
        self.obsidian.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.obsidian.setFont(font)
        self.obsidian.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon91 = QtGui.QIcon()
        icon91.addPixmap(QtGui.QPixmap("icon/obsidian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.obsidian.setIcon(icon91)
        self.obsidian.setIconSize(QtCore.QSize(16, 16))
        self.obsidian.setTristate(False)
        self.obsidian.setObjectName("obsidian")
        self.gridLayout_35.addWidget(self.CardWidget_268, 2, 0, 1, 1)
        self.CardWidget_269 = CardWidget(self.layoutWidget1)
        self.CardWidget_269.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_269.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_269.setObjectName("CardWidget_269")
        self.coal_block = CheckBox(self.CardWidget_269)
        self.coal_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.coal_block.setMinimumSize(QtCore.QSize(17, 16))
        self.coal_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.coal_block.setFont(font)
        self.coal_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon92 = QtGui.QIcon()
        icon92.addPixmap(QtGui.QPixmap("icon/coal_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.coal_block.setIcon(icon92)
        self.coal_block.setIconSize(QtCore.QSize(16, 16))
        self.coal_block.setTristate(False)
        self.coal_block.setObjectName("coal_block")
        self.gridLayout_35.addWidget(self.CardWidget_269, 2, 1, 1, 1)
        self.CardWidget_270 = CardWidget(self.layoutWidget1)
        self.CardWidget_270.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_270.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_270.setObjectName("CardWidget_270")
        self.polished_basalt = CheckBox(self.CardWidget_270)
        self.polished_basalt.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.polished_basalt.setMinimumSize(QtCore.QSize(17, 16))
        self.polished_basalt.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.polished_basalt.setFont(font)
        self.polished_basalt.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon93 = QtGui.QIcon()
        icon93.addPixmap(QtGui.QPixmap("icon/polished_basalt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polished_basalt.setIcon(icon93)
        self.polished_basalt.setIconSize(QtCore.QSize(16, 16))
        self.polished_basalt.setTristate(False)
        self.polished_basalt.setObjectName("polished_basalt")
        self.gridLayout_35.addWidget(self.CardWidget_270, 2, 2, 1, 1)
        self.CardWidget_271 = CardWidget(self.layoutWidget1)
        self.CardWidget_271.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_271.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_271.setObjectName("CardWidget_271")
        self.polished_blackstone = CheckBox(self.CardWidget_271)
        self.polished_blackstone.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.polished_blackstone.setMinimumSize(QtCore.QSize(17, 16))
        self.polished_blackstone.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.polished_blackstone.setFont(font)
        self.polished_blackstone.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon94 = QtGui.QIcon()
        icon94.addPixmap(QtGui.QPixmap("icon/polished_blackstone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polished_blackstone.setIcon(icon94)
        self.polished_blackstone.setIconSize(QtCore.QSize(16, 16))
        self.polished_blackstone.setTristate(False)
        self.polished_blackstone.setObjectName("polished_blackstone")
        self.gridLayout_35.addWidget(self.CardWidget_271, 3, 0, 1, 1)
        self.CardWidget_272 = CardWidget(self.layoutWidget1)
        self.CardWidget_272.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_272.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_272.setObjectName("CardWidget_272")
        self.sculk = CheckBox(self.CardWidget_272)
        self.sculk.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.sculk.setMinimumSize(QtCore.QSize(17, 16))
        self.sculk.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sculk.setFont(font)
        self.sculk.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon95 = QtGui.QIcon()
        icon95.addPixmap(QtGui.QPixmap("icon/sculk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sculk.setIcon(icon95)
        self.sculk.setIconSize(QtCore.QSize(16, 16))
        self.sculk.setTristate(False)
        self.sculk.setObjectName("sculk")
        self.gridLayout_35.addWidget(self.CardWidget_272, 3, 1, 1, 1)
        spacerItem134 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_35.addItem(spacerItem134, 4, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_35, 59, 3, 1, 1)
        self.HorizontalSeparator_95 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_95.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_95.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_95.setObjectName("HorizontalSeparator_95")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_95, 96, 3, 1, 1)
        self.VerticalSeparator_17 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_17.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_17.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_17.setObjectName("VerticalSeparator_17")
        self.gridLayout_15.addWidget(self.VerticalSeparator_17, 91, 2, 1, 1)
        self.gridLayout_34 = QtWidgets.QGridLayout()
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.CardWidget_265 = CardWidget(self.layoutWidget1)
        self.CardWidget_265.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_265.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_265.setObjectName("CardWidget_265")
        self.waxed_copper_block = CheckBox(self.CardWidget_265)
        self.waxed_copper_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.waxed_copper_block.setMinimumSize(QtCore.QSize(17, 16))
        self.waxed_copper_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.waxed_copper_block.setFont(font)
        self.waxed_copper_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon96 = QtGui.QIcon()
        icon96.addPixmap(QtGui.QPixmap("icon/waxed_copper_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.waxed_copper_block.setIcon(icon96)
        self.waxed_copper_block.setIconSize(QtCore.QSize(16, 16))
        self.waxed_copper_block.setTristate(False)
        self.waxed_copper_block.setObjectName("waxed_copper_block")
        self.gridLayout_34.addWidget(self.CardWidget_265, 3, 2, 1, 1)
        self.CardWidget_263 = CardWidget(self.layoutWidget1)
        self.CardWidget_263.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_263.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_263.setObjectName("CardWidget_263")
        self.smooth_red_sandstone = CheckBox(self.CardWidget_263)
        self.smooth_red_sandstone.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.smooth_red_sandstone.setMinimumSize(QtCore.QSize(17, 16))
        self.smooth_red_sandstone.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.smooth_red_sandstone.setFont(font)
        self.smooth_red_sandstone.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon97 = QtGui.QIcon()
        icon97.addPixmap(QtGui.QPixmap("icon/smooth_red_sandstone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smooth_red_sandstone.setIcon(icon97)
        self.smooth_red_sandstone.setIconSize(QtCore.QSize(16, 16))
        self.smooth_red_sandstone.setTristate(False)
        self.smooth_red_sandstone.setObjectName("smooth_red_sandstone")
        self.gridLayout_34.addWidget(self.CardWidget_263, 3, 0, 1, 1)
        self.CardWidget_258 = CardWidget(self.layoutWidget1)
        self.CardWidget_258.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_258.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_258.setObjectName("CardWidget_258")
        self.orange_wool = CheckBox(self.CardWidget_258)
        self.orange_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.orange_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.orange_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.orange_wool.setFont(font)
        self.orange_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon98 = QtGui.QIcon()
        icon98.addPixmap(QtGui.QPixmap("icon/orange_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.orange_wool.setIcon(icon98)
        self.orange_wool.setIconSize(QtCore.QSize(16, 16))
        self.orange_wool.setTristate(False)
        self.orange_wool.setObjectName("orange_wool")
        self.gridLayout_34.addWidget(self.CardWidget_258, 1, 1, 1, 1)
        self.CardWidget_260 = CardWidget(self.layoutWidget1)
        self.CardWidget_260.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_260.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_260.setObjectName("CardWidget_260")
        self.acacia_planks = CheckBox(self.CardWidget_260)
        self.acacia_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.acacia_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.acacia_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.acacia_planks.setFont(font)
        self.acacia_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon99 = QtGui.QIcon()
        icon99.addPixmap(QtGui.QPixmap("icon/acacia_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acacia_planks.setIcon(icon99)
        self.acacia_planks.setIconSize(QtCore.QSize(16, 16))
        self.acacia_planks.setTristate(False)
        self.acacia_planks.setObjectName("acacia_planks")
        self.gridLayout_34.addWidget(self.CardWidget_260, 2, 0, 1, 1)
        self.CardWidget_262 = CardWidget(self.layoutWidget1)
        self.CardWidget_262.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_262.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_262.setObjectName("CardWidget_262")
        self.terracotta = CheckBox(self.CardWidget_262)
        self.terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.terracotta.setFont(font)
        self.terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon100 = QtGui.QIcon()
        icon100.addPixmap(QtGui.QPixmap("icon/terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.terracotta.setIcon(icon100)
        self.terracotta.setIconSize(QtCore.QSize(16, 16))
        self.terracotta.setTristate(False)
        self.terracotta.setObjectName("terracotta")
        self.gridLayout_34.addWidget(self.CardWidget_262, 2, 2, 1, 1)
        self.CardWidget_259 = CardWidget(self.layoutWidget1)
        self.CardWidget_259.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_259.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_259.setObjectName("CardWidget_259")
        self.orange_stained_glass = CheckBox(self.CardWidget_259)
        self.orange_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.orange_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.orange_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.orange_stained_glass.setFont(font)
        self.orange_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon101 = QtGui.QIcon()
        icon101.addPixmap(QtGui.QPixmap("icon/orange_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.orange_stained_glass.setIcon(icon101)
        self.orange_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.orange_stained_glass.setTristate(False)
        self.orange_stained_glass.setObjectName("orange_stained_glass")
        self.gridLayout_34.addWidget(self.CardWidget_259, 1, 2, 1, 1)
        self.CardWidget_264 = CardWidget(self.layoutWidget1)
        self.CardWidget_264.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_264.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_264.setObjectName("CardWidget_264")
        self.honeycomb_block = CheckBox(self.CardWidget_264)
        self.honeycomb_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.honeycomb_block.setMinimumSize(QtCore.QSize(17, 16))
        self.honeycomb_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.honeycomb_block.setFont(font)
        self.honeycomb_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon102 = QtGui.QIcon()
        icon102.addPixmap(QtGui.QPixmap("icon/honeycomb_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.honeycomb_block.setIcon(icon102)
        self.honeycomb_block.setIconSize(QtCore.QSize(16, 16))
        self.honeycomb_block.setTristate(False)
        self.honeycomb_block.setObjectName("honeycomb_block")
        self.gridLayout_34.addWidget(self.CardWidget_264, 3, 1, 1, 1)
        spacerItem135 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_34.addItem(spacerItem135, 0, 1, 1, 1)
        spacerItem136 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_34.addItem(spacerItem136, 4, 1, 1, 1)
        self.CardWidget_257 = CardWidget(self.layoutWidget1)
        self.CardWidget_257.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_257.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_257.setObjectName("CardWidget_257")
        self.orange_concrete = CheckBox(self.CardWidget_257)
        self.orange_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.orange_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.orange_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.orange_concrete.setFont(font)
        self.orange_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon103 = QtGui.QIcon()
        icon103.addPixmap(QtGui.QPixmap("icon/orange_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.orange_concrete.setIcon(icon103)
        self.orange_concrete.setIconSize(QtCore.QSize(16, 16))
        self.orange_concrete.setChecked(True)
        self.orange_concrete.setTristate(False)
        self.orange_concrete.setObjectName("orange_concrete")
        self.gridLayout_34.addWidget(self.CardWidget_257, 1, 0, 1, 1)
        self.CardWidget_261 = CardWidget(self.layoutWidget1)
        self.CardWidget_261.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_261.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_261.setObjectName("CardWidget_261")
        self.pumpkin = CheckBox(self.CardWidget_261)
        self.pumpkin.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.pumpkin.setMinimumSize(QtCore.QSize(17, 16))
        self.pumpkin.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pumpkin.setFont(font)
        self.pumpkin.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon104 = QtGui.QIcon()
        icon104.addPixmap(QtGui.QPixmap("icon/pumpkin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pumpkin.setIcon(icon104)
        self.pumpkin.setIconSize(QtCore.QSize(16, 16))
        self.pumpkin.setTristate(False)
        self.pumpkin.setObjectName("pumpkin")
        self.gridLayout_34.addWidget(self.CardWidget_261, 2, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_34, 31, 3, 1, 1)
        self.CardWidget_62 = CardWidget(self.layoutWidget1)
        self.CardWidget_62.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_62.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_62.setObjectName("CardWidget_62")
        self.layoutWidget_119 = QtWidgets.QWidget(self.CardWidget_62)
        self.layoutWidget_119.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_119.setObjectName("layoutWidget_119")
        self.horizontalLayout_127 = QtWidgets.QHBoxLayout(self.layoutWidget_119)
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_127.setObjectName("horizontalLayout_127")
        self.PixmapLabel_68 = PixmapLabel(self.layoutWidget_119)
        self.PixmapLabel_68.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_68.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_68.setObjectName("PixmapLabel_68")
        self.horizontalLayout_127.addWidget(self.PixmapLabel_68)
        self.CheckBox_B50 = CheckBox(self.layoutWidget_119)
        self.CheckBox_B50.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B50.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B50.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B50.setChecked(True)
        self.CheckBox_B50.setObjectName("CheckBox_B50")
        self.horizontalLayout_127.addWidget(self.CheckBox_B50)
        self.gridLayout_15.addWidget(self.CardWidget_62, 101, 1, 1, 1)
        self.CardWidget_21 = CardWidget(self.layoutWidget1)
        self.CardWidget_21.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_21.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_21.setObjectName("CardWidget_21")
        self.layoutWidget_36 = QtWidgets.QWidget(self.CardWidget_21)
        self.layoutWidget_36.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_36.setObjectName("layoutWidget_36")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.layoutWidget_36)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.PixmapLabel_27 = PixmapLabel(self.layoutWidget_36)
        self.PixmapLabel_27.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_27.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_27.setObjectName("PixmapLabel_27")
        self.horizontalLayout_45.addWidget(self.PixmapLabel_27)
        self.CheckBox_B9 = CheckBox(self.layoutWidget_36)
        self.CheckBox_B9.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B9.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B9.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B9.setChecked(True)
        self.CheckBox_B9.setObjectName("CheckBox_B9")
        self.horizontalLayout_45.addWidget(self.CheckBox_B9)
        self.gridLayout_15.addWidget(self.CardWidget_21, 19, 1, 1, 1)
        self.CardWidget_72 = CardWidget(self.layoutWidget1)
        self.CardWidget_72.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_72.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_72.setObjectName("CardWidget_72")
        self.layoutWidget_138 = QtWidgets.QWidget(self.CardWidget_72)
        self.layoutWidget_138.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_138.setObjectName("layoutWidget_138")
        self.horizontalLayout_147 = QtWidgets.QHBoxLayout(self.layoutWidget_138)
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_147.setObjectName("horizontalLayout_147")
        self.PixmapLabel_78 = PixmapLabel(self.layoutWidget_138)
        self.PixmapLabel_78.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_78.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_78.setObjectName("PixmapLabel_78")
        self.horizontalLayout_147.addWidget(self.PixmapLabel_78)
        self.CheckBox_B59 = CheckBox(self.layoutWidget_138)
        self.CheckBox_B59.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B59.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B59.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B59.setChecked(True)
        self.CheckBox_B59.setObjectName("CheckBox_B59")
        self.horizontalLayout_147.addWidget(self.CheckBox_B59)
        self.gridLayout_15.addWidget(self.CardWidget_72, 119, 1, 1, 1)
        self.HorizontalSeparator_39 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_39.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_39.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_39.setObjectName("HorizontalSeparator_39")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_39, 40, 1, 1, 1)
        self.gridLayout_61 = QtWidgets.QGridLayout()
        self.gridLayout_61.setObjectName("gridLayout_61")
        spacerItem137 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_61.addItem(spacerItem137, 1, 2, 1, 1)
        self.CardWidget_301 = CardWidget(self.layoutWidget1)
        self.CardWidget_301.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_301.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_301.setObjectName("CardWidget_301")
        self.waxed_weathered_copper = CheckBox(self.CardWidget_301)
        self.waxed_weathered_copper.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.waxed_weathered_copper.setMinimumSize(QtCore.QSize(17, 16))
        self.waxed_weathered_copper.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.waxed_weathered_copper.setFont(font)
        self.waxed_weathered_copper.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon105 = QtGui.QIcon()
        icon105.addPixmap(QtGui.QPixmap("icon/waxed_weathered_copper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.waxed_weathered_copper.setIcon(icon105)
        self.waxed_weathered_copper.setIconSize(QtCore.QSize(16, 16))
        self.waxed_weathered_copper.setTristate(False)
        self.waxed_weathered_copper.setObjectName("waxed_weathered_copper")
        self.gridLayout_61.addWidget(self.CardWidget_301, 1, 1, 1, 1)
        spacerItem138 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_61.addItem(spacerItem138, 2, 1, 1, 1)
        spacerItem139 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_61.addItem(spacerItem139, 0, 1, 1, 1)
        self.CardWidget_302 = CardWidget(self.layoutWidget1)
        self.CardWidget_302.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_302.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_302.setObjectName("CardWidget_302")
        self.stripped_warped_stem = CheckBox(self.CardWidget_302)
        self.stripped_warped_stem.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.stripped_warped_stem.setMinimumSize(QtCore.QSize(17, 16))
        self.stripped_warped_stem.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stripped_warped_stem.setFont(font)
        self.stripped_warped_stem.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon106 = QtGui.QIcon()
        icon106.addPixmap(QtGui.QPixmap("icon/stripped_warped_stem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stripped_warped_stem.setIcon(icon106)
        self.stripped_warped_stem.setIconSize(QtCore.QSize(16, 16))
        self.stripped_warped_stem.setChecked(True)
        self.stripped_warped_stem.setTristate(False)
        self.stripped_warped_stem.setObjectName("stripped_warped_stem")
        self.gridLayout_61.addWidget(self.CardWidget_302, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_61, 113, 3, 1, 1)
        self.CardWidget_29 = CardWidget(self.layoutWidget1)
        self.CardWidget_29.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_29.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_29.setObjectName("CardWidget_29")
        self.layoutWidget_53 = QtWidgets.QWidget(self.CardWidget_29)
        self.layoutWidget_53.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_53.setObjectName("layoutWidget_53")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.layoutWidget_53)
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.PixmapLabel_35 = PixmapLabel(self.layoutWidget_53)
        self.PixmapLabel_35.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_35.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_35.setObjectName("PixmapLabel_35")
        self.horizontalLayout_61.addWidget(self.PixmapLabel_35)
        self.CheckBox_B17 = CheckBox(self.layoutWidget_53)
        self.CheckBox_B17.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B17.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B17.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B17.setChecked(True)
        self.CheckBox_B17.setObjectName("CheckBox_B17")
        self.horizontalLayout_61.addWidget(self.CheckBox_B17)
        self.gridLayout_15.addWidget(self.CardWidget_29, 35, 1, 1, 1)
        self.VerticalSeparator_16 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_16.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_16.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_16.setObjectName("VerticalSeparator_16")
        self.gridLayout_15.addWidget(self.VerticalSeparator_16, 93, 2, 1, 1)
        self.VerticalSeparator_45 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_45.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_45.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_45.setObjectName("VerticalSeparator_45")
        self.gridLayout_15.addWidget(self.VerticalSeparator_45, 35, 2, 1, 1)
        self.HorizontalSeparator_56 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_56.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_56.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_56.setObjectName("HorizontalSeparator_56")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_56, 58, 1, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.CardWidget_226 = CardWidget(self.layoutWidget1)
        self.CardWidget_226.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_226.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_226.setObjectName("CardWidget_226")
        self.gray_concrete = CheckBox(self.CardWidget_226)
        self.gray_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.gray_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.gray_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gray_concrete.setFont(font)
        self.gray_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon107 = QtGui.QIcon()
        icon107.addPixmap(QtGui.QPixmap("icon/gray_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gray_concrete.setIcon(icon107)
        self.gray_concrete.setIconSize(QtCore.QSize(16, 16))
        self.gray_concrete.setChecked(True)
        self.gray_concrete.setTristate(False)
        self.gray_concrete.setObjectName("gray_concrete")
        self.gridLayout_8.addWidget(self.CardWidget_226, 1, 0, 1, 1)
        self.CardWidget_227 = CardWidget(self.layoutWidget1)
        self.CardWidget_227.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_227.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_227.setObjectName("CardWidget_227")
        self.gray_stained_glass = CheckBox(self.CardWidget_227)
        self.gray_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.gray_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.gray_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gray_stained_glass.setFont(font)
        self.gray_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon108 = QtGui.QIcon()
        icon108.addPixmap(QtGui.QPixmap("icon/gray_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gray_stained_glass.setIcon(icon108)
        self.gray_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.gray_stained_glass.setTristate(False)
        self.gray_stained_glass.setObjectName("gray_stained_glass")
        self.gridLayout_8.addWidget(self.CardWidget_227, 1, 2, 1, 1)
        self.CardWidget_228 = CardWidget(self.layoutWidget1)
        self.CardWidget_228.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_228.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_228.setObjectName("CardWidget_228")
        self.tinted_glass = CheckBox(self.CardWidget_228)
        self.tinted_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.tinted_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.tinted_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tinted_glass.setFont(font)
        self.tinted_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon109 = QtGui.QIcon()
        icon109.addPixmap(QtGui.QPixmap("icon/tinted_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tinted_glass.setIcon(icon109)
        self.tinted_glass.setIconSize(QtCore.QSize(16, 16))
        self.tinted_glass.setTristate(False)
        self.tinted_glass.setObjectName("tinted_glass")
        self.gridLayout_8.addWidget(self.CardWidget_228, 3, 0, 1, 1)
        spacerItem140 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem140, 4, 1, 1, 1)
        self.CardWidget_229 = CardWidget(self.layoutWidget1)
        self.CardWidget_229.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_229.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_229.setObjectName("CardWidget_229")
        self.gray_wool = CheckBox(self.CardWidget_229)
        self.gray_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.gray_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.gray_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gray_wool.setFont(font)
        self.gray_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon110 = QtGui.QIcon()
        icon110.addPixmap(QtGui.QPixmap("icon/gray_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gray_wool.setIcon(icon110)
        self.gray_wool.setIconSize(QtCore.QSize(16, 16))
        self.gray_wool.setTristate(False)
        self.gray_wool.setObjectName("gray_wool")
        self.gridLayout_8.addWidget(self.CardWidget_229, 1, 1, 1, 1)
        spacerItem141 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem141, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_8, 43, 3, 1, 1)
        self.VerticalSeparator_44 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_44.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_44.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_44.setObjectName("VerticalSeparator_44")
        self.gridLayout_15.addWidget(self.VerticalSeparator_44, 37, 2, 1, 1)
        self.HorizontalSeparator_29 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_29.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_29.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_29.setObjectName("HorizontalSeparator_29")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_29, 30, 1, 1, 1)
        self.CardWidget_58 = CardWidget(self.layoutWidget1)
        self.CardWidget_58.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_58.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_58.setObjectName("CardWidget_58")
        self.layoutWidget_111 = QtWidgets.QWidget(self.CardWidget_58)
        self.layoutWidget_111.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_111.setObjectName("layoutWidget_111")
        self.horizontalLayout_119 = QtWidgets.QHBoxLayout(self.layoutWidget_111)
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_119.setObjectName("horizontalLayout_119")
        self.PixmapLabel_64 = PixmapLabel(self.layoutWidget_111)
        self.PixmapLabel_64.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_64.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_64.setObjectName("PixmapLabel_64")
        self.horizontalLayout_119.addWidget(self.PixmapLabel_64)
        self.CheckBox_B46 = CheckBox(self.layoutWidget_111)
        self.CheckBox_B46.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B46.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B46.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B46.setChecked(True)
        self.CheckBox_B46.setObjectName("CheckBox_B46")
        self.horizontalLayout_119.addWidget(self.CheckBox_B46)
        self.gridLayout_15.addWidget(self.CardWidget_58, 93, 1, 1, 1)
        self.CardWidget_8 = CardWidget(self.layoutWidget1)
        self.CardWidget_8.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_8.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_8.setStyleSheet("background-color: transparent;")
        self.CardWidget_8.setObjectName("CardWidget_8")
        self.layoutWidget_15 = QtWidgets.QWidget(self.CardWidget_8)
        self.layoutWidget_15.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.PixmapLabel_14 = PixmapLabel(self.layoutWidget_15)
        self.PixmapLabel_14.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_14.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_14.setObjectName("PixmapLabel_14")
        self.horizontalLayout_19.addWidget(self.PixmapLabel_14)
        self.CheckBox_B0 = CheckBox(self.layoutWidget_15)
        self.CheckBox_B0.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B0.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B0.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B0.setChecked(True)
        self.CheckBox_B0.setTristate(False)
        self.CheckBox_B0.setObjectName("CheckBox_B0")
        self.horizontalLayout_19.addWidget(self.CheckBox_B0)
        self.gridLayout_15.addWidget(self.CardWidget_8, 1, 1, 1, 1)
        self.VerticalSeparator_53 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_53.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_53.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_53.setObjectName("VerticalSeparator_53")
        self.gridLayout_15.addWidget(self.VerticalSeparator_53, 19, 2, 1, 1)
        self.HorizontalSeparator_48 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_48.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_48.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_48.setObjectName("HorizontalSeparator_48")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_48, 48, 3, 1, 1)
        self.HorizontalSeparator_114 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_114.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_114.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_114.setObjectName("HorizontalSeparator_114")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_114, 116, 1, 1, 1)
        self.HorizontalSeparator_64 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_64.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_64.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_64.setObjectName("HorizontalSeparator_64")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_64, 66, 1, 1, 1)
        self.CardWidget_32 = CardWidget(self.layoutWidget1)
        self.CardWidget_32.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_32.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_32.setObjectName("CardWidget_32")
        self.layoutWidget_59 = QtWidgets.QWidget(self.CardWidget_32)
        self.layoutWidget_59.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_59.setObjectName("layoutWidget_59")
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout(self.layoutWidget_59)
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.PixmapLabel_38 = PixmapLabel(self.layoutWidget_59)
        self.PixmapLabel_38.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_38.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_38.setObjectName("PixmapLabel_38")
        self.horizontalLayout_67.addWidget(self.PixmapLabel_38)
        self.CheckBox_B20 = CheckBox(self.layoutWidget_59)
        self.CheckBox_B20.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B20.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B20.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B20.setChecked(True)
        self.CheckBox_B20.setObjectName("CheckBox_B20")
        self.horizontalLayout_67.addWidget(self.CheckBox_B20)
        self.gridLayout_15.addWidget(self.CardWidget_32, 41, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem142 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem142, 0, 1, 1, 1)
        self.CardWidget_161 = CardWidget(self.layoutWidget1)
        self.CardWidget_161.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_161.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_161.setObjectName("CardWidget_161")
        self.birch_planks = CheckBox(self.CardWidget_161)
        self.birch_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.birch_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.birch_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.birch_planks.setFont(font)
        self.birch_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon111 = QtGui.QIcon()
        icon111.addPixmap(QtGui.QPixmap("icon/birch_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.birch_planks.setIcon(icon111)
        self.birch_planks.setIconSize(QtCore.QSize(16, 16))
        self.birch_planks.setChecked(True)
        self.birch_planks.setTristate(False)
        self.birch_planks.setObjectName("birch_planks")
        self.gridLayout.addWidget(self.CardWidget_161, 1, 0, 1, 1)
        self.CardWidget_164 = CardWidget(self.layoutWidget1)
        self.CardWidget_164.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_164.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_164.setObjectName("CardWidget_164")
        self.smooth_sandstone = CheckBox(self.CardWidget_164)
        self.smooth_sandstone.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.smooth_sandstone.setMinimumSize(QtCore.QSize(17, 16))
        self.smooth_sandstone.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.smooth_sandstone.setFont(font)
        self.smooth_sandstone.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon112 = QtGui.QIcon()
        icon112.addPixmap(QtGui.QPixmap("icon/smooth_sandstone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smooth_sandstone.setIcon(icon112)
        self.smooth_sandstone.setIconSize(QtCore.QSize(16, 16))
        self.smooth_sandstone.setChecked(False)
        self.smooth_sandstone.setTristate(False)
        self.smooth_sandstone.setObjectName("smooth_sandstone")
        self.gridLayout.addWidget(self.CardWidget_164, 1, 1, 1, 1)
        self.CardWidget_160 = CardWidget(self.layoutWidget1)
        self.CardWidget_160.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_160.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_160.setObjectName("CardWidget_160")
        self.glowstone = CheckBox(self.CardWidget_160)
        self.glowstone.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.glowstone.setMinimumSize(QtCore.QSize(17, 16))
        self.glowstone.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.glowstone.setFont(font)
        self.glowstone.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon113 = QtGui.QIcon()
        icon113.addPixmap(QtGui.QPixmap("icon/glowstone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.glowstone.setIcon(icon113)
        self.glowstone.setIconSize(QtCore.QSize(16, 16))
        self.glowstone.setTristate(False)
        self.glowstone.setObjectName("glowstone")
        self.gridLayout.addWidget(self.CardWidget_160, 1, 2, 1, 1)
        self.CardWidget_162 = CardWidget(self.layoutWidget1)
        self.CardWidget_162.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_162.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_162.setObjectName("CardWidget_162")
        self.end_stone = CheckBox(self.CardWidget_162)
        self.end_stone.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.end_stone.setMinimumSize(QtCore.QSize(17, 16))
        self.end_stone.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.end_stone.setFont(font)
        self.end_stone.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon114 = QtGui.QIcon()
        icon114.addPixmap(QtGui.QPixmap("icon/end_stone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.end_stone.setIcon(icon114)
        self.end_stone.setIconSize(QtCore.QSize(16, 16))
        self.end_stone.setTristate(False)
        self.end_stone.setObjectName("end_stone")
        self.gridLayout.addWidget(self.CardWidget_162, 3, 0, 1, 1)
        self.CardWidget_163 = CardWidget(self.layoutWidget1)
        self.CardWidget_163.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_163.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_163.setObjectName("CardWidget_163")
        self.ochre_froglight_top = CheckBox(self.CardWidget_163)
        self.ochre_froglight_top.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.ochre_froglight_top.setMinimumSize(QtCore.QSize(17, 16))
        self.ochre_froglight_top.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ochre_froglight_top.setFont(font)
        self.ochre_froglight_top.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon115 = QtGui.QIcon()
        icon115.addPixmap(QtGui.QPixmap("icon/ochre_froglight_top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ochre_froglight_top.setIcon(icon115)
        self.ochre_froglight_top.setIconSize(QtCore.QSize(16, 16))
        self.ochre_froglight_top.setTristate(False)
        self.ochre_froglight_top.setObjectName("ochre_froglight_top")
        self.gridLayout.addWidget(self.CardWidget_163, 3, 1, 1, 1)
        spacerItem143 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem143, 4, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout, 5, 3, 1, 1)
        self.gridLayout_65 = QtWidgets.QGridLayout()
        self.gridLayout_65.setObjectName("gridLayout_65")
        spacerItem144 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_65.addItem(spacerItem144, 1, 1, 1, 1)
        spacerItem145 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_65.addItem(spacerItem145, 1, 2, 1, 1)
        self.CardWidget_306 = CardWidget(self.layoutWidget1)
        self.CardWidget_306.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_306.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_306.setObjectName("CardWidget_306")
        self.deepslate = CheckBox(self.CardWidget_306)
        self.deepslate.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.deepslate.setMinimumSize(QtCore.QSize(17, 16))
        self.deepslate.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.deepslate.setFont(font)
        self.deepslate.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon116 = QtGui.QIcon()
        icon116.addPixmap(QtGui.QPixmap("icon/deepslate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deepslate.setIcon(icon116)
        self.deepslate.setIconSize(QtCore.QSize(16, 16))
        self.deepslate.setChecked(True)
        self.deepslate.setTristate(False)
        self.deepslate.setObjectName("deepslate")
        self.gridLayout_65.addWidget(self.CardWidget_306, 1, 0, 1, 1)
        spacerItem146 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_65.addItem(spacerItem146, 2, 1, 1, 1)
        spacerItem147 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_65.addItem(spacerItem147, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_65, 119, 3, 1, 1)
        self.HorizontalSeparator_82 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_82.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_82.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_82.setObjectName("HorizontalSeparator_82")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_82, 84, 1, 1, 1)
        self.HorizontalSeparator = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator.setObjectName("HorizontalSeparator")
        self.gridLayout_15.addWidget(self.HorizontalSeparator, 2, 1, 1, 1)
        self.HorizontalSeparator_109 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_109.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_109.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_109.setObjectName("HorizontalSeparator_109")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_109, 110, 3, 1, 1)
        self.VerticalSeparator_58 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_58.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_58.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_58.setObjectName("VerticalSeparator_58")
        self.gridLayout_15.addWidget(self.VerticalSeparator_58, 9, 2, 1, 1)
        self.HorizontalSeparator_63 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_63.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_63.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_63.setObjectName("HorizontalSeparator_63")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_63, 64, 3, 1, 1)
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.CardWidget_230 = CardWidget(self.layoutWidget1)
        self.CardWidget_230.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_230.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_230.setObjectName("CardWidget_230")
        self.light_gray_concrete = CheckBox(self.CardWidget_230)
        self.light_gray_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_gray_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.light_gray_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_gray_concrete.setFont(font)
        self.light_gray_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon117 = QtGui.QIcon()
        icon117.addPixmap(QtGui.QPixmap("icon/light_gray_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_gray_concrete.setIcon(icon117)
        self.light_gray_concrete.setIconSize(QtCore.QSize(16, 16))
        self.light_gray_concrete.setChecked(True)
        self.light_gray_concrete.setTristate(False)
        self.light_gray_concrete.setObjectName("light_gray_concrete")
        self.gridLayout_29.addWidget(self.CardWidget_230, 1, 0, 1, 1)
        spacerItem148 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_29.addItem(spacerItem148, 2, 1, 1, 1)
        spacerItem149 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_29.addItem(spacerItem149, 0, 1, 1, 1)
        self.CardWidget_231 = CardWidget(self.layoutWidget1)
        self.CardWidget_231.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_231.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_231.setObjectName("CardWidget_231")
        self.light_gray_wool = CheckBox(self.CardWidget_231)
        self.light_gray_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_gray_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.light_gray_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_gray_wool.setFont(font)
        self.light_gray_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon118 = QtGui.QIcon()
        icon118.addPixmap(QtGui.QPixmap("icon/light_gray_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_gray_wool.setIcon(icon118)
        self.light_gray_wool.setIconSize(QtCore.QSize(16, 16))
        self.light_gray_wool.setTristate(False)
        self.light_gray_wool.setObjectName("light_gray_wool")
        self.gridLayout_29.addWidget(self.CardWidget_231, 1, 1, 1, 1)
        self.CardWidget_232 = CardWidget(self.layoutWidget1)
        self.CardWidget_232.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_232.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_232.setObjectName("CardWidget_232")
        self.light_gray_stained_glass = CheckBox(self.CardWidget_232)
        self.light_gray_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_gray_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.light_gray_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_gray_stained_glass.setFont(font)
        self.light_gray_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon119 = QtGui.QIcon()
        icon119.addPixmap(QtGui.QPixmap("icon/light_gray_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_gray_stained_glass.setIcon(icon119)
        self.light_gray_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.light_gray_stained_glass.setTristate(False)
        self.light_gray_stained_glass.setObjectName("light_gray_stained_glass")
        self.gridLayout_29.addWidget(self.CardWidget_232, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_29, 45, 3, 1, 1)
        self.CardWidget_14 = CardWidget(self.layoutWidget1)
        self.CardWidget_14.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_14.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_14.setObjectName("CardWidget_14")
        self.layoutWidget_27 = QtWidgets.QWidget(self.CardWidget_14)
        self.layoutWidget_27.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_27.setObjectName("layoutWidget_27")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.layoutWidget_27)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.PixmapLabel_20 = PixmapLabel(self.layoutWidget_27)
        self.PixmapLabel_20.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_20.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_20.setObjectName("PixmapLabel_20")
        self.horizontalLayout_31.addWidget(self.PixmapLabel_20)
        self.CheckBox_B6 = CheckBox(self.layoutWidget_27)
        self.CheckBox_B6.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B6.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B6.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B6.setChecked(True)
        self.CheckBox_B6.setObjectName("CheckBox_B6")
        self.horizontalLayout_31.addWidget(self.CheckBox_B6)
        self.gridLayout_15.addWidget(self.CardWidget_14, 13, 1, 1, 1)
        self.HorizontalSeparator_99 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_99.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_99.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_99.setObjectName("HorizontalSeparator_99")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_99, 100, 3, 1, 1)
        self.HorizontalSeparator_80 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_80.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_80.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_80.setObjectName("HorizontalSeparator_80")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_80, 82, 1, 1, 1)
        self.HorizontalSeparator_97 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_97.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_97.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_97.setObjectName("HorizontalSeparator_97")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_97, 98, 3, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem150 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem150, 1, 2, 1, 1)
        self.CardWidget_156 = CardWidget(self.layoutWidget1)
        self.CardWidget_156.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_156.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_156.setObjectName("CardWidget_156")
        self.slime_block = CheckBox(self.CardWidget_156)
        self.slime_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.slime_block.setMinimumSize(QtCore.QSize(17, 16))
        self.slime_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.slime_block.setFont(font)
        self.slime_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon120 = QtGui.QIcon()
        icon120.addPixmap(QtGui.QPixmap("icon/slime_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slime_block.setIcon(icon120)
        self.slime_block.setIconSize(QtCore.QSize(16, 16))
        self.slime_block.setTristate(False)
        self.slime_block.setObjectName("slime_block")
        self.gridLayout_9.addWidget(self.CardWidget_156, 1, 1, 1, 1)
        spacerItem151 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem151, 2, 1, 1, 1)
        self.CardWidget_157 = CardWidget(self.layoutWidget1)
        self.CardWidget_157.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_157.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_157.setObjectName("CardWidget_157")
        self.grass_block = CheckBox(self.CardWidget_157)
        self.grass_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.grass_block.setMinimumSize(QtCore.QSize(17, 16))
        self.grass_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.grass_block.setFont(font)
        self.grass_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon121 = QtGui.QIcon()
        icon121.addPixmap(QtGui.QPixmap("icon/grass_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grass_block.setIcon(icon121)
        self.grass_block.setIconSize(QtCore.QSize(16, 16))
        self.grass_block.setChecked(True)
        self.grass_block.setAutoRepeat(False)
        self.grass_block.setTristate(False)
        self.grass_block.setObjectName("grass_block")
        self.gridLayout_9.addWidget(self.CardWidget_157, 1, 0, 1, 1)
        spacerItem152 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem152, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_9, 3, 3, 1, 1)
        self.gridLayout_58 = QtWidgets.QGridLayout()
        self.gridLayout_58.setObjectName("gridLayout_58")
        spacerItem153 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_58.addItem(spacerItem153, 1, 1, 1, 1)
        spacerItem154 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_58.addItem(spacerItem154, 1, 2, 1, 1)
        self.CardWidget_297 = CardWidget(self.layoutWidget1)
        self.CardWidget_297.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_297.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_297.setObjectName("CardWidget_297")
        self.stripped_crimson_stem = CheckBox(self.CardWidget_297)
        self.stripped_crimson_stem.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.stripped_crimson_stem.setMinimumSize(QtCore.QSize(17, 16))
        self.stripped_crimson_stem.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stripped_crimson_stem.setFont(font)
        self.stripped_crimson_stem.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon122 = QtGui.QIcon()
        icon122.addPixmap(QtGui.QPixmap("icon/stripped_crimson_stem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stripped_crimson_stem.setIcon(icon122)
        self.stripped_crimson_stem.setIconSize(QtCore.QSize(16, 16))
        self.stripped_crimson_stem.setChecked(True)
        self.stripped_crimson_stem.setTristate(False)
        self.stripped_crimson_stem.setObjectName("stripped_crimson_stem")
        self.gridLayout_58.addWidget(self.CardWidget_297, 1, 0, 1, 1)
        spacerItem155 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_58.addItem(spacerItem155, 2, 1, 1, 1)
        spacerItem156 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_58.addItem(spacerItem156, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_58, 107, 3, 1, 1)
        self.gridLayout_60 = QtWidgets.QGridLayout()
        self.gridLayout_60.setObjectName("gridLayout_60")
        spacerItem157 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_60.addItem(spacerItem157, 1, 2, 1, 1)
        self.CardWidget_299 = CardWidget(self.layoutWidget1)
        self.CardWidget_299.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_299.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_299.setObjectName("CardWidget_299")
        self.waxed_oxidized_copper = CheckBox(self.CardWidget_299)
        self.waxed_oxidized_copper.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.waxed_oxidized_copper.setMinimumSize(QtCore.QSize(17, 16))
        self.waxed_oxidized_copper.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.waxed_oxidized_copper.setFont(font)
        self.waxed_oxidized_copper.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon123 = QtGui.QIcon()
        icon123.addPixmap(QtGui.QPixmap("icon/waxed_oxidized_copper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.waxed_oxidized_copper.setIcon(icon123)
        self.waxed_oxidized_copper.setIconSize(QtCore.QSize(16, 16))
        self.waxed_oxidized_copper.setTristate(False)
        self.waxed_oxidized_copper.setObjectName("waxed_oxidized_copper")
        self.gridLayout_60.addWidget(self.CardWidget_299, 1, 1, 1, 1)
        spacerItem158 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_60.addItem(spacerItem158, 2, 1, 1, 1)
        spacerItem159 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_60.addItem(spacerItem159, 0, 1, 1, 1)
        self.CardWidget_300 = CardWidget(self.layoutWidget1)
        self.CardWidget_300.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_300.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_300.setObjectName("CardWidget_300")
        self.warped_nylium = CheckBox(self.CardWidget_300)
        self.warped_nylium.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.warped_nylium.setMinimumSize(QtCore.QSize(17, 16))
        self.warped_nylium.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.warped_nylium.setFont(font)
        self.warped_nylium.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon124 = QtGui.QIcon()
        icon124.addPixmap(QtGui.QPixmap("icon/warped_nylium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.warped_nylium.setIcon(icon124)
        self.warped_nylium.setIconSize(QtCore.QSize(16, 16))
        self.warped_nylium.setChecked(True)
        self.warped_nylium.setTristate(False)
        self.warped_nylium.setObjectName("warped_nylium")
        self.gridLayout_60.addWidget(self.CardWidget_300, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_60, 111, 3, 1, 1)
        self.CardWidget_59 = CardWidget(self.layoutWidget1)
        self.CardWidget_59.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_59.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_59.setObjectName("CardWidget_59")
        self.layoutWidget_113 = QtWidgets.QWidget(self.CardWidget_59)
        self.layoutWidget_113.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_113.setObjectName("layoutWidget_113")
        self.horizontalLayout_121 = QtWidgets.QHBoxLayout(self.layoutWidget_113)
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_121.setObjectName("horizontalLayout_121")
        self.PixmapLabel_65 = PixmapLabel(self.layoutWidget_113)
        self.PixmapLabel_65.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_65.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_65.setObjectName("PixmapLabel_65")
        self.horizontalLayout_121.addWidget(self.PixmapLabel_65)
        self.CheckBox_B47 = CheckBox(self.layoutWidget_113)
        self.CheckBox_B47.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B47.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B47.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B47.setChecked(True)
        self.CheckBox_B47.setObjectName("CheckBox_B47")
        self.horizontalLayout_121.addWidget(self.CheckBox_B47)
        self.gridLayout_15.addWidget(self.CardWidget_59, 95, 1, 1, 1)
        self.CardWidget_11 = CardWidget(self.layoutWidget1)
        self.CardWidget_11.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_11.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_11.setObjectName("CardWidget_11")
        self.layoutWidget_21 = QtWidgets.QWidget(self.CardWidget_11)
        self.layoutWidget_21.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_21.setObjectName("layoutWidget_21")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.layoutWidget_21)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.PixmapLabel_17 = PixmapLabel(self.layoutWidget_21)
        self.PixmapLabel_17.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_17.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_17.setObjectName("PixmapLabel_17")
        self.horizontalLayout_25.addWidget(self.PixmapLabel_17)
        self.CheckBox_B3 = CheckBox(self.layoutWidget_21)
        self.CheckBox_B3.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B3.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B3.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B3.setChecked(True)
        self.CheckBox_B3.setObjectName("CheckBox_B3")
        self.horizontalLayout_25.addWidget(self.CheckBox_B3)
        self.gridLayout_15.addWidget(self.CardWidget_11, 7, 1, 1, 1)
        self.VerticalSeparator_41 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_41.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_41.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_41.setObjectName("VerticalSeparator_41")
        self.gridLayout_15.addWidget(self.VerticalSeparator_41, 43, 2, 1, 1)
        self.gridLayout_28 = QtWidgets.QGridLayout()
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.CardWidget_219 = CardWidget(self.layoutWidget1)
        self.CardWidget_219.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_219.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_219.setObjectName("CardWidget_219")
        self.lime_concrete = CheckBox(self.CardWidget_219)
        self.lime_concrete.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.lime_concrete.setMinimumSize(QtCore.QSize(17, 16))
        self.lime_concrete.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lime_concrete.setFont(font)
        self.lime_concrete.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon125 = QtGui.QIcon()
        icon125.addPixmap(QtGui.QPixmap("icon/lime_concrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lime_concrete.setIcon(icon125)
        self.lime_concrete.setIconSize(QtCore.QSize(16, 16))
        self.lime_concrete.setChecked(True)
        self.lime_concrete.setTristate(False)
        self.lime_concrete.setObjectName("lime_concrete")
        self.gridLayout_28.addWidget(self.CardWidget_219, 1, 0, 1, 1)
        spacerItem160 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_28.addItem(spacerItem160, 2, 1, 1, 1)
        spacerItem161 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_28.addItem(spacerItem161, 0, 1, 1, 1)
        self.CardWidget_220 = CardWidget(self.layoutWidget1)
        self.CardWidget_220.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_220.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_220.setObjectName("CardWidget_220")
        self.lime_wool = CheckBox(self.CardWidget_220)
        self.lime_wool.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.lime_wool.setMinimumSize(QtCore.QSize(17, 16))
        self.lime_wool.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lime_wool.setFont(font)
        self.lime_wool.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon126 = QtGui.QIcon()
        icon126.addPixmap(QtGui.QPixmap("icon/lime_wool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lime_wool.setIcon(icon126)
        self.lime_wool.setIconSize(QtCore.QSize(16, 16))
        self.lime_wool.setTristate(False)
        self.lime_wool.setObjectName("lime_wool")
        self.gridLayout_28.addWidget(self.CardWidget_220, 1, 1, 1, 1)
        self.CardWidget_221 = CardWidget(self.layoutWidget1)
        self.CardWidget_221.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_221.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_221.setObjectName("CardWidget_221")
        self.lime_stained_glass = CheckBox(self.CardWidget_221)
        self.lime_stained_glass.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.lime_stained_glass.setMinimumSize(QtCore.QSize(17, 16))
        self.lime_stained_glass.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lime_stained_glass.setFont(font)
        self.lime_stained_glass.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon127 = QtGui.QIcon()
        icon127.addPixmap(QtGui.QPixmap("icon/lime_stained_glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lime_stained_glass.setIcon(icon127)
        self.lime_stained_glass.setIconSize(QtCore.QSize(16, 16))
        self.lime_stained_glass.setTristate(False)
        self.lime_stained_glass.setObjectName("lime_stained_glass")
        self.gridLayout_28.addWidget(self.CardWidget_221, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_28, 39, 3, 1, 1)
        self.CardWidget_13 = CardWidget(self.layoutWidget1)
        self.CardWidget_13.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_13.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_13.setObjectName("CardWidget_13")
        self.layoutWidget_25 = QtWidgets.QWidget(self.CardWidget_13)
        self.layoutWidget_25.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_25.setObjectName("layoutWidget_25")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.layoutWidget_25)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.PixmapLabel_19 = PixmapLabel(self.layoutWidget_25)
        self.PixmapLabel_19.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_19.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_19.setObjectName("PixmapLabel_19")
        self.horizontalLayout_29.addWidget(self.PixmapLabel_19)
        self.CheckBox_B5 = CheckBox(self.layoutWidget_25)
        self.CheckBox_B5.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B5.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B5.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B5.setChecked(True)
        self.CheckBox_B5.setObjectName("CheckBox_B5")
        self.horizontalLayout_29.addWidget(self.CheckBox_B5)
        self.gridLayout_15.addWidget(self.CardWidget_13, 11, 1, 1, 1)
        self.gridLayout_48 = QtWidgets.QGridLayout()
        self.gridLayout_48.setObjectName("gridLayout_48")
        spacerItem162 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_48.addItem(spacerItem162, 1, 1, 1, 1)
        spacerItem163 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_48.addItem(spacerItem163, 1, 2, 1, 1)
        self.CardWidget_284 = CardWidget(self.layoutWidget1)
        self.CardWidget_284.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_284.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_284.setObjectName("CardWidget_284")
        self.gray_terracotta = CheckBox(self.CardWidget_284)
        self.gray_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.gray_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.gray_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gray_terracotta.setFont(font)
        self.gray_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon128 = QtGui.QIcon()
        icon128.addPixmap(QtGui.QPixmap("icon/gray_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gray_terracotta.setIcon(icon128)
        self.gray_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.gray_terracotta.setChecked(True)
        self.gray_terracotta.setTristate(False)
        self.gray_terracotta.setObjectName("gray_terracotta")
        self.gridLayout_48.addWidget(self.CardWidget_284, 1, 0, 1, 1)
        spacerItem164 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_48.addItem(spacerItem164, 2, 1, 1, 1)
        spacerItem165 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_48.addItem(spacerItem165, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_48, 87, 3, 1, 1)
        self.VerticalSeparator_39 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_39.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_39.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_39.setObjectName("VerticalSeparator_39")
        self.gridLayout_15.addWidget(self.VerticalSeparator_39, 47, 2, 1, 1)
        self.CardWidget_34 = CardWidget(self.layoutWidget1)
        self.CardWidget_34.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_34.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_34.setObjectName("CardWidget_34")
        self.layoutWidget_63 = QtWidgets.QWidget(self.CardWidget_34)
        self.layoutWidget_63.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_63.setObjectName("layoutWidget_63")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout(self.layoutWidget_63)
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.PixmapLabel_40 = PixmapLabel(self.layoutWidget_63)
        self.PixmapLabel_40.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_40.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_40.setObjectName("PixmapLabel_40")
        self.horizontalLayout_71.addWidget(self.PixmapLabel_40)
        self.CheckBox_B22 = CheckBox(self.layoutWidget_63)
        self.CheckBox_B22.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B22.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B22.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B22.setChecked(True)
        self.CheckBox_B22.setObjectName("CheckBox_B22")
        self.horizontalLayout_71.addWidget(self.CheckBox_B22)
        self.gridLayout_15.addWidget(self.CardWidget_34, 45, 1, 1, 1)
        self.VerticalSeparator_32 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_32.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_32.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_32.setObjectName("VerticalSeparator_32")
        self.gridLayout_15.addWidget(self.VerticalSeparator_32, 61, 2, 1, 1)
        self.VerticalSeparator_52 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_52.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_52.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_52.setObjectName("VerticalSeparator_52")
        self.gridLayout_15.addWidget(self.VerticalSeparator_52, 21, 2, 1, 1)
        self.HorizontalSeparator_38 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_38.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_38.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_38.setObjectName("HorizontalSeparator_38")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_38, 38, 3, 1, 1)
        self.CardWidget_36 = CardWidget(self.layoutWidget1)
        self.CardWidget_36.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_36.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_36.setObjectName("CardWidget_36")
        self.layoutWidget_67 = QtWidgets.QWidget(self.CardWidget_36)
        self.layoutWidget_67.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_67.setObjectName("layoutWidget_67")
        self.horizontalLayout_75 = QtWidgets.QHBoxLayout(self.layoutWidget_67)
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.PixmapLabel_42 = PixmapLabel(self.layoutWidget_67)
        self.PixmapLabel_42.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_42.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_42.setObjectName("PixmapLabel_42")
        self.horizontalLayout_75.addWidget(self.PixmapLabel_42)
        self.CheckBox_B24 = CheckBox(self.layoutWidget_67)
        self.CheckBox_B24.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B24.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B24.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B24.setChecked(True)
        self.CheckBox_B24.setObjectName("CheckBox_B24")
        self.horizontalLayout_75.addWidget(self.CheckBox_B24)
        self.gridLayout_15.addWidget(self.CardWidget_36, 49, 1, 1, 1)
        self.HorizontalSeparator_67 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_67.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_67.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_67.setObjectName("HorizontalSeparator_67")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_67, 68, 3, 1, 1)
        self.CardWidget_50 = CardWidget(self.layoutWidget1)
        self.CardWidget_50.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_50.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_50.setObjectName("CardWidget_50")
        self.layoutWidget_95 = QtWidgets.QWidget(self.CardWidget_50)
        self.layoutWidget_95.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_95.setObjectName("layoutWidget_95")
        self.horizontalLayout_103 = QtWidgets.QHBoxLayout(self.layoutWidget_95)
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_103.setObjectName("horizontalLayout_103")
        self.PixmapLabel_56 = PixmapLabel(self.layoutWidget_95)
        self.PixmapLabel_56.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_56.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_56.setObjectName("PixmapLabel_56")
        self.horizontalLayout_103.addWidget(self.PixmapLabel_56)
        self.CheckBox_B38 = CheckBox(self.layoutWidget_95)
        self.CheckBox_B38.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B38.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B38.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B38.setChecked(True)
        self.CheckBox_B38.setObjectName("CheckBox_B38")
        self.horizontalLayout_103.addWidget(self.CheckBox_B38)
        self.gridLayout_15.addWidget(self.CardWidget_50, 77, 1, 1, 1)
        self.CardWidget_68 = CardWidget(self.layoutWidget1)
        self.CardWidget_68.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_68.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_68.setObjectName("CardWidget_68")
        self.layoutWidget_131 = QtWidgets.QWidget(self.CardWidget_68)
        self.layoutWidget_131.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_131.setObjectName("layoutWidget_131")
        self.horizontalLayout_139 = QtWidgets.QHBoxLayout(self.layoutWidget_131)
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_139.setObjectName("horizontalLayout_139")
        self.PixmapLabel_74 = PixmapLabel(self.layoutWidget_131)
        self.PixmapLabel_74.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_74.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_74.setObjectName("PixmapLabel_74")
        self.horizontalLayout_139.addWidget(self.PixmapLabel_74)
        self.CheckBox_B56 = CheckBox(self.layoutWidget_131)
        self.CheckBox_B56.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B56.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B56.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B56.setChecked(True)
        self.CheckBox_B56.setObjectName("CheckBox_B56")
        self.horizontalLayout_139.addWidget(self.CheckBox_B56)
        self.gridLayout_15.addWidget(self.CardWidget_68, 113, 1, 1, 1)
        self.CardWidget_28 = CardWidget(self.layoutWidget1)
        self.CardWidget_28.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_28.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_28.setObjectName("CardWidget_28")
        self.layoutWidget_51 = QtWidgets.QWidget(self.CardWidget_28)
        self.layoutWidget_51.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_51.setObjectName("layoutWidget_51")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.layoutWidget_51)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.PixmapLabel_34 = PixmapLabel(self.layoutWidget_51)
        self.PixmapLabel_34.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_34.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_34.setObjectName("PixmapLabel_34")
        self.horizontalLayout_59.addWidget(self.PixmapLabel_34)
        self.CheckBox_B16 = CheckBox(self.layoutWidget_51)
        self.CheckBox_B16.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B16.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B16.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B16.setChecked(True)
        self.CheckBox_B16.setObjectName("CheckBox_B16")
        self.horizontalLayout_59.addWidget(self.CheckBox_B16)
        self.gridLayout_15.addWidget(self.CardWidget_28, 33, 1, 1, 1)
        self.HorizontalSeparator_13 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_13.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_13.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_13.setObjectName("HorizontalSeparator_13")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_13, 14, 1, 1, 1)
        self.gridLayout_41 = QtWidgets.QGridLayout()
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.CardWidget_276 = CardWidget(self.layoutWidget1)
        self.CardWidget_276.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_276.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_276.setObjectName("CardWidget_276")
        self.white_terracotta = CheckBox(self.CardWidget_276)
        self.white_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.white_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.white_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.white_terracotta.setFont(font)
        self.white_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon129 = QtGui.QIcon()
        icon129.addPixmap(QtGui.QPixmap("icon/white_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.white_terracotta.setIcon(icon129)
        self.white_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.white_terracotta.setChecked(True)
        self.white_terracotta.setTristate(False)
        self.white_terracotta.setObjectName("white_terracotta")
        self.gridLayout_41.addWidget(self.CardWidget_276, 1, 0, 1, 1)
        spacerItem166 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_41.addItem(spacerItem166, 2, 1, 1, 1)
        spacerItem167 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_41.addItem(spacerItem167, 0, 1, 1, 1)
        self.CardWidget_277 = CardWidget(self.layoutWidget1)
        self.CardWidget_277.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_277.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_277.setObjectName("CardWidget_277")
        self.calcite = CheckBox(self.CardWidget_277)
        self.calcite.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.calcite.setMinimumSize(QtCore.QSize(17, 16))
        self.calcite.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calcite.setFont(font)
        self.calcite.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon130 = QtGui.QIcon()
        icon130.addPixmap(QtGui.QPixmap("icon/calcite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calcite.setIcon(icon130)
        self.calcite.setIconSize(QtCore.QSize(16, 16))
        self.calcite.setTristate(False)
        self.calcite.setObjectName("calcite")
        self.gridLayout_41.addWidget(self.CardWidget_277, 1, 1, 1, 1)
        self.CardWidget_278 = CardWidget(self.layoutWidget1)
        self.CardWidget_278.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_278.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_278.setObjectName("CardWidget_278")
        self.cherry_planks = CheckBox(self.CardWidget_278)
        self.cherry_planks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.cherry_planks.setMinimumSize(QtCore.QSize(17, 16))
        self.cherry_planks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cherry_planks.setFont(font)
        self.cherry_planks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon131 = QtGui.QIcon()
        icon131.addPixmap(QtGui.QPixmap("icon/cherry_planks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cherry_planks.setIcon(icon131)
        self.cherry_planks.setIconSize(QtCore.QSize(16, 16))
        self.cherry_planks.setTristate(False)
        self.cherry_planks.setObjectName("cherry_planks")
        self.gridLayout_41.addWidget(self.CardWidget_278, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_41, 73, 3, 1, 1)
        self.CardWidget_43 = CardWidget(self.layoutWidget1)
        self.CardWidget_43.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_43.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_43.setObjectName("CardWidget_43")
        self.layoutWidget_81 = QtWidgets.QWidget(self.CardWidget_43)
        self.layoutWidget_81.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_81.setObjectName("layoutWidget_81")
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout(self.layoutWidget_81)
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.PixmapLabel_49 = PixmapLabel(self.layoutWidget_81)
        self.PixmapLabel_49.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_49.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_49.setObjectName("PixmapLabel_49")
        self.horizontalLayout_89.addWidget(self.PixmapLabel_49)
        self.CheckBox_B31 = CheckBox(self.layoutWidget_81)
        self.CheckBox_B31.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B31.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B31.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B31.setChecked(True)
        self.CheckBox_B31.setObjectName("CheckBox_B31")
        self.horizontalLayout_89.addWidget(self.CheckBox_B31)
        self.gridLayout_15.addWidget(self.CardWidget_43, 63, 1, 1, 1)
        self.HorizontalSeparator_100 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_100.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_100.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_100.setObjectName("HorizontalSeparator_100")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_100, 102, 1, 1, 1)
        self.CardWidget_9 = CardWidget(self.layoutWidget1)
        self.CardWidget_9.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_9.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_9.setObjectName("CardWidget_9")
        self.layoutWidget_17 = QtWidgets.QWidget(self.CardWidget_9)
        self.layoutWidget_17.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_17.setObjectName("layoutWidget_17")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.PixmapLabel_15 = PixmapLabel(self.layoutWidget_17)
        self.PixmapLabel_15.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_15.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_15.setObjectName("PixmapLabel_15")
        self.horizontalLayout_21.addWidget(self.PixmapLabel_15)
        self.CheckBox_B2 = CheckBox(self.layoutWidget_17)
        self.CheckBox_B2.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B2.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B2.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B2.setChecked(True)
        self.CheckBox_B2.setObjectName("CheckBox_B2")
        self.horizontalLayout_21.addWidget(self.CheckBox_B2)
        self.gridLayout_15.addWidget(self.CardWidget_9, 5, 1, 1, 1)
        self.HorizontalSeparator_76 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_76.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_76.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_76.setObjectName("HorizontalSeparator_76")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_76, 78, 1, 1, 1)
        self.VerticalSeparator_5 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_5.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_5.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_5.setObjectName("VerticalSeparator_5")
        self.gridLayout_15.addWidget(self.VerticalSeparator_5, 117, 2, 1, 1)
        self.VerticalSeparator_64 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_64.setObjectName("VerticalSeparator_64")
        self.gridLayout_15.addWidget(self.VerticalSeparator_64, 1, 4, 123, 1)
        self.CardWidget_41 = CardWidget(self.layoutWidget1)
        self.CardWidget_41.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_41.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_41.setObjectName("CardWidget_41")
        self.layoutWidget_77 = QtWidgets.QWidget(self.CardWidget_41)
        self.layoutWidget_77.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_77.setObjectName("layoutWidget_77")
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout(self.layoutWidget_77)
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.PixmapLabel_47 = PixmapLabel(self.layoutWidget_77)
        self.PixmapLabel_47.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_47.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_47.setObjectName("PixmapLabel_47")
        self.horizontalLayout_85.addWidget(self.PixmapLabel_47)
        self.CheckBox_B29 = CheckBox(self.layoutWidget_77)
        self.CheckBox_B29.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B29.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B29.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B29.setChecked(True)
        self.CheckBox_B29.setObjectName("CheckBox_B29")
        self.horizontalLayout_85.addWidget(self.CheckBox_B29)
        self.gridLayout_15.addWidget(self.CardWidget_41, 59, 1, 1, 1)
        self.HorizontalSeparator_111 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_111.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_111.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_111.setObjectName("HorizontalSeparator_111")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_111, 112, 3, 1, 1)
        self.HorizontalSeparator_68 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_68.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_68.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_68.setObjectName("HorizontalSeparator_68")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_68, 70, 1, 1, 1)
        self.HorizontalSeparator_52 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_52.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_52.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_52.setObjectName("HorizontalSeparator_52")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_52, 52, 3, 1, 1)
        self.HorizontalSeparator_112 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_112.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_112.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_112.setObjectName("HorizontalSeparator_112")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_112, 114, 1, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        spacerItem168 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem168, 1, 2, 1, 1)
        self.CardWidget_186 = CardWidget(self.layoutWidget1)
        self.CardWidget_186.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_186.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_186.setObjectName("CardWidget_186")
        self.smooth_stone = CheckBox(self.CardWidget_186)
        self.smooth_stone.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.smooth_stone.setMinimumSize(QtCore.QSize(17, 16))
        self.smooth_stone.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.smooth_stone.setFont(font)
        self.smooth_stone.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon132 = QtGui.QIcon()
        icon132.addPixmap(QtGui.QPixmap("icon/smooth_stone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smooth_stone.setIcon(icon132)
        self.smooth_stone.setIconSize(QtCore.QSize(16, 16))
        self.smooth_stone.setTristate(False)
        self.smooth_stone.setObjectName("smooth_stone")
        self.gridLayout_22.addWidget(self.CardWidget_186, 1, 1, 1, 1)
        spacerItem169 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem169, 2, 1, 1, 1)
        spacerItem170 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem170, 0, 1, 1, 1)
        self.CardWidget_187 = CardWidget(self.layoutWidget1)
        self.CardWidget_187.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_187.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_187.setObjectName("CardWidget_187")
        self.polished_andesite = CheckBox(self.CardWidget_187)
        self.polished_andesite.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.polished_andesite.setMinimumSize(QtCore.QSize(17, 16))
        self.polished_andesite.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.polished_andesite.setFont(font)
        self.polished_andesite.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon133 = QtGui.QIcon()
        icon133.addPixmap(QtGui.QPixmap("icon/polished_andesite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polished_andesite.setIcon(icon133)
        self.polished_andesite.setIconSize(QtCore.QSize(16, 16))
        self.polished_andesite.setChecked(True)
        self.polished_andesite.setTristate(False)
        self.polished_andesite.setObjectName("polished_andesite")
        self.gridLayout_22.addWidget(self.CardWidget_187, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_22, 23, 3, 1, 1)
        self.HorizontalSeparator_91 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_91.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_91.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_91.setObjectName("HorizontalSeparator_91")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_91, 92, 3, 1, 1)
        self.CardWidget_52 = CardWidget(self.layoutWidget1)
        self.CardWidget_52.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_52.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_52.setObjectName("CardWidget_52")
        self.layoutWidget_99 = QtWidgets.QWidget(self.CardWidget_52)
        self.layoutWidget_99.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_99.setObjectName("layoutWidget_99")
        self.horizontalLayout_107 = QtWidgets.QHBoxLayout(self.layoutWidget_99)
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.PixmapLabel_58 = PixmapLabel(self.layoutWidget_99)
        self.PixmapLabel_58.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_58.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_58.setObjectName("PixmapLabel_58")
        self.horizontalLayout_107.addWidget(self.PixmapLabel_58)
        self.CheckBox_B40 = CheckBox(self.layoutWidget_99)
        self.CheckBox_B40.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B40.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B40.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B40.setChecked(True)
        self.CheckBox_B40.setObjectName("CheckBox_B40")
        self.horizontalLayout_107.addWidget(self.CheckBox_B40)
        self.gridLayout_15.addWidget(self.CardWidget_52, 81, 1, 1, 1)
        self.CardWidget_25 = CardWidget(self.layoutWidget1)
        self.CardWidget_25.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_25.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_25.setObjectName("CardWidget_25")
        self.layoutWidget_45 = QtWidgets.QWidget(self.CardWidget_25)
        self.layoutWidget_45.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_45.setObjectName("layoutWidget_45")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.layoutWidget_45)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.PixmapLabel_31 = PixmapLabel(self.layoutWidget_45)
        self.PixmapLabel_31.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_31.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_31.setObjectName("PixmapLabel_31")
        self.horizontalLayout_53.addWidget(self.PixmapLabel_31)
        self.CheckBox_B13 = CheckBox(self.layoutWidget_45)
        self.CheckBox_B13.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B13.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B13.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B13.setChecked(True)
        self.CheckBox_B13.setObjectName("CheckBox_B13")
        self.horizontalLayout_53.addWidget(self.CheckBox_B13)
        self.gridLayout_15.addWidget(self.CardWidget_25, 27, 1, 1, 1)
        self.CardWidget_23 = CardWidget(self.layoutWidget1)
        self.CardWidget_23.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_23.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_23.setObjectName("CardWidget_23")
        self.layoutWidget_41 = QtWidgets.QWidget(self.CardWidget_23)
        self.layoutWidget_41.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_41.setObjectName("layoutWidget_41")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.layoutWidget_41)
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.PixmapLabel_29 = PixmapLabel(self.layoutWidget_41)
        self.PixmapLabel_29.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_29.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_29.setObjectName("PixmapLabel_29")
        self.horizontalLayout_49.addWidget(self.PixmapLabel_29)
        self.CheckBox_B11 = CheckBox(self.layoutWidget_41)
        self.CheckBox_B11.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B11.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B11.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B11.setChecked(True)
        self.CheckBox_B11.setObjectName("CheckBox_B11")
        self.horizontalLayout_49.addWidget(self.CheckBox_B11)
        self.gridLayout_15.addWidget(self.CardWidget_23, 23, 1, 1, 1)
        self.HorizontalSeparator_7 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_7.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_7.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_7.setObjectName("HorizontalSeparator_7")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_7, 8, 1, 1, 1)
        self.VerticalSeparator_27 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_27.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_27.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_27.setObjectName("VerticalSeparator_27")
        self.gridLayout_15.addWidget(self.VerticalSeparator_27, 71, 2, 1, 1)
        self.HorizontalSeparator_96 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_96.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_96.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_96.setObjectName("HorizontalSeparator_96")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_96, 98, 1, 1, 1)
        self.VerticalSeparator_62 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_62.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_62.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_62.setObjectName("VerticalSeparator_62")
        self.gridLayout_15.addWidget(self.VerticalSeparator_62, 1, 2, 1, 1)
        self.HorizontalSeparator_59 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_59.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_59.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_59.setObjectName("HorizontalSeparator_59")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_59, 60, 3, 1, 1)
        self.HorizontalSeparator_51 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_51.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_51.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_51.setObjectName("HorizontalSeparator_51")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_51, 52, 1, 1, 1)
        self.CardWidget_10 = CardWidget(self.layoutWidget1)
        self.CardWidget_10.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_10.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_10.setObjectName("CardWidget_10")
        self.layoutWidget_19 = QtWidgets.QWidget(self.CardWidget_10)
        self.layoutWidget_19.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_19.setObjectName("layoutWidget_19")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.layoutWidget_19)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.PixmapLabel_16 = PixmapLabel(self.layoutWidget_19)
        self.PixmapLabel_16.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_16.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_16.setObjectName("PixmapLabel_16")
        self.horizontalLayout_23.addWidget(self.PixmapLabel_16)
        self.CheckBox_B1 = CheckBox(self.layoutWidget_19)
        self.CheckBox_B1.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B1.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B1.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B1.setChecked(True)
        self.CheckBox_B1.setObjectName("CheckBox_B1")
        self.horizontalLayout_23.addWidget(self.CheckBox_B1)
        self.gridLayout_15.addWidget(self.CardWidget_10, 3, 1, 1, 1)
        self.HorizontalSeparator_57 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_57.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_57.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_57.setObjectName("HorizontalSeparator_57")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_57, 58, 3, 1, 1)
        self.HorizontalSeparator_71 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_71.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_71.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_71.setObjectName("HorizontalSeparator_71")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_71, 72, 3, 1, 1)
        self.gridLayout_36 = QtWidgets.QGridLayout()
        self.gridLayout_36.setObjectName("gridLayout_36")
        spacerItem171 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem171, 1, 2, 1, 1)
        self.CardWidget_194 = CardWidget(self.layoutWidget1)
        self.CardWidget_194.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_194.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_194.setObjectName("CardWidget_194")
        self.prismarine_bricks = CheckBox(self.CardWidget_194)
        self.prismarine_bricks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.prismarine_bricks.setMinimumSize(QtCore.QSize(17, 16))
        self.prismarine_bricks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prismarine_bricks.setFont(font)
        self.prismarine_bricks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon134 = QtGui.QIcon()
        icon134.addPixmap(QtGui.QPixmap("icon/prismarine_bricks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prismarine_bricks.setIcon(icon134)
        self.prismarine_bricks.setIconSize(QtCore.QSize(16, 16))
        self.prismarine_bricks.setTristate(False)
        self.prismarine_bricks.setObjectName("prismarine_bricks")
        self.gridLayout_36.addWidget(self.CardWidget_194, 1, 1, 1, 1)
        spacerItem172 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_36.addItem(spacerItem172, 2, 1, 1, 1)
        spacerItem173 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_36.addItem(spacerItem173, 0, 1, 1, 1)
        self.CardWidget_195 = CardWidget(self.layoutWidget1)
        self.CardWidget_195.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_195.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_195.setObjectName("CardWidget_195")
        self.diamond_block = CheckBox(self.CardWidget_195)
        self.diamond_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.diamond_block.setMinimumSize(QtCore.QSize(17, 16))
        self.diamond_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.diamond_block.setFont(font)
        self.diamond_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon135 = QtGui.QIcon()
        icon135.addPixmap(QtGui.QPixmap("icon/diamond_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.diamond_block.setIcon(icon135)
        self.diamond_block.setIconSize(QtCore.QSize(16, 16))
        self.diamond_block.setChecked(True)
        self.diamond_block.setTristate(False)
        self.diamond_block.setObjectName("diamond_block")
        self.gridLayout_36.addWidget(self.CardWidget_195, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_36, 63, 3, 1, 1)
        self.HorizontalSeparator_42 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_42.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_42.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_42.setObjectName("HorizontalSeparator_42")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_42, 42, 3, 1, 1)
        self.VerticalSeparator_19 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_19.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_19.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_19.setObjectName("VerticalSeparator_19")
        self.gridLayout_15.addWidget(self.VerticalSeparator_19, 87, 2, 1, 1)
        self.HorizontalSeparator_18 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_18.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_18.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_18.setObjectName("HorizontalSeparator_18")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_18, 18, 3, 1, 1)
        self.HorizontalSeparator_73 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_73.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_73.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_73.setObjectName("HorizontalSeparator_73")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_73, 74, 3, 1, 1)
        self.HorizontalSeparator_26 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_26.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_26.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_26.setObjectName("HorizontalSeparator_26")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_26, 26, 3, 1, 1)
        self.HorizontalSeparator_117 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_117.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_117.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_117.setObjectName("HorizontalSeparator_117")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_117, 118, 3, 1, 1)
        self.HorizontalSeparator_62 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_62.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_62.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_62.setObjectName("HorizontalSeparator_62")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_62, 64, 1, 1, 1)
        self.HorizontalSeparator_58 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_58.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_58.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_58.setObjectName("HorizontalSeparator_58")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_58, 60, 1, 1, 1)
        self.CardWidget_12 = CardWidget(self.layoutWidget1)
        self.CardWidget_12.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_12.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_12.setObjectName("CardWidget_12")
        self.layoutWidget_23 = QtWidgets.QWidget(self.CardWidget_12)
        self.layoutWidget_23.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_23.setObjectName("layoutWidget_23")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.layoutWidget_23)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.PixmapLabel_18 = PixmapLabel(self.layoutWidget_23)
        self.PixmapLabel_18.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_18.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_18.setObjectName("PixmapLabel_18")
        self.horizontalLayout_27.addWidget(self.PixmapLabel_18)
        self.CheckBox_B4 = CheckBox(self.layoutWidget_23)
        self.CheckBox_B4.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B4.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B4.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B4.setChecked(True)
        self.CheckBox_B4.setObjectName("CheckBox_B4")
        self.horizontalLayout_27.addWidget(self.CheckBox_B4)
        self.gridLayout_15.addWidget(self.CardWidget_12, 9, 1, 1, 1)
        self.HorizontalSeparator_94 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_94.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_94.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_94.setObjectName("HorizontalSeparator_94")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_94, 96, 1, 1, 1)
        self.gridLayout_47 = QtWidgets.QGridLayout()
        self.gridLayout_47.setObjectName("gridLayout_47")
        spacerItem174 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_47.addItem(spacerItem174, 1, 2, 1, 1)
        self.CardWidget_282 = CardWidget(self.layoutWidget1)
        self.CardWidget_282.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_282.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_282.setObjectName("CardWidget_282")
        self.stripped_cherry_log = CheckBox(self.CardWidget_282)
        self.stripped_cherry_log.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.stripped_cherry_log.setMinimumSize(QtCore.QSize(17, 16))
        self.stripped_cherry_log.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stripped_cherry_log.setFont(font)
        self.stripped_cherry_log.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon136 = QtGui.QIcon()
        icon136.addPixmap(QtGui.QPixmap("icon/stripped_cherry_log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stripped_cherry_log.setIcon(icon136)
        self.stripped_cherry_log.setIconSize(QtCore.QSize(16, 16))
        self.stripped_cherry_log.setTristate(False)
        self.stripped_cherry_log.setObjectName("stripped_cherry_log")
        self.gridLayout_47.addWidget(self.CardWidget_282, 1, 1, 1, 1)
        spacerItem175 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_47.addItem(spacerItem175, 2, 1, 1, 1)
        spacerItem176 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_47.addItem(spacerItem176, 0, 1, 1, 1)
        self.CardWidget_283 = CardWidget(self.layoutWidget1)
        self.CardWidget_283.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_283.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_283.setObjectName("CardWidget_283")
        self.pink_terracotta = CheckBox(self.CardWidget_283)
        self.pink_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.pink_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.pink_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pink_terracotta.setFont(font)
        self.pink_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon137 = QtGui.QIcon()
        icon137.addPixmap(QtGui.QPixmap("icon/pink_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pink_terracotta.setIcon(icon137)
        self.pink_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.pink_terracotta.setChecked(True)
        self.pink_terracotta.setTristate(False)
        self.pink_terracotta.setObjectName("pink_terracotta")
        self.gridLayout_47.addWidget(self.CardWidget_283, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_47, 85, 3, 1, 1)
        self.gridLayout_45 = QtWidgets.QGridLayout()
        self.gridLayout_45.setObjectName("gridLayout_45")
        spacerItem177 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_45.addItem(spacerItem177, 1, 1, 1, 1)
        spacerItem178 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_45.addItem(spacerItem178, 1, 2, 1, 1)
        self.CardWidget_280 = CardWidget(self.layoutWidget1)
        self.CardWidget_280.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_280.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_280.setObjectName("CardWidget_280")
        self.yellow_terracotta = CheckBox(self.CardWidget_280)
        self.yellow_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.yellow_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.yellow_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.yellow_terracotta.setFont(font)
        self.yellow_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon138 = QtGui.QIcon()
        icon138.addPixmap(QtGui.QPixmap("icon/yellow_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_terracotta.setIcon(icon138)
        self.yellow_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.yellow_terracotta.setChecked(True)
        self.yellow_terracotta.setTristate(False)
        self.yellow_terracotta.setObjectName("yellow_terracotta")
        self.gridLayout_45.addWidget(self.CardWidget_280, 1, 0, 1, 1)
        spacerItem179 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_45.addItem(spacerItem179, 2, 1, 1, 1)
        spacerItem180 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_45.addItem(spacerItem180, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_45, 81, 3, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem181 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem181, 1, 2, 1, 1)
        self.CardWidget_171 = CardWidget(self.layoutWidget1)
        self.CardWidget_171.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_171.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_171.setObjectName("CardWidget_171")
        self.blue_ice = CheckBox(self.CardWidget_171)
        self.blue_ice.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.blue_ice.setMinimumSize(QtCore.QSize(17, 16))
        self.blue_ice.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.blue_ice.setFont(font)
        self.blue_ice.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon139 = QtGui.QIcon()
        icon139.addPixmap(QtGui.QPixmap("icon/blue_ice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blue_ice.setIcon(icon139)
        self.blue_ice.setIconSize(QtCore.QSize(16, 16))
        self.blue_ice.setTristate(False)
        self.blue_ice.setObjectName("blue_ice")
        self.gridLayout_12.addWidget(self.CardWidget_171, 1, 1, 1, 1)
        spacerItem182 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem182, 2, 1, 1, 1)
        spacerItem183 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem183, 0, 1, 1, 1)
        self.CardWidget_172 = CardWidget(self.layoutWidget1)
        self.CardWidget_172.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_172.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_172.setObjectName("CardWidget_172")
        self.ice = CheckBox(self.CardWidget_172)
        self.ice.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.ice.setMinimumSize(QtCore.QSize(17, 16))
        self.ice.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ice.setFont(font)
        self.ice.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon140 = QtGui.QIcon()
        icon140.addPixmap(QtGui.QPixmap("icon/ice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ice.setIcon(icon140)
        self.ice.setIconSize(QtCore.QSize(16, 16))
        self.ice.setChecked(True)
        self.ice.setTristate(False)
        self.ice.setObjectName("ice")
        self.gridLayout_12.addWidget(self.CardWidget_172, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_12, 11, 3, 1, 1)
        self.HorizontalSeparator_85 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_85.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_85.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_85.setObjectName("HorizontalSeparator_85")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_85, 86, 3, 1, 1)
        self.VerticalSeparator_25 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_25.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_25.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_25.setObjectName("VerticalSeparator_25")
        self.gridLayout_15.addWidget(self.VerticalSeparator_25, 75, 2, 1, 1)
        self.CardWidget_26 = CardWidget(self.layoutWidget1)
        self.CardWidget_26.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_26.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_26.setObjectName("CardWidget_26")
        self.layoutWidget_47 = QtWidgets.QWidget(self.CardWidget_26)
        self.layoutWidget_47.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_47.setObjectName("layoutWidget_47")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.layoutWidget_47)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.PixmapLabel_32 = PixmapLabel(self.layoutWidget_47)
        self.PixmapLabel_32.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_32.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_32.setObjectName("PixmapLabel_32")
        self.horizontalLayout_55.addWidget(self.PixmapLabel_32)
        self.CheckBox_B14 = CheckBox(self.layoutWidget_47)
        self.CheckBox_B14.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B14.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B14.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B14.setChecked(True)
        self.CheckBox_B14.setObjectName("CheckBox_B14")
        self.horizontalLayout_55.addWidget(self.CheckBox_B14)
        self.gridLayout_15.addWidget(self.CardWidget_26, 29, 1, 1, 1)
        self.VerticalSeparator_7 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_7.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_7.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_7.setObjectName("VerticalSeparator_7")
        self.gridLayout_15.addWidget(self.VerticalSeparator_7, 111, 2, 1, 1)
        self.HorizontalSeparator_70 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_70.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_70.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_70.setObjectName("HorizontalSeparator_70")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_70, 72, 1, 1, 1)
        self.VerticalSeparator_18 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_18.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_18.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_18.setObjectName("VerticalSeparator_18")
        self.gridLayout_15.addWidget(self.VerticalSeparator_18, 89, 2, 1, 1)
        self.HorizontalSeparator_46 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_46.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_46.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_46.setObjectName("HorizontalSeparator_46")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_46, 46, 3, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem184 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem184, 1, 1, 1, 1)
        spacerItem185 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem185, 1, 2, 1, 1)
        self.CardWidget_174 = CardWidget(self.layoutWidget1)
        self.CardWidget_174.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_174.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_174.setObjectName("CardWidget_174")
        self.oak_leaves = CheckBox(self.CardWidget_174)
        self.oak_leaves.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.oak_leaves.setMinimumSize(QtCore.QSize(17, 16))
        self.oak_leaves.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.oak_leaves.setFont(font)
        self.oak_leaves.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon141 = QtGui.QIcon()
        icon141.addPixmap(QtGui.QPixmap("icon/oak_leaves.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oak_leaves.setIcon(icon141)
        self.oak_leaves.setIconSize(QtCore.QSize(16, 16))
        self.oak_leaves.setChecked(True)
        self.oak_leaves.setTristate(False)
        self.oak_leaves.setObjectName("oak_leaves")
        self.gridLayout_14.addWidget(self.CardWidget_174, 1, 0, 1, 1)
        spacerItem186 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem186, 2, 1, 1, 1)
        spacerItem187 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem187, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 15, 3, 1, 1)
        self.HorizontalSeparator_107 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_107.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_107.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_107.setObjectName("HorizontalSeparator_107")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_107, 108, 3, 1, 1)
        self.VerticalSeparator_59 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_59.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_59.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_59.setObjectName("VerticalSeparator_59")
        self.gridLayout_15.addWidget(self.VerticalSeparator_59, 7, 2, 1, 1)
        self.gridLayout_44 = QtWidgets.QGridLayout()
        self.gridLayout_44.setObjectName("gridLayout_44")
        spacerItem188 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_44.addItem(spacerItem188, 1, 1, 1, 1)
        spacerItem189 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_44.addItem(spacerItem189, 1, 2, 1, 1)
        self.CardWidget_279 = CardWidget(self.layoutWidget1)
        self.CardWidget_279.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_279.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_279.setObjectName("CardWidget_279")
        self.light_blue_terracotta = CheckBox(self.CardWidget_279)
        self.light_blue_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_blue_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.light_blue_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_blue_terracotta.setFont(font)
        self.light_blue_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon142 = QtGui.QIcon()
        icon142.addPixmap(QtGui.QPixmap("icon/light_blue_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_blue_terracotta.setIcon(icon142)
        self.light_blue_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.light_blue_terracotta.setChecked(True)
        self.light_blue_terracotta.setTristate(False)
        self.light_blue_terracotta.setObjectName("light_blue_terracotta")
        self.gridLayout_44.addWidget(self.CardWidget_279, 1, 0, 1, 1)
        spacerItem190 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_44.addItem(spacerItem190, 2, 1, 1, 1)
        spacerItem191 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_44.addItem(spacerItem191, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_44, 79, 3, 1, 1)
        self.CardWidget_30 = CardWidget(self.layoutWidget1)
        self.CardWidget_30.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_30.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_30.setObjectName("CardWidget_30")
        self.layoutWidget_55 = QtWidgets.QWidget(self.CardWidget_30)
        self.layoutWidget_55.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_55.setObjectName("layoutWidget_55")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.layoutWidget_55)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.PixmapLabel_36 = PixmapLabel(self.layoutWidget_55)
        self.PixmapLabel_36.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_36.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_36.setObjectName("PixmapLabel_36")
        self.horizontalLayout_63.addWidget(self.PixmapLabel_36)
        self.CheckBox_B18 = CheckBox(self.layoutWidget_55)
        self.CheckBox_B18.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B18.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B18.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B18.setChecked(True)
        self.CheckBox_B18.setObjectName("CheckBox_B18")
        self.horizontalLayout_63.addWidget(self.CheckBox_B18)
        self.gridLayout_15.addWidget(self.CardWidget_30, 37, 1, 1, 1)
        self.CardWidget_56 = CardWidget(self.layoutWidget1)
        self.CardWidget_56.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_56.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_56.setObjectName("CardWidget_56")
        self.layoutWidget_107 = QtWidgets.QWidget(self.CardWidget_56)
        self.layoutWidget_107.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_107.setObjectName("layoutWidget_107")
        self.horizontalLayout_115 = QtWidgets.QHBoxLayout(self.layoutWidget_107)
        self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_115.setObjectName("horizontalLayout_115")
        self.PixmapLabel_62 = PixmapLabel(self.layoutWidget_107)
        self.PixmapLabel_62.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_62.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_62.setObjectName("PixmapLabel_62")
        self.horizontalLayout_115.addWidget(self.PixmapLabel_62)
        self.CheckBox_B44 = CheckBox(self.layoutWidget_107)
        self.CheckBox_B44.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B44.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B44.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B44.setChecked(True)
        self.CheckBox_B44.setObjectName("CheckBox_B44")
        self.horizontalLayout_115.addWidget(self.CheckBox_B44)
        self.gridLayout_15.addWidget(self.CardWidget_56, 89, 1, 1, 1)
        self.VerticalSeparator_54 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_54.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_54.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_54.setObjectName("VerticalSeparator_54")
        self.gridLayout_15.addWidget(self.VerticalSeparator_54, 17, 2, 1, 1)
        self.HorizontalSeparator_28 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_28.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_28.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_28.setObjectName("HorizontalSeparator_28")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_28, 28, 3, 1, 1)
        self.HorizontalSeparator_74 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_74.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_74.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_74.setObjectName("HorizontalSeparator_74")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_74, 76, 1, 1, 1)
        self.HorizontalSeparator_37 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_37.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_37.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_37.setObjectName("HorizontalSeparator_37")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_37, 38, 1, 1, 1)
        self.HorizontalSeparator_93 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_93.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_93.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_93.setObjectName("HorizontalSeparator_93")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_93, 94, 3, 1, 1)
        self.CardWidget_22 = CardWidget(self.layoutWidget1)
        self.CardWidget_22.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_22.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_22.setObjectName("CardWidget_22")
        self.layoutWidget_39 = QtWidgets.QWidget(self.CardWidget_22)
        self.layoutWidget_39.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_39.setObjectName("layoutWidget_39")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.layoutWidget_39)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.PixmapLabel_28 = PixmapLabel(self.layoutWidget_39)
        self.PixmapLabel_28.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_28.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_28.setObjectName("PixmapLabel_28")
        self.horizontalLayout_47.addWidget(self.PixmapLabel_28)
        self.CheckBox_B10 = CheckBox(self.layoutWidget_39)
        self.CheckBox_B10.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B10.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B10.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B10.setChecked(True)
        self.CheckBox_B10.setObjectName("CheckBox_B10")
        self.horizontalLayout_47.addWidget(self.CheckBox_B10)
        self.gridLayout_15.addWidget(self.CardWidget_22, 21, 1, 1, 1)
        self.HorizontalSeparator_3 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_3.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_3.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_3.setObjectName("HorizontalSeparator_3")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_3, 4, 1, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem192 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem192, 1, 1, 1, 1)
        spacerItem193 = QtWidgets.QSpacerItem(128, 16, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem193, 1, 2, 1, 1)
        self.CardWidget_173 = CardWidget(self.layoutWidget1)
        self.CardWidget_173.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_173.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_173.setObjectName("CardWidget_173")
        self.iron_block = CheckBox(self.CardWidget_173)
        self.iron_block.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.iron_block.setMinimumSize(QtCore.QSize(17, 16))
        self.iron_block.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.iron_block.setFont(font)
        self.iron_block.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon143 = QtGui.QIcon()
        icon143.addPixmap(QtGui.QPixmap("icon/iron_block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iron_block.setIcon(icon143)
        self.iron_block.setIconSize(QtCore.QSize(16, 16))
        self.iron_block.setChecked(True)
        self.iron_block.setTristate(False)
        self.iron_block.setObjectName("iron_block")
        self.gridLayout_13.addWidget(self.CardWidget_173, 1, 0, 1, 1)
        spacerItem194 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem194, 2, 1, 1, 1)
        spacerItem195 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem195, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_13, 13, 3, 1, 1)
        self.CardWidget_42 = CardWidget(self.layoutWidget1)
        self.CardWidget_42.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_42.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_42.setObjectName("CardWidget_42")
        self.layoutWidget_79 = QtWidgets.QWidget(self.CardWidget_42)
        self.layoutWidget_79.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_79.setObjectName("layoutWidget_79")
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout(self.layoutWidget_79)
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.PixmapLabel_48 = PixmapLabel(self.layoutWidget_79)
        self.PixmapLabel_48.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_48.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_48.setObjectName("PixmapLabel_48")
        self.horizontalLayout_87.addWidget(self.PixmapLabel_48)
        self.CheckBox_B30 = CheckBox(self.layoutWidget_79)
        self.CheckBox_B30.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B30.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B30.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B30.setChecked(True)
        self.CheckBox_B30.setObjectName("CheckBox_B30")
        self.horizontalLayout_87.addWidget(self.CheckBox_B30)
        self.gridLayout_15.addWidget(self.CardWidget_42, 61, 1, 1, 1)
        self.HorizontalSeparator_34 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_34.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_34.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_34.setObjectName("HorizontalSeparator_34")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_34, 34, 3, 1, 1)
        self.HorizontalSeparator_54 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_54.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_54.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_54.setObjectName("HorizontalSeparator_54")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_54, 54, 3, 1, 1)
        self.CardWidget_47 = CardWidget(self.layoutWidget1)
        self.CardWidget_47.setMinimumSize(QtCore.QSize(216, 36))
        self.CardWidget_47.setMaximumSize(QtCore.QSize(216, 36))
        self.CardWidget_47.setObjectName("CardWidget_47")
        self.layoutWidget_89 = QtWidgets.QWidget(self.CardWidget_47)
        self.layoutWidget_89.setGeometry(QtCore.QRect(0, 0, 208, 34))
        self.layoutWidget_89.setObjectName("layoutWidget_89")
        self.horizontalLayout_97 = QtWidgets.QHBoxLayout(self.layoutWidget_89)
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_97.setObjectName("horizontalLayout_97")
        self.PixmapLabel_53 = PixmapLabel(self.layoutWidget_89)
        self.PixmapLabel_53.setMinimumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_53.setMaximumSize(QtCore.QSize(24, 24))
        self.PixmapLabel_53.setObjectName("PixmapLabel_53")
        self.horizontalLayout_97.addWidget(self.PixmapLabel_53)
        self.CheckBox_B35 = CheckBox(self.layoutWidget_89)
        self.CheckBox_B35.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox_B35.setMaximumSize(QtCore.QSize(176, 32))
        self.CheckBox_B35.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
"")
        self.CheckBox_B35.setChecked(True)
        self.CheckBox_B35.setObjectName("CheckBox_B35")
        self.horizontalLayout_97.addWidget(self.CheckBox_B35)
        self.gridLayout_15.addWidget(self.CardWidget_47, 71, 1, 1, 1)
        self.HorizontalSeparator_79 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_79.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_79.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_79.setObjectName("HorizontalSeparator_79")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_79, 80, 3, 1, 1)
        self.gridLayout_49 = QtWidgets.QGridLayout()
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.CardWidget_285 = CardWidget(self.layoutWidget1)
        self.CardWidget_285.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_285.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_285.setObjectName("CardWidget_285")
        self.light_gray_terracotta = CheckBox(self.CardWidget_285)
        self.light_gray_terracotta.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.light_gray_terracotta.setMinimumSize(QtCore.QSize(17, 16))
        self.light_gray_terracotta.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.light_gray_terracotta.setFont(font)
        self.light_gray_terracotta.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon144 = QtGui.QIcon()
        icon144.addPixmap(QtGui.QPixmap("icon/light_gray_terracotta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light_gray_terracotta.setIcon(icon144)
        self.light_gray_terracotta.setIconSize(QtCore.QSize(16, 16))
        self.light_gray_terracotta.setChecked(True)
        self.light_gray_terracotta.setTristate(False)
        self.light_gray_terracotta.setObjectName("light_gray_terracotta")
        self.gridLayout_49.addWidget(self.CardWidget_285, 1, 0, 1, 1)
        spacerItem196 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_49.addItem(spacerItem196, 2, 1, 1, 1)
        spacerItem197 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_49.addItem(spacerItem197, 0, 1, 1, 1)
        self.CardWidget_286 = CardWidget(self.layoutWidget1)
        self.CardWidget_286.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_286.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_286.setObjectName("CardWidget_286")
        self.waxed_exposed_copper = CheckBox(self.CardWidget_286)
        self.waxed_exposed_copper.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.waxed_exposed_copper.setMinimumSize(QtCore.QSize(17, 16))
        self.waxed_exposed_copper.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.waxed_exposed_copper.setFont(font)
        self.waxed_exposed_copper.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon145 = QtGui.QIcon()
        icon145.addPixmap(QtGui.QPixmap("icon/waxed_exposed_copper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.waxed_exposed_copper.setIcon(icon145)
        self.waxed_exposed_copper.setIconSize(QtCore.QSize(16, 16))
        self.waxed_exposed_copper.setTristate(False)
        self.waxed_exposed_copper.setObjectName("waxed_exposed_copper")
        self.gridLayout_49.addWidget(self.CardWidget_286, 1, 1, 1, 1)
        self.CardWidget_287 = CardWidget(self.layoutWidget1)
        self.CardWidget_287.setMinimumSize(QtCore.QSize(128, 16))
        self.CardWidget_287.setMaximumSize(QtCore.QSize(100, 16))
        self.CardWidget_287.setObjectName("CardWidget_287")
        self.mud_bricks = CheckBox(self.CardWidget_287)
        self.mud_bricks.setGeometry(QtCore.QRect(0, 0, 128, 16))
        self.mud_bricks.setMinimumSize(QtCore.QSize(17, 16))
        self.mud_bricks.setMaximumSize(QtCore.QSize(128, 16))
        font = QtGui.QFont()
        font.setFamily("萝莉体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mud_bricks.setFont(font)
        self.mud_bricks.setStyleSheet("CheckBox {\n"
"    color: black;\n"
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
        icon146 = QtGui.QIcon()
        icon146.addPixmap(QtGui.QPixmap("icon/mud_bricks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mud_bricks.setIcon(icon146)
        self.mud_bricks.setIconSize(QtCore.QSize(16, 16))
        self.mud_bricks.setTristate(False)
        self.mud_bricks.setObjectName("mud_bricks")
        self.gridLayout_49.addWidget(self.CardWidget_287, 1, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_49, 89, 3, 1, 1)
        self.HorizontalSeparator_106 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_106.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_106.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_106.setObjectName("HorizontalSeparator_106")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_106, 108, 1, 1, 1)
        self.VerticalSeparator_56 = VerticalSeparator(self.layoutWidget1)
        self.VerticalSeparator_56.setMinimumSize(QtCore.QSize(4, 0))
        self.VerticalSeparator_56.setMaximumSize(QtCore.QSize(4, 16777215))
        self.VerticalSeparator_56.setObjectName("VerticalSeparator_56")
        self.gridLayout_15.addWidget(self.VerticalSeparator_56, 13, 2, 1, 1)
        self.HorizontalSeparator_9 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_9.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_9.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_9.setObjectName("HorizontalSeparator_9")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_9, 10, 1, 1, 1)
        self.HorizontalSeparator_125 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_125.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_125.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_125.setObjectName("HorizontalSeparator_125")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_125, 0, 1, 1, 1)
        self.HorizontalSeparator_126 = HorizontalSeparator(self.layoutWidget1)
        self.HorizontalSeparator_126.setMinimumSize(QtCore.QSize(0, 4))
        self.HorizontalSeparator_126.setMaximumSize(QtCore.QSize(16777215, 4))
        self.HorizontalSeparator_126.setObjectName("HorizontalSeparator_126")
        self.gridLayout_15.addWidget(self.HorizontalSeparator_126, 0, 3, 1, 1)
        self.SingleDirectionScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.SingleDirectionScrollArea)

        self.retranslateUi(Bui)
        self.CheckBox_B0.toggled['bool'].connect(self.glass.setChecked)  # type: ignore
        self.CheckBox_B1.toggled['bool'].connect(self.grass_block.setChecked)  # type: ignore
        self.CheckBox_B1.toggled['bool'].connect(self.slime_block.setChecked)  # type: ignore
        self.CheckBox_B2.toggled['bool'].connect(self.birch_planks.setChecked)  # type: ignore
        self.CheckBox_B2.toggled['bool'].connect(self.smooth_sandstone.setChecked)  # type: ignore
        self.CheckBox_B2.toggled['bool'].connect(self.glowstone.setChecked)  # type: ignore
        self.CheckBox_B2.toggled['bool'].connect(self.end_stone.setChecked)  # type: ignore
        self.CheckBox_B2.toggled['bool'].connect(self.ochre_froglight_top.setChecked)  # type: ignore
        self.CheckBox_B3.toggled['bool'].connect(self.mushroom_stem.setChecked)  # type: ignore
        self.CheckBox_B4.toggled['bool'].connect(self.redstone_block.setChecked)  # type: ignore
        self.CheckBox_B5.toggled['bool'].connect(self.ice.setChecked)  # type: ignore
        self.CheckBox_B5.toggled['bool'].connect(self.blue_ice.setChecked)  # type: ignore
        self.CheckBox_B6.toggled['bool'].connect(self.iron_block.setChecked)  # type: ignore
        self.CheckBox_B7.toggled['bool'].connect(self.oak_leaves.setChecked)  # type: ignore
        self.CheckBox_B8.toggled['bool'].connect(self.white_concrete.setChecked)  # type: ignore
        self.CheckBox_B8.toggled['bool'].connect(self.white_wool.setChecked)  # type: ignore
        self.CheckBox_B8.toggled['bool'].connect(self.white_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B8.toggled['bool'].connect(self.snow_block.setChecked)  # type: ignore
        self.CheckBox_B9.toggled['bool'].connect(self.clay.setChecked)  # type: ignore
        self.CheckBox_B10.toggled['bool'].connect(self.coarse_dirt.setChecked)  # type: ignore
        self.CheckBox_B10.toggled['bool'].connect(self.polished_granite.setChecked)  # type: ignore
        self.CheckBox_B10.toggled['bool'].connect(self.jungle_planks.setChecked)  # type: ignore
        self.CheckBox_B10.toggled['bool'].connect(self.brown_mushroom_block.setChecked)  # type: ignore
        self.CheckBox_B10.toggled['bool'].connect(self.dirt.setChecked)  # type: ignore
        self.CheckBox_B10.toggled['bool'].connect(self.packed_mud.setChecked)  # type: ignore
        self.CheckBox_B11.toggled['bool'].connect(self.polished_andesite.setChecked)  # type: ignore
        self.CheckBox_B11.toggled['bool'].connect(self.smooth_stone.setChecked)  # type: ignore
        self.CheckBox_B12.toggled['bool'].connect(self.water.setChecked)  # type: ignore
        self.CheckBox_B13.toggled['bool'].connect(self.oak_planks.setChecked)  # type: ignore
        self.CheckBox_B14.toggled['bool'].connect(self.quartz_block.setChecked)  # type: ignore
        self.CheckBox_B14.toggled['bool'].connect(self.sea_lantern.setChecked)  # type: ignore
        self.CheckBox_B14.toggled['bool'].connect(self.target.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.orange_concrete.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.orange_wool.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.orange_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.acacia_planks.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.pumpkin.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.terracotta.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.smooth_red_sandstone.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.honeycomb_block.setChecked)  # type: ignore
        self.CheckBox_B15.toggled['bool'].connect(self.waxed_copper_block.setChecked)  # type: ignore
        self.CheckBox_B16.toggled['bool'].connect(self.magenta_concrete.setChecked)  # type: ignore
        self.CheckBox_B16.toggled['bool'].connect(self.magenta_wool.setChecked)  # type: ignore
        self.CheckBox_B16.toggled['bool'].connect(self.magenta_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B16.toggled['bool'].connect(self.purpur_block.setChecked)  # type: ignore
        self.CheckBox_B17.toggled['bool'].connect(self.light_blue_concrete.setChecked)  # type: ignore
        self.CheckBox_B17.toggled['bool'].connect(self.light_blue_wool.setChecked)  # type: ignore
        self.CheckBox_B17.toggled['bool'].connect(self.light_blue_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B18.toggled['bool'].connect(self.yellow_concrete.setChecked)  # type: ignore
        self.CheckBox_B18.toggled['bool'].connect(self.yellow_wool.setChecked)  # type: ignore
        self.CheckBox_B18.toggled['bool'].connect(self.yellow_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B18.toggled['bool'].connect(self.hay_block.setChecked)  # type: ignore
        self.CheckBox_B18.toggled['bool'].connect(self.bamboo_planks.setChecked)  # type: ignore
        self.CheckBox_B19.toggled['bool'].connect(self.lime_concrete.setChecked)  # type: ignore
        self.CheckBox_B19.toggled['bool'].connect(self.lime_wool.setChecked)  # type: ignore
        self.CheckBox_B19.toggled['bool'].connect(self.lime_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B20.toggled['bool'].connect(self.pink_concrete.setChecked)  # type: ignore
        self.CheckBox_B20.toggled['bool'].connect(self.pink_wool.setChecked)  # type: ignore
        self.CheckBox_B20.toggled['bool'].connect(self.pink_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B20.toggled['bool'].connect(self.pearlescent_froglight_top.setChecked)  # type: ignore
        self.CheckBox_B21.toggled['bool'].connect(self.gray_concrete.setChecked)  # type: ignore
        self.CheckBox_B21.toggled['bool'].connect(self.gray_wool.setChecked)  # type: ignore
        self.CheckBox_B21.toggled['bool'].connect(self.gray_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B21.toggled['bool'].connect(self.tinted_glass.setChecked)  # type: ignore
        self.CheckBox_B22.toggled['bool'].connect(self.light_gray_concrete.setChecked)  # type: ignore
        self.CheckBox_B22.toggled['bool'].connect(self.light_gray_wool.setChecked)  # type: ignore
        self.CheckBox_B22.toggled['bool'].connect(self.light_gray_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B23.toggled['bool'].connect(self.cyan_concrete.setChecked)  # type: ignore
        self.CheckBox_B23.toggled['bool'].connect(self.cyan_wool.setChecked)  # type: ignore
        self.CheckBox_B23.toggled['bool'].connect(self.cyan_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B23.toggled['bool'].connect(self.prismarine.setChecked)  # type: ignore
        self.CheckBox_B24.toggled['bool'].connect(self.purple_concrete.setChecked)  # type: ignore
        self.CheckBox_B24.toggled['bool'].connect(self.purple_wool.setChecked)  # type: ignore
        self.CheckBox_B24.toggled['bool'].connect(self.purple_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B24.toggled['bool'].connect(self.amethyst_block.setChecked)  # type: ignore
        self.CheckBox_B25.toggled['bool'].connect(self.blue_concrete.setChecked)  # type: ignore
        self.CheckBox_B25.toggled['bool'].connect(self.blue_wool.setChecked)  # type: ignore
        self.CheckBox_B25.toggled['bool'].connect(self.blue_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B26.toggled['bool'].connect(self.brown_concrete.setChecked)  # type: ignore
        self.CheckBox_B26.toggled['bool'].connect(self.brown_wool.setChecked)  # type: ignore
        self.CheckBox_B26.toggled['bool'].connect(self.brown_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B26.toggled['bool'].connect(self.dark_oak_planks.setChecked)  # type: ignore
        self.CheckBox_B26.toggled['bool'].connect(self.soul_soil.setChecked)  # type: ignore
        self.CheckBox_B27.toggled['bool'].connect(self.green_concrete.setChecked)  # type: ignore
        self.CheckBox_B27.toggled['bool'].connect(self.green_wool.setChecked)  # type: ignore
        self.CheckBox_B27.toggled['bool'].connect(self.green_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B27.toggled['bool'].connect(self.dried_kelp_block.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.red_concrete.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.red_wool.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.red_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.bricks.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.red_mushroom_block.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.nether_wart_block.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.shroomlight.setChecked)  # type: ignore
        self.CheckBox_B28.toggled['bool'].connect(self.mangrove_planks.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.black_concrete.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.black_wool.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.black_stained_glass.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.obsidian.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.coal_block.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.polished_basalt.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.polished_blackstone.setChecked)  # type: ignore
        self.CheckBox_B29.toggled['bool'].connect(self.sculk.setChecked)  # type: ignore
        self.CheckBox_B30.toggled['bool'].connect(self.gold_block.setChecked)  # type: ignore
        self.CheckBox_B31.toggled['bool'].connect(self.diamond_block.setChecked)  # type: ignore
        self.CheckBox_B31.toggled['bool'].connect(self.prismarine_bricks.setChecked)  # type: ignore
        self.CheckBox_B32.toggled['bool'].connect(self.lapis_block.setChecked)  # type: ignore
        self.CheckBox_B33.toggled['bool'].connect(self.emerald_block.setChecked)  # type: ignore
        self.CheckBox_B34.toggled['bool'].connect(self.podzol.setChecked)  # type: ignore
        self.CheckBox_B34.toggled['bool'].connect(self.spruce_planks.setChecked)  # type: ignore
        self.CheckBox_B35.toggled['bool'].connect(self.netherrack.setChecked)  # type: ignore
        self.CheckBox_B35.toggled['bool'].connect(self.nether_bricks.setChecked)  # type: ignore
        self.CheckBox_B35.toggled['bool'].connect(self.magma_block.setChecked)  # type: ignore
        self.CheckBox_B36.toggled['bool'].connect(self.white_terracotta.setChecked)  # type: ignore
        self.CheckBox_B36.toggled['bool'].connect(self.calcite.setChecked)  # type: ignore
        self.CheckBox_B36.toggled['bool'].connect(self.cherry_planks.setChecked)  # type: ignore
        self.CheckBox_B37.toggled['bool'].connect(self.orange_terracotta.setChecked)  # type: ignore
        self.CheckBox_B38.toggled['bool'].connect(self.magenta_terracotta.setChecked)  # type: ignore
        self.CheckBox_B39.toggled['bool'].connect(self.light_blue_terracotta.setChecked)  # type: ignore
        self.CheckBox_B40.toggled['bool'].connect(self.yellow_terracotta.setChecked)  # type: ignore
        self.CheckBox_B41.toggled['bool'].connect(self.lime_terracotta.setChecked)  # type: ignore
        self.CheckBox_B42.toggled['bool'].connect(self.pink_terracotta.setChecked)  # type: ignore
        self.CheckBox_B42.toggled['bool'].connect(self.stripped_cherry_log.setChecked)  # type: ignore
        self.CheckBox_B43.toggled['bool'].connect(self.gray_terracotta.setChecked)  # type: ignore
        self.CheckBox_B44.toggled['bool'].connect(self.light_gray_terracotta.setChecked)  # type: ignore
        self.CheckBox_B44.toggled['bool'].connect(self.waxed_exposed_copper.setChecked)  # type: ignore
        self.CheckBox_B44.toggled['bool'].connect(self.mud_bricks.setChecked)  # type: ignore
        self.CheckBox_B45.toggled['bool'].connect(self.cyan_terracotta.setChecked)  # type: ignore
        self.CheckBox_B45.toggled['bool'].connect(self.mud.setChecked)  # type: ignore
        self.CheckBox_B46.toggled['bool'].connect(self.purple_terracotta.setChecked)  # type: ignore
        self.CheckBox_B47.toggled['bool'].connect(self.blue_terracotta.setChecked)  # type: ignore
        self.CheckBox_B48.toggled['bool'].connect(self.brown_terracotta.setChecked)  # type: ignore
        self.CheckBox_B49.toggled['bool'].connect(self.green_terracotta.setChecked)  # type: ignore
        self.CheckBox_B50.toggled['bool'].connect(self.red_terracotta.setChecked)  # type: ignore
        self.CheckBox_B51.toggled['bool'].connect(self.black_terracotta.setChecked)  # type: ignore
        self.CheckBox_B52.toggled['bool'].connect(self.crimson_nylium.setChecked)  # type: ignore
        self.CheckBox_B53.toggled['bool'].connect(self.stripped_crimson_stem.setChecked)  # type: ignore
        self.CheckBox_B54.toggled['bool'].connect(self.stripped_crimson_hyphae.setChecked)  # type: ignore
        self.CheckBox_B55.toggled['bool'].connect(self.warped_nylium.setChecked)  # type: ignore
        self.CheckBox_B55.toggled['bool'].connect(self.waxed_oxidized_copper.setChecked)  # type: ignore
        self.CheckBox_B56.toggled['bool'].connect(self.stripped_warped_stem.setChecked)  # type: ignore
        self.CheckBox_B56.toggled['bool'].connect(self.waxed_weathered_copper.setChecked)  # type: ignore
        self.CheckBox_B57.toggled['bool'].connect(self.stripped_warped_hyphae.setChecked)  # type: ignore
        self.CheckBox_B58.toggled['bool'].connect(self.warped_wart_block.setChecked)  # type: ignore
        self.CheckBox_B59.toggled['bool'].connect(self.deepslate.setChecked)  # type: ignore
        self.CheckBox_B60.toggled['bool'].connect(self.raw_iron_block.setChecked)  # type: ignore
        self.CheckBox_B61.toggled['bool'].connect(self.verdant_froglight_top.setChecked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Bui)

    def retranslateUi(self, Bui):
        _translate = QtCore.QCoreApplication.translate
        Bui.setWindowTitle(_translate("Bui", "Form"))
        self.TitleLabel.setText(_translate("Bui", "选择地图画色卡"))
        self.BodyLabel.setText(_translate("Bui", "地图像素画的核心就是利用少量的不均匀的色卡来还原作品，以下你将指定使用的色卡："))
        self.PushButton.setText(_translate("Bui", "NEXT →"))
        self.CaptionLabel.setText(_translate("Bui", "说明：B0. NONE 是必选项，作为透明方块和整体的填充； B7. PLANT 是关于植物的，下面会有一个方块衬托； B12. WATER 是关于水的，以深度作为变体的指标，下面会\n"
"           挖空水柱；如选择多种方块作为颜色的载体则随机选择方块与结构中； 如选择基色而未选择方块则不视为选择基色。"))
        self.black_terracotta.setText(_translate("Bui", "黑色陶瓦"))
        self.PixmapLabel_60.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#703637;\">█</span><span style=\" font-size:6pt; color:#8A4243;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#A04D4E;\">█</span><span style=\" font-size:6pt; color:#542829;\">█</span></p></body></html>"))
        self.CheckBox_B42.setText(_translate("Bui", "B42. TERRACOTTA_PINK"))
        self.PixmapLabel_52.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#5B3C22;\">█</span><span style=\" font-size:6pt; color:#6F4A2A;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#815631;\">█</span><span style=\" font-size:6pt; color:#442D19;\">█</span></p></body></html>"))
        self.CheckBox_B34.setText(_translate("Bui", "B34. PODZOL"))
        self.PixmapLabel_66.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#352318;\">█</span><span style=\" font-size:6pt; color:#412B1E;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4C3223;\">█</span><span style=\" font-size:6pt; color:#281A12;\">█</span></p></body></html>"))
        self.CheckBox_B48.setText(_translate("Bui", "B48. TERRACOTTA_BROWN"))
        self.PixmapLabel_43.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#24357D;\">█</span><span style=\" font-size:6pt; color:#2C4199;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#334CB2;\">█</span><span style=\" font-size:6pt; color:#1B285E;\">█</span></p></body></html>"))
        self.CheckBox_B25.setText(_translate("Bui", "B25. COLOR_BLUE"))
        self.light_blue_concrete.setText(_translate("Bui", "淡蓝色混凝土"))
        self.light_blue_wool.setText(_translate("Bui", "淡蓝色羊毛"))
        self.light_blue_stained_glass.setText(_translate("Bui", "淡蓝色染色玻璃"))
        self.spruce_planks.setText(_translate("Bui", "云杉木板"))
        self.podzol.setText(_translate("Bui", "灰化土"))
        self.crimson_nylium.setText(_translate("Bui", "绯红菌岩"))
        self.cyan_concrete.setText(_translate("Bui", "青色混凝土"))
        self.cyan_stained_glass.setText(_translate("Bui", "青色染色玻璃"))
        self.prismarine.setText(_translate("Bui", "海晶石"))
        self.cyan_wool.setText(_translate("Bui", "青色羊毛"))
        self.magenta_terracotta.setText(_translate("Bui", "品红色陶瓦"))
        self.stripped_crimson_hyphae.setText(_translate("Bui", "去皮绯红菌核"))
        self.green_concrete.setText(_translate("Bui", "绿色混凝土"))
        self.green_stained_glass.setText(_translate("Bui", "绿色染色玻璃"))
        self.dried_kelp_block.setText(_translate("Bui", "海带块"))
        self.green_wool.setText(_translate("Bui", "绿色羊毛"))
        self.PixmapLabel_30.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#2D2DB4;\">█</span><span style=\" font-size:6pt; color:#3737DC;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4040FF;\">█</span><span style=\" font-size:6pt; color:#212187;\">█</span></p></body></html>"))
        self.CheckBox_B12.setText(_translate("Bui", "B12. WATER"))
        self.PixmapLabel_46.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#6C2424;\">█</span><span style=\" font-size:6pt; color:#842C2C;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#993333;\">█</span><span style=\" font-size:6pt; color:#511B1B;\">█</span></p></body></html>"))
        self.CheckBox_B28.setText(_translate("Bui", "B28. COLOR_RED"))
        self.PixmapLabel_44.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#483524;\">█</span><span style=\" font-size:6pt; color:#58412C;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#664C33;\">█</span><span style=\" font-size:6pt; color:#36281B;\">█</span></p></body></html>"))
        self.CheckBox_B26.setText(_translate("Bui", "B26. COLOR_BROWN"))
        self.PixmapLabel_54.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#937C71;\">█</span><span style=\" font-size:6pt; color:#B4988A;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#D1B1A1;\">█</span><span style=\" font-size:6pt; color:#6E5D55;\">█</span></p></body></html>"))
        self.CheckBox_B36.setText(_translate("Bui", "B36. TERRACOTTA_WHITE"))
        self.PixmapLabel_33.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#985924;\">█</span><span style=\" font-size:6pt; color:#BA6D2C;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#D87F33;\">█</span><span style=\" font-size:6pt; color:#72431B;\">█</span></p></body></html>"))
        self.CheckBox_B15.setText(_translate("Bui", "B15. COLOR_ORANGE"))
        self.PixmapLabel_45.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#485924;\">█</span><span style=\" font-size:6pt; color:#586D2C;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#667F33;\">█</span><span style=\" font-size:6pt; color:#36431B;\">█</span></p></body></html>"))
        self.CheckBox_B27.setText(_translate("Bui", "B27. COLOR_GREEN"))
        self.PixmapLabel_69.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#1A0F0B;\">█</span><span style=\" font-size:6pt; color:#1F120D;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#251610;\">█</span><span style=\" font-size:6pt; color:#130B08;\">█</span></p></body></html>"))
        self.CheckBox_B51.setText(_translate("Bui", "B51. TERRACOTTA_BLACK"))
        self.PixmapLabel_63.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#3D4040;\">█</span><span style=\" font-size:6pt; color:#4B4F4F;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#575C5C;\">█</span><span style=\" font-size:6pt; color:#2E3030;\">█</span></p></body></html>"))
        self.CheckBox_B45.setText(_translate("Bui", "B45. TERRACOTTA_CYAN"))
        self.red_concrete.setText(_translate("Bui", "红色混凝土"))
        self.red_wool.setText(_translate("Bui", "红色羊毛"))
        self.red_stained_glass.setText(_translate("Bui", "红色染色玻璃"))
        self.bricks.setText(_translate("Bui", "红砖块"))
        self.red_mushroom_block.setText(_translate("Bui", "红色蘑菇方块"))
        self.nether_wart_block.setText(_translate("Bui", "下界疣块"))
        self.shroomlight.setText(_translate("Bui", "菌光体"))
        self.mangrove_planks.setText(_translate("Bui", "红树木板"))
        self.mushroom_stem.setText(_translate("Bui", "蘑菇柄"))
        self.lapis_block.setText(_translate("Bui", "青金石块"))
        self.brown_concrete.setText(_translate("Bui", "棕色混凝土"))
        self.brown_wool.setText(_translate("Bui", "棕色羊毛"))
        self.brown_stained_glass.setText(_translate("Bui", "棕色染色玻璃"))
        self.dark_oak_planks.setText(_translate("Bui", "深色橡木木板"))
        self.soul_soil.setText(_translate("Bui", "灵魂土"))
        self.yellow_concrete.setText(_translate("Bui", "黄色混凝土"))
        self.yellow_wool.setText(_translate("Bui", "黄色羊毛"))
        self.yellow_stained_glass.setText(_translate("Bui", "黄色染色玻璃"))
        self.hay_block.setText(_translate("Bui", "干草捆"))
        self.bamboo_planks.setText(_translate("Bui", "竹板"))
        self.PixmapLabel_37.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#599011;\">█</span><span style=\" font-size:6pt; color:#6DB015;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#7FCC19;\">█</span><span style=\" font-size:6pt; color:#436C0D;\">█</span></p></body></html>"))
        self.CheckBox_B19.setText(_translate("Bui", "B19. COLOR_LIGHT_GREEN"))
        self.verdant_froglight_top.setText(_translate("Bui", "青翠蛙明灯"))
        self.gold_block.setText(_translate("Bui", "金块"))
        self.PixmapLabel_50.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#345AB4;\">█</span><span style=\" font-size:6pt; color:#3F6EDC;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4A80FF;\">█</span><span style=\" font-size:6pt; color:#274387;\">█</span></p></body></html>"))
        self.CheckBox_B32.setText(_translate("Bui", "B32. LAPIS"))
        self.PixmapLabel_41.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#35596C;\">█</span><span style=\" font-size:6pt; color:#416D84;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4C7F99;\">█</span><span style=\" font-size:6pt; color:#284351;\">█</span></p></body></html>"))
        self.CheckBox_B23.setText(_translate("Bui", "B23. COLOR_CYAN"))
        self.purple_terracotta.setText(_translate("Bui", "紫色陶瓦"))
        self.blue_concrete.setText(_translate("Bui", "蓝色混凝土"))
        self.blue_wool.setText(_translate("Bui", "蓝色羊毛"))
        self.blue_stained_glass.setText(_translate("Bui", "蓝色染色玻璃"))
        self.clay.setText(_translate("Bui", "黏土块"))
        self.white_concrete.setText(_translate("Bui", "白色混凝土"))
        self.white_stained_glass.setText(_translate("Bui", "白色染色玻璃"))
        self.snow_block.setText(_translate("Bui", "雪块"))
        self.white_wool.setText(_translate("Bui", "白色羊毛"))
        self.PixmapLabel_72.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#401114;\">█</span><span style=\" font-size:6pt; color:#4F1519;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#5C191D;\">█</span><span style=\" font-size:6pt; color:#300D0F;\">█</span></p></body></html>"))
        self.CheckBox_B54.setText(_translate("Bui", "B54. CRIMSON_HYPHAE"))
        self.PixmapLabel_73.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#0F585E;\">█</span><span style=\" font-size:6pt; color:#126C73;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#167E86;\">█</span><span style=\" font-size:6pt; color:#0B4246;\">█</span></p></body></html>"))
        self.CheckBox_B55.setText(_translate("Bui", "B55. WARPED_NYLIUM"))
        self.PixmapLabel_67.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#35391D;\">█</span><span style=\" font-size:6pt; color:#414624;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4C522A;\">█</span><span style=\" font-size:6pt; color:#282B16;\">█</span></p></body></html>"))
        self.CheckBox_B49.setText(_translate("Bui", "B49. TERRACOTTA_GREEN"))
        self.quartz_block.setText(_translate("Bui", "石英块"))
        self.sea_lantern.setText(_translate("Bui", "海晶灯"))
        self.target.setText(_translate("Bui", "标靶"))
        self.glass.setText(_translate("Bui", "玻璃"))
        self.PixmapLabel_26.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#B4B4B4;\">█</span><span style=\" font-size:6pt; color:#DCDCDC;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#FFFFFF;\">█</span><span style=\" font-size:6pt; color:#878787;\">█</span></p></body></html>"))
        self.CheckBox_B8.setText(_translate("Bui", "B8. SNOW"))
        self.PixmapLabel_59.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#485225;\">█</span><span style=\" font-size:6pt; color:#58642D;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#677535;\">█</span><span style=\" font-size:6pt; color:#363D1C;\">█</span></p></body></html>"))
        self.CheckBox_B41.setText(_translate("Bui", "B41. TERRACOTTA_LIGHT_GREEN"))
        self.oak_planks.setText(_translate("Bui", "橡木木板"))
        self.purple_concrete.setText(_translate("Bui", "紫色混凝土"))
        self.purple_stained_glass.setText(_translate("Bui", "紫色染色玻璃"))
        self.amethyst_block.setText(_translate("Bui", "紫水晶块"))
        self.purple_wool.setText(_translate("Bui", "紫色羊毛"))
        self.raw_iron_block.setText(_translate("Bui", "粗铁块"))
        self.PixmapLabel_79.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#987B67;\">█</span><span style=\" font-size:6pt; color:#BA967E;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#D8AF93;\">█</span><span style=\" font-size:6pt; color:#725C4D;\">█</span></p></body></html>"))
        self.CheckBox_B60.setText(_translate("Bui", "B60. RAW_IRON"))
        self.PixmapLabel_61.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#281C18;\">█</span><span style=\" font-size:6pt; color:#31231E;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#392923;\">█</span><span style=\" font-size:6pt; color:#1E1512;\">█</span></p></body></html>"))
        self.CheckBox_B43.setText(_translate("Bui", "B43. TERRACOTTA_GRAY"))
        self.emerald_block.setText(_translate("Bui", "绿宝石块"))
        self.PixmapLabel_39.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#353535;\">█</span><span style=\" font-size:6pt; color:#414141;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4C4C4C;\">█</span><span style=\" font-size:6pt; color:#282828;\">█</span></p></body></html>"))
        self.CheckBox_B21.setText(_translate("Bui", "B21. COLOR_GRAY"))
        self.PixmapLabel_71.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#682C44;\">█</span><span style=\" font-size:6pt; color:#7F3653;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#943F61;\">█</span><span style=\" font-size:6pt; color:#4E2133;\">█</span></p></body></html>"))
        self.CheckBox_B53.setText(_translate("Bui", "B53. CRIMSON_STEM"))
        self.PixmapLabel_70.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#852122;\">█</span><span style=\" font-size:6pt; color:#A3292A;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#BD3031;\">█</span><span style=\" font-size:6pt; color:#641919;\">█</span></p></body></html>"))
        self.CheckBox_B52.setText(_translate("Bui", "B52. CRIMSON_NYLIUM"))
        self.PixmapLabel_75.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#3C1F2B;\">█</span><span style=\" font-size:6pt; color:#4A2535;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#562C3E;\">█</span><span style=\" font-size:6pt; color:#2D1720;\">█</span></p></body></html>"))
        self.CheckBox_B57.setText(_translate("Bui", "B57. WARPED_HYPHAE"))
        self.coarse_dirt.setText(_translate("Bui", "砂土"))
        self.jungle_planks.setText(_translate("Bui", "丛林木板"))
        self.brown_mushroom_block.setText(_translate("Bui", "棕色蘑菇方块"))
        self.dirt.setText(_translate("Bui", "泥土"))
        self.polished_granite.setText(_translate("Bui", "磨制花岗岩"))
        self.packed_mud.setText(_translate("Bui", "泥坯"))
        self.warped_wart_block.setText(_translate("Bui", "诡异疣块"))
        self.blue_terracotta.setText(_translate("Bui", "蓝色陶瓦"))
        self.red_terracotta.setText(_translate("Bui", "红色陶瓦"))
        self.netherrack.setText(_translate("Bui", "下界岩"))
        self.nether_bricks.setText(_translate("Bui", "下界砖块"))
        self.magma_block.setText(_translate("Bui", "岩浆块"))
        self.pink_concrete.setText(_translate("Bui", "粉红色混凝土"))
        self.pink_stained_glass.setText(_translate("Bui", "粉红色染色玻璃"))
        self.pearlescent_froglight_top.setText(_translate("Bui", "珠光蛙明灯"))
        self.pink_wool.setText(_translate("Bui", "粉红色羊毛"))
        self.redstone_block.setText(_translate("Bui", "红石块"))
        self.PixmapLabel_51.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#009928;\">█</span><span style=\" font-size:6pt; color:#00BB32;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#00D93A;\">█</span><span style=\" font-size:6pt; color:#00721E;\">█</span></p></body></html>"))
        self.CheckBox_B33.setText(_translate("Bui", "B33. EMERALD"))
        self.orange_terracotta.setText(_translate("Bui", "橙色陶瓦"))
        self.mud.setText(_translate("Bui", "泥巴"))
        self.cyan_terracotta.setText(_translate("Bui", "青色陶瓦"))
        self.PixmapLabel_55.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#703919;\">█</span><span style=\" font-size:6pt; color:#89461F;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#9F5224;\">█</span><span style=\" font-size:6pt; color:#542B13;\">█</span></p></body></html>"))
        self.CheckBox_B37.setText(_translate("Bui", "B37. TERRACOTTA_ORANGE"))
        self.PixmapLabel_57.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4F4C61;\">█</span><span style=\" font-size:6pt; color:#605D77;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#706C8A;\">█</span><span style=\" font-size:6pt; color:#3B3949;\">█</span></p></body></html>"))
        self.CheckBox_B39.setText(_translate("Bui", "B39. TERRACOTTA_LIGHT_BLUE"))
        self.green_terracotta.setText(_translate("Bui", "绿色陶瓦"))
        self.PixmapLabel_80.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#597569;\">█</span><span style=\" font-size:6pt; color:#6D9081;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#7FA796;\">█</span><span style=\" font-size:6pt; color:#43584F;\">█</span></p></body></html>"))
        self.CheckBox_B61.setText(_translate("Bui", "B61. GLOW_LICHEN"))
        self.PixmapLabel_21.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#005700;\">█</span><span style=\" font-size:6pt; color:#006A00;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#007C00;\">█</span><span style=\" font-size:6pt; color:#004100;\">█</span></p></body></html>"))
        self.CheckBox_B7.setText(_translate("Bui", "B7. PLANT"))
        self.stripped_warped_hyphae.setText(_translate("Bui", "去皮诡异菌核"))
        self.brown_terracotta.setText(_translate("Bui", "棕色陶瓦"))
        self.PixmapLabel_77.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#0E7F5D;\">█</span><span style=\" font-size:6pt; color:#119B72;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#14B485;\">█</span><span style=\" font-size:6pt; color:#0A5F46;\">█</span></p></body></html>"))
        self.CheckBox_B58.setText(_translate("Bui", "B58. WARPED_WART_BLOCK"))
        self.magenta_concrete.setText(_translate("Bui", "品红色混凝土"))
        self.magenta_stained_glass.setText(_translate("Bui", "品红色染色玻璃"))
        self.purpur_block.setText(_translate("Bui", "紫珀块"))
        self.magenta_wool.setText(_translate("Bui", "品红色羊毛"))
        self.lime_terracotta.setText(_translate("Bui", "黄绿色陶瓦"))
        self.water.setText(_translate("Bui", "水"))
        self.black_concrete.setText(_translate("Bui", "黑色混凝土"))
        self.black_wool.setText(_translate("Bui", "黑色羊毛"))
        self.black_stained_glass.setText(_translate("Bui", "黑色染色玻璃"))
        self.obsidian.setText(_translate("Bui", "黑曜石"))
        self.coal_block.setText(_translate("Bui", "煤炭块"))
        self.polished_basalt.setText(_translate("Bui", "磨制玄武岩"))
        self.polished_blackstone.setText(_translate("Bui", "磨制黑石"))
        self.sculk.setText(_translate("Bui", "幽匿块"))
        self.waxed_copper_block.setText(_translate("Bui", "涂蜡铜块"))
        self.smooth_red_sandstone.setText(_translate("Bui", "平滑红砂岩"))
        self.orange_wool.setText(_translate("Bui", "橙色羊毛"))
        self.acacia_planks.setText(_translate("Bui", "金合欢木板"))
        self.terracotta.setText(_translate("Bui", "陶瓦"))
        self.orange_stained_glass.setText(_translate("Bui", "橙色染色玻璃"))
        self.honeycomb_block.setText(_translate("Bui", "蜜脾块"))
        self.orange_concrete.setText(_translate("Bui", "橙色混凝土"))
        self.pumpkin.setText(_translate("Bui", "南瓜"))
        self.PixmapLabel_68.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#642A20;\">█</span><span style=\" font-size:6pt; color:#7A3327;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#8E3C2E;\">█</span><span style=\" font-size:6pt; color:#4B1F18;\">█</span></p></body></html>"))
        self.CheckBox_B50.setText(_translate("Bui", "B50. TERRACOTTA_RED"))
        self.PixmapLabel_27.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#737681;\">█</span><span style=\" font-size:6pt; color:#8D909E;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#A4A8B8;\">█</span><span style=\" font-size:6pt; color:#565861;\">█</span></p></body></html>"))
        self.CheckBox_B9.setText(_translate("Bui", "B9. CLAY"))
        self.PixmapLabel_78.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#464646;\">█</span><span style=\" font-size:6pt; color:#565656;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#646464;\">█</span><span style=\" font-size:6pt; color:#343434;\">█</span></p></body></html>"))
        self.CheckBox_B59.setText(_translate("Bui", "B59.     DEEPSLATE"))
        self.waxed_weathered_copper.setText(_translate("Bui", "锈蚀的涂蜡铜块"))
        self.stripped_warped_stem.setText(_translate("Bui", "去皮诡异菌柄"))
        self.PixmapLabel_35.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#486C98;\">█</span><span style=\" font-size:6pt; color:#5884BA;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#6699D8;\">█</span><span style=\" font-size:6pt; color:#365172;\">█</span></p></body></html>"))
        self.CheckBox_B17.setText(_translate("Bui", "B17. COLOR_LIGHT_BLUE"))
        self.gray_concrete.setText(_translate("Bui", "灰色混凝土"))
        self.gray_stained_glass.setText(_translate("Bui", "灰色染色玻璃"))
        self.tinted_glass.setText(_translate("Bui", "遮光玻璃"))
        self.gray_wool.setText(_translate("Bui", "灰色羊毛"))
        self.PixmapLabel_64.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#56333E;\">█</span><span style=\" font-size:6pt; color:#693E4B;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#7A4958;\">█</span><span style=\" font-size:6pt; color:#40262E;\">█</span></p></body></html>"))
        self.CheckBox_B46.setText(_translate("Bui", "B46. TERRACOTTA_PURPLE"))
        self.PixmapLabel_14.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#000000;\">□</span><span style=\" font-size:6pt; color:#000000;\">□</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#000000;\">□</span><span style=\" font-size:6pt; color:#000000;\">□</span></p></body></html>"))
        self.CheckBox_B0.setText(_translate("Bui", "B0. NONE"))
        self.PixmapLabel_38.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#AA5974;\">█</span><span style=\" font-size:6pt; color:#D06D8E;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#F27FA5;\">█</span><span style=\" font-size:6pt; color:#804357;\">█</span></p></body></html>"))
        self.CheckBox_B20.setText(_translate("Bui", "B20. COLOR_PINK"))
        self.birch_planks.setText(_translate("Bui", "白桦木板"))
        self.smooth_sandstone.setText(_translate("Bui", "平滑砂岩"))
        self.glowstone.setText(_translate("Bui", "荧石"))
        self.end_stone.setText(_translate("Bui", "末地石"))
        self.ochre_froglight_top.setText(_translate("Bui", "赭黄蛙明灯"))
        self.deepslate.setText(_translate("Bui", "深板岩"))
        self.light_gray_concrete.setText(_translate("Bui", "淡灰色混凝土"))
        self.light_gray_wool.setText(_translate("Bui", "淡灰色羊毛"))
        self.light_gray_stained_glass.setText(_translate("Bui", "淡灰色染色玻璃"))
        self.PixmapLabel_20.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#757575;\">█</span><span style=\" font-size:6pt; color:#909090;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#A7A7A7;\">█</span><span style=\" font-size:6pt; color:#585858;\">█</span></p></body></html>"))
        self.CheckBox_B6.setText(_translate("Bui", "B6. METAL"))
        self.slime_block.setText(_translate("Bui", "黏液块"))
        self.grass_block.setText(_translate("Bui", "草方块"))
        self.stripped_crimson_stem.setText(_translate("Bui", "去皮绯红菌柄"))
        self.waxed_oxidized_copper.setText(_translate("Bui", "氧化的涂蜡铜块"))
        self.warped_nylium.setText(_translate("Bui", "诡异菌岩"))
        self.PixmapLabel_65.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#352B40;\">█</span><span style=\" font-size:6pt; color:#41354F;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4C3E5C;\">█</span><span style=\" font-size:6pt; color:#282030;\">█</span></p></body></html>"))
        self.CheckBox_B47.setText(_translate("Bui", "B47. TERRACOTTA_BLUE"))
        self.PixmapLabel_17.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#8C8C8C;\">█</span><span style=\" font-size:6pt; color:#ABABAB;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#C7C7C7;\">█</span><span style=\" font-size:6pt; color:#696969;\">█</span></p></body></html>"))
        self.CheckBox_B3.setText(_translate("Bui", "B3. WOOL"))
        self.lime_concrete.setText(_translate("Bui", "黄绿色混凝土"))
        self.lime_wool.setText(_translate("Bui", "黄绿色羊毛"))
        self.lime_stained_glass.setText(_translate("Bui", "黄绿色染色玻璃"))
        self.PixmapLabel_19.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#7070B4;\">█</span><span style=\" font-size:6pt; color:#8A8ADC;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#A0A0FF;\">█</span><span style=\" font-size:6pt; color:#545487;\">█</span></p></body></html>"))
        self.CheckBox_B5.setText(_translate("Bui", "B5. ICE"))
        self.gray_terracotta.setText(_translate("Bui", "灰色陶瓦"))
        self.PixmapLabel_40.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#6C6C6C;\">█</span><span style=\" font-size:6pt; color:#848484;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#999999;\">█</span><span style=\" font-size:6pt; color:#515151;\">█</span></p></body></html>"))
        self.CheckBox_B22.setText(_translate("Bui", "B22. COLOR_LIGHT_GRAY"))
        self.PixmapLabel_42.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#592C7D;\">█</span><span style=\" font-size:6pt; color:#6D3699;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#7F3FB2;\">█</span><span style=\" font-size:6pt; color:#43215E;\">█</span></p></body></html>"))
        self.CheckBox_B24.setText(_translate("Bui", "B24. COLOR_PURPLE"))
        self.PixmapLabel_56.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#693D4C;\">█</span><span style=\" font-size:6pt; color:#804B5D;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#95576C;\">█</span><span style=\" font-size:6pt; color:#4E2E39;\">█</span></p></body></html>"))
        self.CheckBox_B38.setText(_translate("Bui", "B38. TERRACOTTA_MAGENTA"))
        self.PixmapLabel_74.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#286462;\">█</span><span style=\" font-size:6pt; color:#327A78;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#3A8E8C;\">█</span><span style=\" font-size:6pt; color:#1E4B4A;\">█</span></p></body></html>"))
        self.CheckBox_B56.setText(_translate("Bui", "B56. WARPED_STEM"))
        self.PixmapLabel_34.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#7D3598;\">█</span><span style=\" font-size:6pt; color:#9941BA;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#B24CD8;\">█</span><span style=\" font-size:6pt; color:#5E2872;\">█</span></p></body></html>"))
        self.CheckBox_B16.setText(_translate("Bui", "B16. COLOR_MAGENTA"))
        self.white_terracotta.setText(_translate("Bui", "白色陶瓦"))
        self.calcite.setText(_translate("Bui", "方解石"))
        self.cherry_planks.setText(_translate("Bui", "樱花木板"))
        self.PixmapLabel_49.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#409A96;\">█</span><span style=\" font-size:6pt; color:#4FBCB7;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#5CDBD5;\">█</span><span style=\" font-size:6pt; color:#307370;\">█</span></p></body></html>"))
        self.CheckBox_B31.setText(_translate("Bui", "B31. DIAMOND"))
        self.PixmapLabel_15.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#AEA473;\">█</span><span style=\" font-size:6pt; color:#D5C98C;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#F7E9A3;\">█</span><span style=\" font-size:6pt; color:#827B56;\">█</span></p></body></html>"))
        self.CheckBox_B2.setText(_translate("Bui", "B2. SAND"))
        self.PixmapLabel_47.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#111111;\">█</span><span style=\" font-size:6pt; color:#151515;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#191919;\">█</span><span style=\" font-size:6pt; color:#0D0D0D;\">█</span></p></body></html>"))
        self.CheckBox_B29.setText(_translate("Bui", "B29. COLOR_BLACK"))
        self.smooth_stone.setText(_translate("Bui", "平滑石头"))
        self.polished_andesite.setText(_translate("Bui", "磨制安山岩"))
        self.PixmapLabel_58.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#835D19;\">█</span><span style=\" font-size:6pt; color:#A0721F;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#BA8524;\">█</span><span style=\" font-size:6pt; color:#624613;\">█</span></p></body></html>"))
        self.CheckBox_B40.setText(_translate("Bui", "B40. TERRACOTTA_YELLOW"))
        self.PixmapLabel_31.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#645432;\">█</span><span style=\" font-size:6pt; color:#7B663E;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#8F7748;\">█</span><span style=\" font-size:6pt; color:#4B3F26;\">█</span></p></body></html>"))
        self.CheckBox_B13.setText(_translate("Bui", "B13. WOOD"))
        self.PixmapLabel_29.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4F4F4F;\">█</span><span style=\" font-size:6pt; color:#606060;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#707070;\">█</span><span style=\" font-size:6pt; color:#3B3B3B;\">█</span></p></body></html>"))
        self.CheckBox_B11.setText(_translate("Bui", "B11. STONE"))
        self.PixmapLabel_16.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#597D27;\">█</span><span style=\" font-size:6pt; color:#6D9930;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#7FB238;\">█</span><span style=\" font-size:6pt; color:#435E1D;\">█</span></p></body></html>"))
        self.CheckBox_B1.setText(_translate("Bui", "B1. GRASS"))
        self.prismarine_bricks.setText(_translate("Bui", "海晶石砖"))
        self.diamond_block.setText(_translate("Bui", "钻石块"))
        self.PixmapLabel_18.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#B40000;\">█</span><span style=\" font-size:6pt; color:#DC0000;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#FF0000;\">█</span><span style=\" font-size:6pt; color:#870000;\">█</span></p></body></html>"))
        self.CheckBox_B4.setText(_translate("Bui", "B4. FIRE"))
        self.stripped_cherry_log.setText(_translate("Bui", "去皮樱花木头"))
        self.pink_terracotta.setText(_translate("Bui", "粉红色陶瓦"))
        self.yellow_terracotta.setText(_translate("Bui", "黄色陶瓦"))
        self.blue_ice.setText(_translate("Bui", "蓝冰"))
        self.ice.setText(_translate("Bui", "冰"))
        self.PixmapLabel_32.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#B4B1AC;\">█</span><span style=\" font-size:6pt; color:#DCD9D3;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#FFFCF5;\">█</span><span style=\" font-size:6pt; color:#878581;\">█</span></p></body></html>"))
        self.CheckBox_B14.setText(_translate("Bui", "B14. QUARTZ"))
        self.oak_leaves.setText(_translate("Bui", "橡树树叶"))
        self.light_blue_terracotta.setText(_translate("Bui", "淡蓝色陶瓦"))
        self.PixmapLabel_36.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#A1A124;\">█</span><span style=\" font-size:6pt; color:#C5C52C;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#E5E533;\">█</span><span style=\" font-size:6pt; color:#79791B;\">█</span></p></body></html>"))
        self.CheckBox_B18.setText(_translate("Bui", "B18. COLOR_YELLOW"))
        self.PixmapLabel_62.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#5F4B45;\">█</span><span style=\" font-size:6pt; color:#745C54;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#876B62;\">█</span><span style=\" font-size:6pt; color:#473833;\">█</span></p></body></html>"))
        self.CheckBox_B44.setText(_translate("Bui", "B44. TERRACOTTA_LIGHT_GRAY"))
        self.PixmapLabel_28.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#6A4C36;\">█</span><span style=\" font-size:6pt; color:#825E42;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#976D4D;\">█</span><span style=\" font-size:6pt; color:#4F3928;\">█</span></p></body></html>"))
        self.CheckBox_B10.setText(_translate("Bui", "B10. DIRT"))
        self.iron_block.setText(_translate("Bui", "铁块"))
        self.PixmapLabel_48.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#B0A836;\">█</span><span style=\" font-size:6pt; color:#D7CD42;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#FAEE4D;\">█</span><span style=\" font-size:6pt; color:#847E28;\">█</span></p></body></html>"))
        self.CheckBox_B30.setText(_translate("Bui", "B30. GOLD"))
        self.PixmapLabel_53.setText(_translate("Bui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#4F0100;\">█</span><span style=\" font-size:6pt; color:#600100;\">█</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; letter-spacing: 1px;\"><span style=\" font-size:6pt; color:#700200;\">█</span><span style=\" font-size:6pt; color:#3B0100;\">█</span></p></body></html>"))
        self.CheckBox_B35.setText(_translate("Bui", "B35. NETHER"))
        self.light_gray_terracotta.setText(_translate("Bui", "淡灰色陶瓦"))
        self.waxed_exposed_copper.setText(_translate("Bui", "斑驳的涂蜡铜块"))
        self.mud_bricks.setText(_translate("Bui", "泥砖"))
from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, CheckBox, HorizontalSeparator, PixmapLabel, PushButton, SimpleCardWidget, SingleDirectionScrollArea, TitleLabel, VerticalSeparator
