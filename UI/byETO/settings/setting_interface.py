
import os, re, requests, pyperclip

from typing import List
from PyQt5 import QtWidgets, QtCore
from requests.exceptions import SSLError

from ETO.byETO.settings.config import *
from qfluentwidgets import (PushSettingCard, ScrollArea, ComboBoxSettingCard, ExpandLayout, Theme, InfoBar, setThemeColor,
                            FluentStyleSheet, MessageBoxBase, SubtitleLabel, StrongBodyLabel, BodyLabel, InfoBarPosition)

from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFontDialog, QFileDialog, QColorDialog, QVBoxLayout, QFrame

class CustomMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, now_tag, search_tag, search_body, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('检查更新')
        self.subtitleLabel = StrongBodyLabel(f'当前版本：{now_tag}' '\n' f'最新版本：{search_tag}')

        self.ScrollArea_2 = ScrollArea(self)
        self.ScrollArea_2.setMinimumSize(QtCore.QSize(270, 270))
        self.ScrollArea_2.setMaximumSize(QtCore.QSize(270, 270))
        self.ScrollArea_2.setFrameShape(QFrame.NoFrame)
        self.ScrollArea_2.setFrameShadow(QFrame.Plain)
        self.ScrollArea_2.setLineWidth(0)
        self.ScrollArea_2.setWidgetResizable(True)
        self.ScrollArea_2.setObjectName("ScrollArea_2")
        self.ScrollArea_2.setStyleSheet(f"background-color: {'#272727' if qconfig.theme == Theme.DARK else '#f9f9f9'};")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 270, 2700))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.BodyLabel = BodyLabel(self.scrollAreaWidgetContents_2)
        self.BodyLabel.setMinimumSize(QtCore.QSize(240, 0))
        self.BodyLabel.setMaximumSize(QtCore.QSize(240, 16777215))
        self.BodyLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.BodyLabel.setWordWrap(True)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridLayout.addWidget(self.BodyLabel, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.ScrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.set_font("萝莉体", 15, self.titleLabel)
        self.set_font("萝莉体", 12, self.subtitleLabel)
        self.set_font("萝莉体", 10, self.BodyLabel)
        self.set_font("萝莉体", 10, self.yesButton)

        cancelButtonStyle = """
        QPushButton {
            font-family: '萝莉体';
            font-size: 13px;
        }
        """
        self.cancelButton.setStyleSheet(cancelButtonStyle)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.subtitleLabel)
        self.viewLayout.addWidget(self.ScrollArea_2)

        _translate = QtCore.QCoreApplication.translate
        self.BodyLabel.setText(_translate("Form", search_body))

        self.widget.setMinimumWidth(300)

    def set_font(self, font_name, font_size, label):
        """ 设置指定标签的字体和大小 """
        font = QFont(font_name, font_size)
        label.setFont(font)


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
            self.tr('更  改'),
            FIF.DOWNLOAD,
            self.tr("备份目录"),
            cfg.get(cfg.downloadFolder),
            self.personalGroup
        )
        self.savesFolderCard = PushSettingCard(
            self.tr('更  改'),
            FIF.SAVE,
            self.tr("存档目录"),
            cfg.get(cfg.savesFolder),
            self.personalGroup
        )
        self.themeColorCard = PushSettingCard(
            self.tr('更  改'),
            FIF.PALETTE,
            self.tr('主题颜色'),
            cfg.get(cfg.ThemeColor).name().upper(),
            parent=self.personalGroup
        )
        self.themeCard = ComboBoxSettingCard(
            cfg.themeModeETO,
            FIF.BRUSH,
            self.tr('黑白主题'),
            self.tr('设置UI的主体风格'),
            texts=[self.tr('暗色主题'), self.tr('亮色主题')],
            parent=self.personalGroup
        )
        self.deskLyricFontCard = PushSettingCard(
            self.tr('更  改'),
            FIF.FONT,
            self.tr('主体字体'),
            cfg.get(cfg.deskLyricFontFamily) + ' (不给改就好这萝莉体)',
            parent=self.personalGroup
        )
        self.updateOnStartUpCard = PushSettingCard(
            self.tr('获  取'),
            FIF.UPDATE,
            self.tr('检查更新'),
            f'当前版本: {cfg.get(cfg.versionControl)}',
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

    def CardFont(self, Card, mode):

        titleLabelStyle = """
                        QLabel {
                            font-family: '萝莉体';
                            font-size: 15px;
                        }
                        """
        Card.titleLabel.setStyleSheet(titleLabelStyle)

        contentLabelStyle = """
                        QLabel {
                            font-family: '萝莉体';
                            font-size: 12px;
                        }
                        """
        Card.contentLabel.setStyleSheet(contentLabelStyle)

        if mode == 0:
            ButtonStyle = """
                            QPushButton {
                                font-family: '萝莉体';
                                font-size: 15px;
                            }
                            """
            Card.button.setStyleSheet(ButtonStyle)

        elif mode == 1:
            Style = re.sub(r'\*\*\*', '#ffffff' if qconfig.theme == Theme.DARK else '#000000', '''
            RangeSettingCard > QLabel#valueLabel{
                font-family: '萝莉体';
                font-size: 15px;
                color: rgb(159, 159, 159);
            }
            QPushButton {
                width: 112px;
                height: 31px;
                padding: 0px;
                border-radius: 5px;
                font: 15px 、'萝莉体';
                color: ***;
            }
            ColorPickerButton {
                font-family: '萝莉体';
                font-size: 15px;
                border: 1px solid rgba(255, 255, 255, 10);
                border-radius: 5px;
                border-bottom: 1px solid rgba(255, 255, 255, 7);
            }
            ComboBox {
                color: ***;
                font-family: '萝莉体';
                font-size: 15px;
            }
            QComboBox QAbstractItemView {
                color: ***;
                font-family: '萝莉体';
                font-size: 15px;
            }''')

            # 下拉框字体不会搞 byETO
            Card.comboBox.setStyleSheet(Style)

    def __initLayout(self):
        # add cards to group
        self.personalGroup.addSettingCard(self.downloadFolderCard)
        self.personalGroup.addSettingCard(self.savesFolderCard)
        self.personalGroup.addSettingCard(self.themeColorCard)
        self.personalGroup.addSettingCard(self.deskLyricFontCard)
        self.personalGroup.addSettingCard(self.updateOnStartUpCard)
        self.personalGroup.addSettingCard(self.loadingStyleCard)
        self.personalGroup.addSettingCard(self.themeCard)

        self.CardFont(self.downloadFolderCard, 0)
        self.CardFont(self.savesFolderCard, 0)
        self.CardFont(self.themeColorCard, 0)
        self.CardFont(self.deskLyricFontCard, 0)
        self.CardFont(self.updateOnStartUpCard, 0)
        self.CardFont(self.loadingStyleCard, 1)
        self.CardFont(self.themeCard, 1)

        self.expandLayout.addWidget(self.personalGroup)

    def __setQss(self):
        """ set style sheet """
        self.scrollWidget.setObjectName('scrollWidget')

        theme = 'dark' if cfg.get(cfg.themeModeETO) == '暗色主题' else 'light'

        try:
            with open(f'./byETO/settings/resource/qss/{theme}/setting_interface.qss', encoding='utf-8') as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            with open(f'{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}/byETO/settings/resource/qss/{theme}/setting_interface.qss', encoding='utf-8') as f:
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

    def __onVersionCardClicked(self):
        """ version card clicked slot """

        def search(url):
            try:
                text = requests.get(url).text
                data = json.loads(text)

            except SSLError as e:
                InfoBar.error(
                    title='SSL Error',
                    content=str(e),
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2500,
                    parent=self
                )
                return False

            except Exception as e:
                InfoBar.error(
                    title='Unknown Error',
                    content=str(e),
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2500,
                    parent=self
                )
                return False

            try:
                search_url = data["assets"][0]["browser_download_url"]
                search_size = data["assets"][0]["size"]
                search_tag = data["tag_name"]
                search_body = data["body"]

            except KeyError:
                InfoBar.error(
                    title='IP Error',
                    content=data['message'],
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2500,
                    parent=self
                )
                return False

            except Exception as e:
                InfoBar.error(
                    title='Unknown Error',
                    content=str(e),
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2500,
                    parent=self
                )
                return False

            return search_url, search_size, search_tag, search_body

        searches = search("https://api.github.com/repos/ETO-QSH/DeskpetETO-download/releases/latest")

        if not searches == False:
            search_url, search_size, search_tag, search_body = searches
            now_tag = cfg.get(cfg.versionControl)

            w = CustomMessageBox(now_tag, search_tag, search_body, self.setting)
            w.yesButton.setText("点击复制URL")
            w.cancelButton.setText(f"不浪费{int(search_size/1024/1024)}MB")

            pyperclip.copy(search_url) if w.exec() else False

    def updateThemeColorCardContent(self):
        """ 更新主题颜色卡的内容 """
        content = cfg.get(cfg.ThemeColor).name()  # 获取颜色名称字符串
        setThemeColor(content)
        self.themeColorCard.setContent(content.upper())  # 更新 PushSettingCard 的内容

    def updateDeskLyricFontCardContent(self):
        """ 更新主题字体卡的内容 """
        content = cfg.get(cfg.deskLyricFontFamily)
        self.deskLyricFontCard.setContent(content)

    def __onThemeChanged(self, theme: Theme):
        self.__showRestartTooltip()

    def __connectSignalToSlot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__showRestartTooltip)
        cfg.themeChanged.connect(self.__onThemeChanged)

        self.downloadFolderCard.clicked.connect(self.__onDownloadFolderCardClicked)
        self.savesFolderCard.clicked.connect(self.__onSavesFolderCardClicked)
        self.updateOnStartUpCard.clicked.connect(self.__onVersionCardClicked)

        self.deskLyricFontCard.clicked.connect(self.__onDeskLyricFontCardClicked)
        self.themeColorCard.clicked.connect(self.__onthemeColorCardClicked)
