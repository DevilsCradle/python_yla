import requests
from bs4 import BeautifulSoup

#CSS selector를 이용해서 Naver news head line 기사 제목 가져오기

url = "https://news.naver.com/"

response = requests.get(url)
html = response.content

bs_obj = BeautifulSoup(html,"html.parser")
titles = bs_obj.select("#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a")

for title in titles :
    print(title.text)
'''    
select("태그명")
select(".클래스명")
select("#아이디명")
select("태그명[속성=값]")
'''
