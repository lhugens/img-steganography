
import argparse
from PIL import Image

def asci(text):
    ntext = []
    for char in text:  
        ntext.append(format(ord(char), '08b'))
    return ntext
    
def pixelgen(pic, text):
    lentext = len(text)
    piciter = iter(pic)
    bintext = asci(text)

    for i in range(lentext):
        pixels = [ value for value in piciter.__next__()[:3] + 
                                      piciter.__next__()[:3] + 
                                      piciter.__next__()[:3] ] 

        for j in range(8):
            if (bintext[i][j] == '0') and (pixels[j] % 2 != 0):
                pixels[j] = (pixels[j] + 1) % 256
            elif (bintext[i][j] == '1') and (pixels[j] % 2 == 0):
                pixels[j] = (pixels[j] + 1) % 256

        if (i == lentext - 1) :
            if (pixels[-1] % 2 == 0):
                pixels[-1] = (pixels[-1] + 1) % 256
        else:
            if (pixels[-1] % 2 != 0):
                pixels[-1] = (pixels[-1] + 1) % 256

        pixels = tuple(pixels)
        yield pixels[0:3]
        yield pixels[3:6]
        yield pixels[6:9]

def encode(pic, text):
    npic = pic.copy()
    width = npic.size[0]
    (x, y) = (0, 0)

    for pixel in pixelgen(npic.getdata(), text):
        npic.putpixel((x, y), pixel)
        if (x == width - 1):
            x = 0
            y += 1
        else:
            x += 1

    return npic

def decode(pic):
    piciter = iter(pic.getdata())
    text = ''

    while True:
        pixels = [ value for value in piciter.__next__()[:3] + 
                                      piciter.__next__()[:3] + 
                                      piciter.__next__()[:3] ] 

        bintext = ''
        for j in range(8):
            if (pixels[j] % 2 == 0):
                bintext += '0'
            else:
                bintext += '1'
        text += chr(int(bintext, 2))

        if (pixels[-1] % 2 != 0):
            return text

parser = argparse.ArgumentParser(prefix_chars='-')

parser.add_argument('-f', type=str, help='image file')
parser.add_argument('-m', type=str, help='text file')

args = parser.parse_args()

if (args.f != None) and (args.m != None):
    img = Image.open(args.f, 'r')
    txt = open(args.m)
    msg = str(txt.read())
    if len(img.getdata())/3 <= len(msg):
        print('Text is too long for this picture.')
    else:
        name, ext = str(args.f).split('.')
        nimg = encode(img, msg)
        #nimg.save(name + '-new.' + ext)
        nimg.save(name + '.' + ext)

elif (args.f != None):
    img = Image.open(str(args.f), 'r')
    with open("out.txt", "w") as text_file:
        text_file.write(decode(img))
    #print(decode(img))

else:
    parser.print_help()
