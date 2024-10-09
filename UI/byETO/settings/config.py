
import json

from PyQt5.QtGui import QGuiApplication, QFont, QColor
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, ColorConfigItem,
                            OptionsValidator, RangeConfigItem, RangeValidator, FolderValidator)

class Config(QConfig):
    """ Config of application """

    try:
        with open('./byETO/settings/config/config.json', 'r', encoding="utf-8") as file:
           config_data = json.load(file)
        theme_color = config_data["QFluentWidgets"]["ThemeColor"]
    except FileNotFoundError:
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
qconfig.load('./byETO/settings/config/config.json', cfg)
