
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
import matplotlib.pyplot as plt
import numpy as np


def lab_to_hex(L, a, b):
    lab_color = LabColor(L, a, b)
    srgb_color = convert_color(lab_color, sRGBColor)
    hex_color = srgb_color.get_rgb_hex()
    return hex_color

def ShowPit(color_list):
    # 分别提取L, a, b值
    L_values = [color[0] for color in color_list]
    a_values = [color[1] for color in color_list]
    b_values = [color[2] for color in color_list]

    # 创建三个独立的图表
    fig, axs = plt.subplots(3, 1, figsize=(12, 4))  # 3行1列的子图布局

    # 绘制L值的图表
    axs[0].set_title('L Values Over Color List')
    axs[0].set_ylabel('L Value')
    axs[0].set_xlim(0, 100)
    axs[0].set_xticks(np.arange(0, 100, 12.5))
    for L in L_values:
        axs[0].axvline(x=L, color='blue', linestyle='-', linewidth=0.25)

    # 绘制a值的图表
    axs[1].set_title('a Values Over Color List')
    axs[1].set_ylabel('a Value')
    axs[1].set_xlim(-128, 127)
    axs[1].set_xticks(np.arange(-128, 128, 32))
    for a in a_values:
        axs[1].axvline(x=a, color='green', linestyle='-', linewidth=0.25)

    # 绘制b值的图表
    axs[2].set_title('b Values Over Color List')
    axs[2].set_ylabel('b Value')
    axs[2].set_xlim(-128, 127)
    axs[2].set_xticks(np.arange(-128, 128, 32))
    for b in b_values:
        axs[2].axvline(x=b, color='red', linestyle='-', linewidth=0.25)

    # 调整子图间距
    plt.tight_layout()
    plt.show()


def Tocolors(map_colors):
    lab_colors = [convert_color(sRGBColor.new_from_rgb_hex(color), LabColor) for color in map_colors]
    lab_colors = [(i.lab_l, i.lab_a, i.lab_b) for i in lab_colors]
    return lab_colors


def main():
    map_colors = ['#597D27', '#6D9930', '#7FB238', '#435E1D',
                  '#AEA473', '#D5C98C', '#F7E9A3', '#827B56',
                  '#8C8C8C', '#ABABAB', '#C7C7C7', '#696969',
                  '#B40000', '#DC0000', '#FF0000', '#870000',
                  '#7070B4', '#8A8ADC', '#A0A0FF', '#545487',
                  '#757575', '#909090', '#A7A7A7', '#585858',
                  '#005700', '#006A00', '#007C00', '#004100',
                  '#B4B4B4', '#DCDCDC', '#FFFFFF', '#878787',
                  '#737681', '#8D909E', '#A4A8B8', '#565861',
                  '#6A4C36', '#825E42', '#976D4D', '#4F3928',
                  '#4F4F4F', '#606060', '#707070', '#3B3B3B',
                  '#2D2DB4', '#3737DC', '#4040FF', '#212187',
                  '#645432', '#7B663E', '#8F7748', '#4B3F26',
                  '#B4B1AC', '#DCD9D3', '#FFFCF5', '#878581',
                  '#985924', '#BA6D2C', '#D87F33', '#72431B',
                  '#7D3598', '#9941BA', '#B24CD8', '#5E2872',
                  '#486C98', '#5884BA', '#6699D8', '#365172',
                  '#A1A124', '#C5C52C', '#E5E533', '#79791B',
                  '#599011', '#6DB015', '#7FCC19', '#436C0D',
                  '#AA5974', '#D06D8E', '#F27FA5', '#804357',
                  '#353535', '#414141', '#4C4C4C', '#282828',
                  '#6C6C6C', '#848484', '#999999', '#515151',
                  '#35596C', '#416D84', '#4C7F99', '#284351',
                  '#592C7D', '#6D3699', '#7F3FB2', '#43215E',
                  '#24357D', '#2C4199', '#334CB2', '#1B285E',
                  '#483524', '#58412C', '#664C33', '#36281B',
                  '#485924', '#586D2C', '#667F33', '#36431B',
                  '#6C2424', '#842C2C', '#993333', '#511B1B',
                  '#111111', '#151515', '#191919', '#0D0D0D',
                  '#B0A836', '#D7CD42', '#FAEE4D', '#847E28',
                  '#409A96', '#4FBCB7', '#5CDBD5', '#307370',
                  '#345AB4', '#3F6EDC', '#4A80FF', '#274387',
                  '#009928', '#00BB32', '#00D93A', '#00721E',
                  '#5B3C22', '#6F4A2A', '#815631', '#442D19',
                  '#4F0100', '#600100', '#700200', '#3B0100',
                  '#937C71', '#B4988A', '#D1B1A1', '#6E5D55',
                  '#703919', '#89461F', '#9F5224', '#542B13',
                  '#693D4C', '#804B5D', '#95576C', '#4E2E39',
                  '#4F4C61', '#605D77', '#706C8A', '#3B3949',
                  '#835D19', '#A0721F', '#BA8524', '#624613',
                  '#485225', '#58642D', '#677535', '#363D1C',
                  '#703637', '#8A4243', '#A04D4E', '#542829',
                  '#281C18', '#31231E', '#392923', '#1E1512',
                  '#5F4B45', '#745C54', '#876B62', '#473833',
                  '#3D4040', '#4B4F4F', '#575C5C', '#2E3030',
                  '#56333E', '#693E4B', '#7A4958', '#40262E',
                  '#352B40', '#41354F', '#4C3E5C', '#282030',
                  '#352318', '#412B1E', '#4C3223', '#281A12',
                  '#35391D', '#414624', '#4C522A', '#282B16',
                  '#642A20', '#7A3327', '#8E3C2E', '#4B1F18',
                  '#1A0F0B', '#1F120D', '#251610', '#130B08',
                  '#852122', '#A3292A', '#BD3031', '#641919',
                  '#682C44', '#7F3653', '#943F61', '#4E2133',
                  '#401114', '#4F1519', '#5C191D', '#300D0F',
                  '#0F585E', '#126C73', '#167E86', '#0B4246',
                  '#286462', '#327A78', '#3A8E8C', '#1E4B4A',
                  '#3C1F2B', '#4A2535', '#562C3E', '#2D1720',
                  '#0E7F5D', '#119B72', '#14B485', '#0A5F46',
                  '#3C3C3C', '#4A4A4A', '#565656', '#2D2D2D',
                  '#836958', '#A0816C', '#BA967E', '#624F42',
                  '#597569', '#6D9081', '#7FA796', '#43584F', ]

    Getcolors = Tocolors(map_colors)
    
    Lu, au, bu, Ld, ad, bd = 0, 0, 0, 0, 0, 0
    for i in Getcolors:
        if i[0] > Lu:
            Lu = i[0]
        if i[0] < Ld:
            Ld = i[0]
        if i[1] > au:
            au = i[1]
        if i[1] < ad:
            ad = i[1]
        if i[2] > bu:
            bu = i[2]
        if i[2] < bd:
            bd = i[2]
    print(Lu, Ld, au, ad, bu, bd)

    ShowPit(Getcolors)


if __name__ == '__main__':
    main()
