# https://developers.naver.com/docs/search/blog/

import urllib.request
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context
client_id = "BoqP7ttLY0wDhxvLzawS"
client_secret = "ztLCPvpLyO"

#requests 형태로 코드 변환
encText = "나혼자 산다"
#encText = urllib.parse.quote("나혼자 산다")

#print(encText)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
response = requests.get(url, headers = {"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret} )

if(response.status_code==200):
    html = response.content
    print(html)
else:
    print("Error Code:" + response.status_code)

'''
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
'''