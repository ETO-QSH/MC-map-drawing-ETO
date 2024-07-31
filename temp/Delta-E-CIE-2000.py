from tqdm import tqdm
from PIL import Image
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from scipy.spatial import KDTree
from multiprocessing import Pool

def rgb_to_hex(rgb_r, rgb_g, rgb_b):
    r = round(rgb_r * 255)
    g = round(rgb_g * 255)
    b = round(rgb_b * 255)
    hex_color = f'#{r:02X}{g:02X}{b:02X}'
    return hex_color

def create_kdtree(map_colors):
    lab_colors = [convert_color(sRGBColor.new_from_rgb_hex(color), LabColor) for color in map_colors]
    return KDTree([color.get_value_tuple() for color in lab_colors]), lab_colors

def find_closest_color(rgb_color, kdtree, lab_colors):
    rgb_color_obj = sRGBColor.new_from_rgb_hex(rgb_color)
    lab_color = convert_color(rgb_color_obj, LabColor)

    # 使用 KD-Tree 查找最近的 16 个邻居
    distances, indices = kdtree.query(lab_color.get_value_tuple(), k=16)

    min_delta_e = float('inf')
    closest_color = None

    for index in indices:
        lab = lab_colors[index]
        delta_e = delta_e_cie2000(lab_color, lab)
        if delta_e < min_delta_e:
            min_delta_e = delta_e
            closest_color = lab

    cc = convert_color(closest_color, sRGBColor)
    hex_color = rgb_to_hex(cc.rgb_r, cc.rgb_g, cc.rgb_b)
    return rgb_color, hex_color

def map_color_wrapper(args):
    rgb_color, kdtree, lab_colors = args
    return find_closest_color(rgb_color, kdtree, lab_colors)

def read_image_and_map_colors(image_path, map_colors):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = image.load()
    width, height = image.size

    kdtree, lab_colors = create_kdtree(map_colors)

    unique_colors = set()
    for i in range(width):
        for j in range(height):
            rgb_color_tuple = pixels[i, j]
            rgb_color = "#{:02X}{:02X}{:02X}".format(*rgb_color_tuple)
            unique_colors.add(rgb_color)

    unique_colors = list(unique_colors)

    with Pool(processes=None) as pool:
        results = list(tqdm(pool.imap(map_color_wrapper, [(color, kdtree, lab_colors) for color in unique_colors]), total=len(unique_colors), desc="Processing Colors"))

    color_mapping = dict(results)

    new_image = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            rgb_color_tuple = pixels[i, j]
            rgb_color = "#{:02X}{:02X}{:02X}".format(*rgb_color_tuple)
            mapped_color_hex = color_mapping[rgb_color]
            hex_color = mapped_color_hex.lstrip('#')
            new_image.putpixel((i, j), tuple(int(hex_color[k:k+2], 16) for k in (0, 2, 4)))

    return new_image

def save_new_image(new_image, save_path):
    new_image.save(save_path)

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

    image_path, save_path = '128.png', 'new.png'
    new_image = read_image_and_map_colors(image_path, map_colors)
    save_new_image(new_image, save_path)

if __name__ == '__main__':
    main()
