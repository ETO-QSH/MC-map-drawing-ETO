
import os; import nbtlib; from PIL import Image; from useful import *; from nbtlib import *  #/function ETO:eto  #/kill @e[type=!player]  #/give ETO filled_map{map:0}
pic='.\\images\\png.png'; img=Image.open(pic); size, name=((img.width+127)//128*128, (img.height+127)//128*128), os.path.splitext(os.path.split(pic)[1])[0]
old, new=Image.new('RGBA', size, (0, 0, 0, 0)), Image.new('RGBA', (size[0], size[1])); old.paste(img, ((size[0]-img.width)//2, (size[1]-img.height)//2))
def tip(m): global t, i; t=[(2+((m[0]+n[0])/2)/256)*((m[0]-n[0])**2)+4*((m[1]-n[1])**2)+(2+(255-((m[0]+n[0])/2))/256)*((m[2]-n[2])**2) for n in map_color]; i=t.index(min(t))
[(tip(old.getpixel((p, q))), new.putpixel((p, q), (map_color[i] if old.getpixel((p, q))[3]!=0 else (0, 0, 0, 0)))) for p in range(size[0]) for q in range(size[1])]
[[os.makedirs('data') if os.path.lexists('data') == False else True], [os.makedirs('images') if os.path.lexists('images') == False else True],
  os.makedirs('datapacks\\eto\\data\\{}\\functions'.format(name)) if os.path.lexists('datapacks\\eto\\data\\{}\\functions'.format(name)) == False else True,
  open('datapacks\\eto\\pack.mcmeta', mode='w', encoding='utf-8').write('{"pack":{"pack_format":8,"description":"ETO"}}'), new.save('images\\{}_new.png'.format(name))]
def map_dat(g, o, p, q): File({"":Compound({'data':Compound({'map':Int('{}'.format(p+1))}), 'DataVersion':Int('0')})}).save('data\\idcounts.dat'); new=File({"":Compound({'data':
  Compound({'zCenter':Int('0'), 'unlimitedTracking':Byte('0'), 'trackingPosition':Byte('0'), 'frames':List([]), 'scale':Byte('0'), 'locked':Byte('1'), 'dimension':String(
  'minecraft:overworld'),'banners':List([]), 'xCenter':Int('0'), 'colors':List(nbtlib.tag.ByteArray([]))}), 'DataVersion':Int('2975')})}); new['']['data']['colors'
  ]=nbtlib.tag.ByteArray(q); new.save('data\\map_{}.dat'.format(p+1)); [[(open('datapacks\\eto\\data\\{}\\functions\\{}.mcfunction'.format(name, ['xa', 'za', 'na', 'ea', 'sa', 'wa',
  'xb', 'zb', 'nb', 'eb', 'sb', 'wb'][6*l+x]),mode='a',encoding='utf-8').write(('summon item_frame ~{} ~{} ~{} {{Facing:{},Invisible:1,Fixed:1,ItemRotation:{},Item:'+
  '{{Count:1,id:"filled_map",tag:{{map:{}}}}}}}\n').format(y[0], y[1], y[2], y[3], y[4], y[5]))) for x, y in enumerate([((1 if l == 0 else -2)+m, size[1]//128-o//g,
  (1 if m == 1 else -1)*((0 if m == 1 else g-1)-o%g),4+m, 0, p+1), ((-1 if m == 1 else 1)*((0 if m == 1 else g-1)-o%g), size[1]//128-o//g, (1 if l == 0 else -2)+m, 2+m, 0, p+1)]+
  [(((-1 if m == n//2 else 1)*(o%g-(0 if m == 0 else g-1)) if n%2 == 0 else ((1 if n//2 == 0 else -1)*(g-o//g-1))), (2 if l == 0 else -1)+m, ((-1 if n//2 == 0 else 1)*((size[1]
  //128-1)-o//g) if n%2 == 0 else (1 if m == n//2 else -1)*((0 if m == 0 else g-1)-o%g)), m, (n+2 if m == n%2 == 0 else n), p+1) for n in range(4)])] for l in [0, 1] for m in [0, 1]]
[map_dat(size[0]//128, o, (nbtlib.load('data\\idcounts.dat')['']['data']['map'] if os.path.lexists('data\\idcounts.dat') == True else -1), q) for o, q in enumerate([[(tip(old.
  getpixel((p, q))), new.putpixel((p, q), map_color[i]), (i-256 if i>128 else i))[2] if old.getpixel((p, q))[3]!=0 else (new.putpixel((p, q), (0, 0, 0, 0)), 0)[1] for q in 
  range(128) for p in range(128)] for dex, old in enumerate([old.crop((128*j, 128*k, 128*(j+1), 128*(k+1))) for k in range(size[1]//128) for j in range(size[0]//128)])])]
