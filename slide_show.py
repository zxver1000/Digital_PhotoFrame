import sys
import os
import cv2
import math
import pyautogui
import numpy as np
from urllib.request import urlopen
from PIL import Image
import urllib.request


def getValue(url):

    
    #img = Image.open(urlopen(url))
    
    idx=0
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    
    a=url
    a=a.split(',')
    cnt=len(a)
    while 1:
        resp =urllib.request.urlopen(a[idx])
        img=np.asarray(bytearray(resp.read()),dtype='uint8')
        img=cv2.imdecode(img,cv2.IMREAD_COLOR)
        if img is None:
            break
        cv2.imshow('image',img)
        if cv2.waitKey(1000) >=0:
            break
        idx+=1
        if idx >=cnt:
            idx=0
    
    


if __name__ == '__main__':
    getValue(sys.argv[1])
