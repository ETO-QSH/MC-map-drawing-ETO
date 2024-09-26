# coding:utf-8
import json
from enum import Enum

from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QGuiApplication, QFont, QColor
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            ColorConfigItem, OptionsValidator, RangeConfigItem, RangeValidator,
                            FolderListValidator, EnumSerializer, FolderValidator, ConfigSerializer, __version__)

class Language(Enum):
    """ Language enumeration """

    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Chinese, QLocale.HongKong)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


class Config(QConfig):
    """ Config of application """

    try:
        with open('settings/config/config.json', 'r', encoding="utf-8") as file:
           config_data = json.load(file)
        theme_color = config_data["QFluentWidgets"]["ThemeColor"]
    except FileNotFoundError:
        theme_color = ''

    downloadFolder = ConfigItem("Folders", "Download", "Backup", FolderValidator())

    savesFolder = ConfigItem("Folders", "Saves", "saves", FolderValidator())

    ThemeColor = ColorConfigItem("QFluentWidgets", "ThemeColor", theme_color if theme_color != '' else "#ffbfbf")

    dpiScale = OptionsConfigItem("MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, 2.25, "Auto"]), restart=True)

    language = OptionsConfigItem("MainWindow", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)

    deskLyricFontSize = RangeConfigItem("DesktopLyric", "FontSize", 50, RangeValidator(15, 50))

    deskLyricFontFamily = ConfigItem("DesktopLyric", "FontFamily", "萝莉体")

    checkUpdateAtStartUp = OptionsConfigItem("Update", "CheckUpdateAtStartUp", "Auto", OptionsValidator(["每次检查", "每月检查", "永不更新"]), restart=True)

    loadingStyle = OptionsConfigItem("Update", "CheckUpdateAtStartUp", "动画式一", OptionsValidator(["动画式一", "动画式二", "动画式三"]), restart=True)

    @property
    def desktopLyricFont(self):
        """ get the desktop lyric font """
        font = QFont(self.deskLyricFontFamily.value)
        font.setPixelSize(self.deskLyricFontSize.value)
        return font

    @desktopLyricFont.setter
    def desktopLyricFont(self, font: QFont):
        dpi = QGuiApplication.primaryScreen().logicalDotsPerInch()
        self.deskLyricFontFamily.value = font.family()
        self.deskLyricFontSize.value = max(15, int(font.pointSize()*dpi/72))
        self.save()

    @property
    def ThemeColorIT(self):
        color = QColor(self.ThemeColor.value)
        return color

    @ThemeColorIT.setter
    def ThemeColorIT(self, color: QColor):
        self.ThemeColor.value = color.name()
        self.save()

cfg = Config()
qconfig.load('D:/Work Files/PyQt-Fluent-Widgets-exploit/ETO/settings/config/config.json', cfg)
