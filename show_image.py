import sys
import os
import cv2
import math
import pyautogui
import numpy as np
from urllib.request import urlopen
from PIL import Image



def getValue(url):

    
    img = Image.open(urlopen(url))
    img.show()
    os.system("xdg-open {}".format(img))
    print("abcdef")
    pyautogui.press('f11')
    #url="https://firebasestorage.googleapis.com/v0/b/random-7ef55.appspot.com/o/image%2F2%EB%B2%88%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8.PNG?alt=media&token=7a2b110b-7a6b-43e5-81b0-af472154a010";
    #url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxODExMTZfMjE0%2FMDAxNTQyMzU4MDY1OTE3.mke0JLFBO4jS-hJojejDruHQmJkV7b4gKs3oRfn7tdIg.1LxHXj9zP7M09hPrht0iW17TRKkmCAgV6kEjTgPtPDcg.JPEG%2FI1P4kSElZvKVehuLxO8qMBSTUkIU.jpg&type=sc960_832"
    return "adbd"
   
    


if __name__ == '__main__':
    getValue(sys.argv[1])
