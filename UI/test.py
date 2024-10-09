
from PyQt5.QtGui import QFontDatabase

print('1')

font_id = QFontDatabase.addApplicationFont("./font/萝莉体.ttf")

print('2')

font_name = QFontDatabase.applicationFontFamilies(font_id)[0]

print('3')

# 创建字体对象
font = QtGui.QFont(font_name)

# 创建样式表
stylesheet = f'''
    QLabel {{
        font-family: {font_name};
        font-size: 12px;
        color: red;
    }}
'''
