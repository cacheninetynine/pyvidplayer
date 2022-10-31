from PIL import Image
import time
import sys
import os
lst = [5,64,127,192,245]
size = os.get_terminal_size()
print(f'{size}\n')
res = (round(size.columns/2), round(size.lines)-2)
fastres = (round(size.columns/2), round(size.lines)-1)
print(res)
time.sleep(0.5)
# # # #
start = sys.argv[1]
vidlen = int(sys.argv[2])
fps = float(sys.argv[3])
colormode = str(sys.argv[4])
# # # #

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

def colorconvert(img):
    d = ''
    img = Image.open(img).resize(size=res,resample = Image.NEAREST)
    for color in img.getdata():
        d += colored(color[0], color[1], color[2], '██')
    print(d)
    
def convert(img):
    d = ''
    img = Image.open(img).resize(size=res,resample = Image.NEAREST)
    for color in img.getdata():
        avr = (color[0] + color[0] + color[1] + color[1] + color[1] + color[2]) / 6
        rslt = min(lst, key=lambda x: abs(x - avr))
        if rslt == 5:
            d += '  '
        if rslt == 64:
            d += '░░'
        if rslt == 127:
            d += '▒▒'
        if rslt == 192:
            d += '▓▓'
        if rslt == 245:
            d += '██'
    print(d)

def slowrender():
    for i in range(1,vidlen):
        oldtime = time.time()
        if len(str(i)) == 1:
            fard = f'0000{i}'
        if len(str(i)) == 2:
            fard = f'000{i}'
        if len(str(i)) == 3:
            fard = f'00{i}'
        if len(str(i)) == 4:
            fard = f'0{i}'
        if len(str(i)) == 5:
            fard = f'{i}'
        convert(img=f'{start}{fard}.jpg')
        fi = 1.0/fps - min((1.0/fps, time.time() - oldtime))
        print(f'{fard}.jpg | fps {fps} | fi {fi}')
        time.sleep(fi)
        
def slowcolorrender():
    for i in range(1,vidlen):
        oldtime = time.time()
        if len(str(i)) == 1:
            fard = f'0000{i}'
        if len(str(i)) == 2:
            fard = f'000{i}'
        if len(str(i)) == 3:
            fard = f'00{i}'
        if len(str(i)) == 4:
            fard = f'0{i}'
        if len(str(i)) == 5:
            fard = f'{i}'
        colorconvert(img=f'{start}{fard}.jpg')
        fi = 1.0/fps - min((1.0/fps, time.time() - oldtime))
        print(f'{fard}.jpg | fps {fps} | {colormode} | fi {fi}')
        time.sleep(fi)
        

if colormode == 'color':
    slowcolorrender()
elif colormode == 'bw':
    slowrender()
else:
    print("Invalid Color Mode")
