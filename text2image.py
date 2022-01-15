
import time
from selenium import webdriver
from PIL import Image
import os
import sys
import json
import urllib.request
def transl(text) :
    
    client_id = "TnA8EcHrHmEQGHfn4TmM" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "lZANutSSPx" # 개발자센터에서 발급받은 Client Secret 값
    
    encText = text#입력
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        res = json.loads(response_body.decode('utf-8'))
        result = res['message']['result']['translatedText']
        return result
    else:
        print("Error Code:" + rescode)

def text2image_gauGAN(input_text):
    #print(input_text)
    driver = webdriver.Chrome("./chromedriver")
    time.sleep(0.2)
    add = 'http://gaugan.org/gaugan2/'
    time.sleep(0.2)
    driver.get(add)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/header/button/span").click()
    time.sleep(0.2)
    driver.find_element_by_xpath("//*[@id='enable_text']").click()
    time.sleep(0.2)
    driver.find_element_by_xpath("//*[@id='enable_seg']").click()
    time.sleep(0.2)
    driver.find_element_by_xpath("//*[@id='myCheck']").click()

    input_box = driver.find_element_by_xpath("//*[@id='text_input']")
    input_box.clear()
    input_box.send_keys(input_text)
    time.sleep(0.2)

    driver.find_element_by_xpath("//*[@id='render']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='save_render']").click()
    time.sleep(3)
    
    print("success")
    #im = Image.open("C:/Users/Hyun/OneDrive - konkuk.ac.kr/문서/gaugan_output.jpg")
    #im.show()

if __name__ == "__main__":
    text_arr=transl(sys.argv[1])
    text2image_gauGAN(text_arr)


