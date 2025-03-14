
import os, json
from enum import Enum

from PyQt5.QtGui import QGuiApplication, QFont, QColor

from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, ColorConfigItem,
                            OptionsValidator, RangeConfigItem, RangeValidator, FolderValidator, EnumSerializer, Theme)

def find_path(filename):
    for root, dirs, files in os.walk(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))):
        for file in files:
            if file.endswith(os.path.splitext(filename)[1]) and file.startswith(os.path.splitext(filename)[0]):
                return os.path.join(root, file)
    return None

class myConfig(QConfig):
    def __init__(self):
        super().__init__()

    with open(find_path("config.json"), 'r', encoding="utf-8") as file:
        config_data = json.load(file)

    theme_color = config_data["QFluentWidgets"]["ThemeColor"]

    downloadFolder = ConfigItem("Folders", "Download", "./Backup", FolderValidator())

    savesFolder = ConfigItem("Folders", "Saves", "./saves", FolderValidator())

    ThemeColor = ColorConfigItem("Style", "ThemeColor", theme_color)

    deskLyricFontSize = RangeConfigItem("Font", "FontSize", 50, RangeValidator(15, 50))

    deskLyricFontFamily = ConfigItem("Font", "FontFamily", "萝莉体")

    versionControl = ConfigItem("Version", "version", "1.0.0")

    themeModeETO = OptionsConfigItem("Style", "themeModeETO", "暗色主题", OptionsValidator(["暗色主题", "亮色主题"]))

    loadingStyle = OptionsConfigItem("Style", "loadingStyle", "动画式一", OptionsValidator(["动画式一", "动画式二", "动画式三"]))

    @property
    def desktopLyricFont(self):
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

cfg = myConfig()
qconfig.load(find_path("config.json"), cfg)
