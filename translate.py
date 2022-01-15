import os
import sys
import json
import urllib.request
client_id = "TnA8EcHrHmEQGHfn4TmM" # 개발자센터에서 발급받은 Client ID 값
client_secret = "lZANutSSPx" # 개발자센터에서 발급받은 Client Secret 값
print("원하는 문구 입력 :", end=' ')
encText = input()#입력
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
    print(result)#출력
else:
    print("Error Code:" + rescode)
