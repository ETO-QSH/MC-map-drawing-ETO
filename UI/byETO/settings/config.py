
import os, json

from PyQt5.QtGui import QGuiApplication, QFont, QColor
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, ColorConfigItem,
                            OptionsValidator, RangeConfigItem, RangeValidator, FolderValidator)

def find_path(filename):
    for root, dirs, files in os.walk(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))):
        for file in files:
            if file.endswith(os.path.splitext(filename)[1]) and file.startswith(os.path.splitext(filename)[0]):
                return os.path.join(root, file)
    return None

class Config(QConfig):
    try:
        with open('./config.json', 'r', encoding="utf-8") as file:
           config_data = json.load(file)
        theme_color = config_data["QFluentWidgets"]["ThemeColor"]
    except FileNotFoundError:
        try:
            with open('./byETO/settings/config/config.json', 'r', encoding="utf-8") as file:
               config_data = json.load(file)
            theme_color = config_data["QFluentWidgets"]["ThemeColor"]
        except FileNotFoundError:
            try:
                with open(find_path("config.json"), 'r', encoding="utf-8") as file:
                    config_data = json.load(file)
                theme_color = config_data["QFluentWidgets"]["ThemeColor"]
            except FileNotFoundError:
                print('ConfigFileNotFoundError-byETO')
                theme_color = ''

    downloadFolder = ConfigItem("Folders", "Download", "./Backup", FolderValidator())

    savesFolder = ConfigItem("Folders", "Saves", "./saves", FolderValidator())

    ThemeColor = ColorConfigItem("Color", "ThemeColor", theme_color if theme_color != '' else "#FFBFBF")

    deskLyricFontSize = RangeConfigItem("Font", "FontSize", 50, RangeValidator(15, 50))

    deskLyricFontFamily = ConfigItem("Font", "FontFamily", "萝莉体")

    versionControl = ConfigItem("Version", "version", "1.0.0")

    themeModeETO = OptionsConfigItem("Style", "themeModeETO", "暗色主题", OptionsValidator(["暗色主题", "亮色主题"]), restart=True)

    loadingStyle = OptionsConfigItem("Style", "loadingStyle", "动画式一", OptionsValidator(["动画式一", "动画式二", "动画式三"]), restart=True)

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

try:
    qconfig.load('./config.json', cfg)
except FileNotFoundError:
    try:
        qconfig.load('./byETO/settings/config/config.json', cfg)
    except FileNotFoundError:
        qconfig.load(find_path('config.json'), cfg)
