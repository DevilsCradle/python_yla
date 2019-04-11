'''
# 쿠팡에서 특정 키워드로 검색한 결과를 파싱하기
import requests
from bs4 import BeautifulSoup


def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content


def getProductInfo(li):
    name = li.find("div", {"class": "name"})
    priceValue = li.find("strong", {"class": "price-value"})
    return {"name": name.text, "price": priceValue.text}


def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id": "productList"})
    lis = ul.findAll("li")
    print("상품개수:", len(lis))
    products = []
    for li in lis:
        productInfo = getProductInfo(li)
        products.append(productInfo)
    return products


keywordResult = []
for page in range(1, 5):
    url = "https://www.coupang.com/np/search?component=&q={0}&page={1}&channel=user".format("에어컨", page)
    pageString = crawl(url)
    products = parse(pageString)
    keywordResult = keywordResult + products

print(len(keywordResult))

import json

file = open("./에어컨.json", "w+")
#keywordResult  = python 형태
# Json.dumps(python dicdata) return json data
jsonData = json.dumps(keywordResult)
file.write(jsonData)
file.close()
'''
import json
#파일 열기
fileRead = open("./에어컨.json", "r+")
#데이터 변환
jsonData = fileRead.read()
pythonData = json.loads(jsonData)
#파일 닫기
fileRead.close()
print(pythonData)

with open("./에어컨.json", "r+") as fileRead:
    pythonData = json.load(fileRead)
