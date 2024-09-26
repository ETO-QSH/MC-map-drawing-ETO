# coding:utf-8

from typing import List
from ETO.settings.config import *
from qfluentwidgets import (SettingCardGroup, SwitchSettingCard, FolderListSettingCard,
                            OptionsSettingCard, RangeSettingCard, PushSettingCard,
                            ColorSettingCard, HyperlinkCard, PrimaryPushSettingCard, ScrollArea,
                            ComboBoxSettingCard, ExpandLayout, Theme, InfoBar, CustomColorSettingCard,
                            setTheme, setThemeColor, isDarkTheme, FluentStyleSheet, setFont)
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QStandardPaths
from PyQt5.QtWidgets import QWidget, QLabel, QFontDialog, QFileDialog, QColorDialog, QVBoxLayout


class CustomSettingCardGroup(QWidget):
    def __init__(self, spacing: int, parent=None):
        super().__init__(parent=parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.cardLayout = ExpandLayout()

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setSpacing(0)
        self.cardLayout.setContentsMargins(0, 0, 0, 0)
        self.cardLayout.setSpacing(2)

        self.vBoxLayout.addSpacing(spacing)
        self.vBoxLayout.addLayout(self.cardLayout, 1)

        FluentStyleSheet.SETTING_CARD_GROUP.apply(self)

    def addSettingCard(self, card: QWidget):
        """ add setting card to group """
        card.setParent(self)
        self.cardLayout.addWidget(card)
        self.adjustSize()

    def addSettingCards(self, cards: List[QWidget]):
        """ add setting cards to group """
        for card in cards:
            self.addSettingCard(card)

    def adjustSize(self):
        h = self.cardLayout.heightForWidth(self.width()) + 0
        return self.resize(self.width(), h)

class SettingInterface(ScrollArea):
    """ Setting interface """
    checkUpdateSig = pyqtSignal()
    downloadFolderChanged = pyqtSignal(str)
    savesFolderChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.setting = parent

        self.personalGroup = CustomSettingCardGroup(0, self.scrollWidget)
        self.downloadFolderCard = PushSettingCard(
            self.tr('更改'),
            FIF.DOWNLOAD,
            self.tr("备份目录"),
            cfg.get(cfg.downloadFolder),
            self.personalGroup
        )
        self.savesFolderCard = PushSettingCard(
            self.tr('更改'),
            FIF.SAVE,
            self.tr("存档目录"),
            cfg.get(cfg.savesFolder),
            self.personalGroup
        )
        self.themeColorCard = PushSettingCard(
            self.tr('更改'),
            FIF.PALETTE,
            self.tr('主题颜色'),
            cfg.get(cfg.ThemeColor).name(),
            parent=self.personalGroup
        )
        self.themeCard = ComboBoxSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            self.tr('黑白主题'),
            self.tr('设置UI的主体风格'),
            texts=[self.tr('亮色主题'), self.tr('暗色主题'), self.tr('系统主题')],
            parent=self.personalGroup
        )
        self.zoomCard = ComboBoxSettingCard(
            cfg.dpiScale,
            FIF.ZOOM,
            self.tr('界面缩放'),
            self.tr('设置字体和窗口大小'),
            texts=["   100%   ", "   125%   ", "   150%   ", "   175%   ", "   200%   ", "   225%   ", self.tr("系统比例")],
            parent=self.personalGroup
        )
        self.languageCard = ComboBoxSettingCard(
            cfg.language,
            FIF.LANGUAGE,
            self.tr('操作语言'),
            self.tr('设置UI语言'),
            texts=['简体中文', '繁體中文', '散装英语', self.tr('系统语言')],
            parent=self.personalGroup
        )
        self.deskLyricFontCard = PushSettingCard(
            self.tr('更改'),
            FIF.FONT,
            self.tr('主体字体'),
            cfg.get(cfg.deskLyricFontFamily),
            parent=self.personalGroup
        )
        self.updateOnStartUpCard = ComboBoxSettingCard(
            cfg.checkUpdateAtStartUp,
            FIF.UPDATE,
            self.tr('启动更新'),
            self.tr('程序启动时会检查最新更新'),
            texts=['每次检查', '每月检查', self.tr('永不更新')],
            parent=self.personalGroup
        )
        self.loadingStyleCard = ComboBoxSettingCard(
            cfg.loadingStyle,
            FIF.TRANSPARENT,
            self.tr('加载样式'),
            self.tr('选择ΔE+KT算法的加载动画'),
            texts=["动画式一", "动画式二", "动画式三"],
            parent=self.personalGroup
        )

        self.__initWidget()

    def __initWidget(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 0, 0, 0)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.__setQss()
        self.__initLayout()
        self.__connectSignalToSlot()

    def __initLayout(self):
        # add cards to group
        self.personalGroup.addSettingCard(self.downloadFolderCard)
        self.personalGroup.addSettingCard(self.savesFolderCard)
        self.personalGroup.addSettingCard(self.themeColorCard)
        self.personalGroup.addSettingCard(self.deskLyricFontCard)
        self.personalGroup.addSettingCard(self.loadingStyleCard)
        self.personalGroup.addSettingCard(self.zoomCard)
        self.personalGroup.addSettingCard(self.languageCard)
        self.personalGroup.addSettingCard(self.themeCard)
        self.personalGroup.addSettingCard(self.updateOnStartUpCard)

        self.expandLayout.addWidget(self.personalGroup)

    def __setQss(self):
        """ set style sheet """
        self.scrollWidget.setObjectName('scrollWidget')

        theme = 'dark' if isDarkTheme() else 'light'
        with open(f'settings/resource/qss/{theme}/setting_interface.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def __showRestartTooltip(self):
        """ show restart tooltip """
        InfoBar.warning(
            '',
            self.tr('此配置于重启后生效'),
            parent=self.setting.window()
        )

    def __onDeskLyricFontCardClicked(self):
        """ desktop lyric font button clicked slot """
        font, isOk = QFontDialog.getFont(cfg.desktopLyricFont, self.window(), self.tr("选择字体"))
        if isOk:
            cfg.desktopLyricFont = font
            self.updateDeskLyricFontCardContent()

    def __onthemeColorCardClicked(self):
        """ theme color card button clicked slot """
        color = QColorDialog.getColor(cfg.ThemeColorIT, self.window(), self.tr("选择颜色"))
        for i in range(2):
            if color.isValid():
                cfg.ThemeColorIT = color
                self.updateThemeColorCardContent()  # 更新主题颜色卡内容
                cfg.set(cfg.ThemeColor, color)

    def __onDownloadFolderCardClicked(self):
        """ download folder card clicked slot """
        folder = QFileDialog.getExistingDirectory(self, self.tr("选择文件夹"), "./")
        if not folder or cfg.get(cfg.downloadFolder) == folder:
            return

        cfg.set(cfg.downloadFolder, folder)
        self.downloadFolderCard.setContent(folder)

    def __onSavesFolderCardClicked(self):
        """ saves folder card clicked slot """
        folder = QFileDialog.getExistingDirectory(self, self.tr("选择文件夹"), "./")
        if not folder or cfg.get(cfg.savesFolder) == folder:
            return

        cfg.set(cfg.savesFolder, folder)
        self.savesFolderCard.setContent(folder)

    def updateThemeColorCardContent(self):
        """ 更新主题颜色卡的内容 """
        content = cfg.get(cfg.ThemeColor).name()  # 获取颜色名称字符串
        setThemeColor(content)
        self.themeColorCard.setContent(content)  # 更新 PushSettingCard 的内容

    def updateDeskLyricFontCardContent(self):
        """ 更新主题字体卡的内容 """
        content = cfg.get(cfg.deskLyricFontFamily)
        self.deskLyricFontCard.setContent(content)

    def __onThemeChanged(self, theme: Theme):
        self.__showRestartTooltip()
        #setTheme(theme)
        #self.__setQss()

    def __connectSignalToSlot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__showRestartTooltip)
        cfg.themeChanged.connect(self.__onThemeChanged)

        self.downloadFolderCard.clicked.connect(self.__onDownloadFolderCardClicked)
        self.savesFolderCard.clicked.connect(self.__onSavesFolderCardClicked)

        self.deskLyricFontCard.clicked.connect(self.__onDeskLyricFontCardClicked)
        self.themeColorCard.clicked.connect(self.__onthemeColorCardClicked)
