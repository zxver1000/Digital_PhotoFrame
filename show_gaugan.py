import sys


import tkinter
import math
import os
import cv2
import numpy as np
from PIL import Image
import pyautogui
from urllib.request import urlopen
#print("1")
def show(alpa):
    if(alpa=="0"):
        print("hihi")
        url="C:/Users/kkj/Downloads/gaugan_output.jpg"
#url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxODExMTZfMjE0%2FMDAxNTQyMzU4MDY1OTE3.mke0JLFBO4jS-hJojejDruHQmJkV7b4gKs3oRfn7tdIg.1LxHXj9zP7M09hPrht0iW17TRKkmCAgV6kEjTgPtPDcg.JPEG%2FI1P4kSElZvKVehuLxO8qMBSTUkIU.jpg&type=sc960_832"
        img = Image.open(url)
        img.show()
        pyautogui.press('f11')
    else :
        url="C:/Users/kkj/Downloads/gaugan_output ("+alpa+").jpg"
#url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxODExMTZfMjE0%2FMDAxNTQyMzU4MDY1OTE3.mke0JLFBO4jS-hJojejDruHQmJkV7b4gKs3oRfn7tdIg.1LxHXj9zP7M09hPrht0iW17TRKkmCAgV6kEjTgPtPDcg.JPEG%2FI1P4kSElZvKVehuLxO8qMBSTUkIU.jpg&type=sc960_832"
        img = Image.open(url)
        img.show()
        pyautogui.press('f11')

#image=Image.open(urllib.urlopen(url).read())
#print(cv2.__version__)

#frame='./public/image/1.png'
#a=cv2.imread(frame,cv2.IMREAD_COLOR)
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
#cv2.imshow('cor',a)

#cv2.waitKey(0)
#os.system("xdg-open {}".format(image))


##
#root=tkinter.Tk()
#root.title("blog")
#root.geometry("840x420")
#root.attributes('-fullscreen',True)
#root.resizable(0, 0)
#image=tkinter.PhotoImage(file="./public/image/1.png") #PhotoImage를 통한 이미지 지정
#label=tkinter.Label(root, image=image) #라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
#label.pack()
if __name__ == "__main__":
    show(sys.argv[1])
    
