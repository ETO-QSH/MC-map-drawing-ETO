# coding:utf-8
import os
from PyQt5.QtCore import Qt, QLocale, QTranslator
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget

from qfluentwidgets import isDarkTheme, FluentTranslator, setThemeColor, setTheme, Theme
from ETO.settings.setting_interface import SettingInterface
from ETO.settings.config import *

class UI_Yui(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.settingInterface = SettingInterface(self)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.settingInterface)

        self.setQss()

    def setQss(self):
        theme = 'dark' if cfg.get(cfg.themeModeETO) == '暗色主题' else 'light'
        with open(f'settings/resource/qss/{theme}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

