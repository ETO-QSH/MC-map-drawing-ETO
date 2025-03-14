
from PyQt5.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import Theme

from ETO.byETO.settings.setting_interface import SettingInterface
from ETO.byETO.settings.config import *

import os

class UI_Yui(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.settingInterface = SettingInterface(self)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.settingInterface)

        self.setQss()

    def setQss(self):
        theme = 'dark' if qconfig.theme == Theme.DARK else 'light'
        try:
            with open(f'./byETO/settings/resource/qss/{theme}/demo.qss', encoding='utf-8') as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            with open(f'{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}/ETO/byETO/settings/resource/qss/{theme}/demo.qss', encoding='utf-8') as f:
                self.setStyleSheet(f.read())
