from PyQt5.QtCore import QPoint

from qfluentwidgets import InfoBarManager, InfoBar


@InfoBarManager.register('Custom')
class CustomInfoBarManager(InfoBarManager):
    """ 自定义消息条管理器 """

    def _pos(self, infoBar: InfoBar, parentSize=None):
        p = infoBar.parent()
        parentSize = parentSize or p.size()

        # 第一个消息条的位置
        x = (parentSize.width() - infoBar.width()) // 2
        y = (parentSize.height() - infoBar.height()) // 2

        # 计算当前 infoBar 的位置
        index = self.infoBars[p].index(infoBar)
        for bar in self.infoBars[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(x, y)

    def _slideStartPos(self, infoBar: InfoBar):
        pos = self._pos(infoBar)
        return QPoint(pos.x(), pos.y() - 16)



InfoBar.success(
    title='Lesson 4',
    content="表达敬意吧，表达出敬意，然后迈向回旋的另一个全新阶段！",
    orient=Qt.Horizontal,
    isClosable=True,
    position="Custom",  # 使用自定义管理器
    duration=2000,
    parent=window
)
