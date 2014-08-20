import PIL
from PIL import Image
from random import *
from math import *
import os

BLACKSTAMP = Image.open("brush.png")

def createStamp(s, c):
    split = BLACKSTAMP.split()
    im = Image.merge("RGB", (split[0],split[1],split[2])).resize((s,s))
    alpha = split[0].resize((s,s))
    for i in range(im.size[0]):
        for j in range(im.size[0]):
            im.putpixel((i,j),(c[0],c[1],c[2]))
    return im, alpha
            

def createImg(c, xLen=100,yLen=100,minN=5,maxN=10,minL=10,maxL=100,size=3):
    print(c,xLen,yLen,minL,maxL)
    im = Image.new("RGB", (xLen,yLen),(0,0,0))
    for i in range(randint(minN, maxN)):
        l = randint(minL,maxL)
        s = int(size*l/((minL+maxL)*2))
        v = uniform(.3,3)
        vd = uniform(-.15,.15)
        d = uniform(0,6.28)
        x = uniform(xLen/5,(4*xLen)/5)
        y = uniform(yLen/5,(4*yLen)/5)
        cv = [randint(-5,5),randint(-5,5),randint(-5,5)]
        #brush, mask = createStamp(10,c)
        brush = Image.new("RGBA", (3,3), c)
        while(l > 0):
            tc = list(c)
            for i in range(3):
                tc[i] += cv[i]
                cv[i] += randint(-1,1)
            c = tuple(tc)
            #brush, mask = createStamp(10,c)
            brush = Image.new("RGBA", (3,3), c)
            y += sin(d)*v
            x += cos(d)*v
            d += vd
            l -= 1;
            im.paste(brush, (int(x),int(y), int(x)+brush.size[0], int(y)+brush.size[1]))#, mask)
            im.paste(brush, (xLen-int(x),int(y), xLen-int(x)+brush.size[0], int(y)+brush.size[1]))#, mask)
            vd += uniform(-.05,.05)
            v += uniform(-.1,.1)
    return im
RUNTITLE= "v0.19-batch3/"
SIZE = 8

if not os.path.exists(RUNTITLE):
    os.makedirs(RUNTITLE)

for i in range(SIZE):
    c = (randint(0,255),randint(0,255),randint(0,255))
    im = createImg(c)
    im.save(RUNTITLE+str(i)+".png")
