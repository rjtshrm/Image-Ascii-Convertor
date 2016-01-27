# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 00:26:52 2016

@author: Rajat_Sharma
"""

'''from PIL import Image
import sys,os,time
ascii=[ '#', '?', '%', '.', 'S', '+', ',', '*', ':', '@', ' ']
print sys.argv[-1]
filename=sys.argv[-1]
img=Image.open(filename)
if img.size[0]>640 and img.size[1]>480:
    res=img.resize((640,480))
    res.save('resize.jpg')
    img=Image.open('resize.jpg')
rgb=img.convert('RGB')
x,y=img.size
f=open(filename+'.txt','w')
for i in range(0,y):
    f.write('\n')
    for j in range(0,x):
        ls=rgb.getpixel((j,i))
        val=(ls[0]+ls[1]+ls[2])/3
        if val<0:
            ch=ascii[10]
        elif val>=0 and val<15:
            ch=ascii[0]
        elif val>=15 and val<30:
            ch=ascii[1]
        elif val>=30 and val<60:
            ch=ascii[2]
        elif val>=60 and val<100:
            ch=ascii[3]
        elif val>=100 and val<130:
            ch=ascii[4]
        elif val>=130 and val<150:
            ch=ascii[5]
        elif val>=150 and val<175:
            ch=ascii[6]
        elif val>=175 and val<200:
            ch=ascii[7]
        elif val>=200 and val<230:
            ch=ascii[8]
        elif val>=230 and val<=255:
            ch=ascii[9]
        f.write(ch)
try:
    #time.sleep(5)
    os.remove('resize.jpg')
except:
    pass

__author__ = "Rajat Sharma"
__version__ = "1.0.1"
__maintainer__ = "Rajat Sharma"
__email__ = "rjt.rjtshrm94@gmail.com"'''

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 00:26:52 2016

@author: Rajat_Sharma
"""
from PIL import Image
import sys,os,time

def _main_(filename):
    ascii=[ '#', '?', '%', '.', 'S', '+', ',', '*', ':', '@', ' ']
    img=Image.open(filename)
    if img.size[0]>640 and img.size[1]>480:
        res=img.resize((640,480))
        res.save('resize.jpg')
        img=Image.open('resize.jpg')
    rgb=img.convert('RGB')
    x,y=img.size
    f=open(filename+'.txt','w')
    for i in range(0,y):
        f.write('\n')
        for j in range(0,x):
            ls=rgb.getpixel((j,i))
            val=(ls[0]+ls[1]+ls[2])/3
            if val<0:
                ch=ascii[10]
            elif val>=0 and val<15:
                ch=ascii[0]
            elif val>=15 and val<30:
                ch=ascii[1]
            elif val>=30 and val<60:
                ch=ascii[2]
            elif val>=60 and val<100:
                ch=ascii[3]
            elif val>=100 and val<130:
                ch=ascii[4]
            elif val>=130 and val<150:
                ch=ascii[5]
            elif val>=150 and val<175:
                ch=ascii[6]
            elif val>=175 and val<200:
                ch=ascii[7]
            elif val>=200 and val<230:
                ch=ascii[8]
            elif val>=230 and val<=255:
                ch=ascii[9]
            f.write(ch)
    try:
        #time.sleep(5)
        os.remove('resize.jpg')
    except:
        pass


filename=sys.argv[-1]
_main_(filename)

__author__ = "Rajat Sharma"
__version__ = "1.0.1"
__maintainer__ = "Rajat Sharma"
__email__ = "rjt.rjtshrm94@gmail.com"
