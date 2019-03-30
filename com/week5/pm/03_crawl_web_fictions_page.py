'''웹 소설 로맨스 장르 페이지의 베스트 리그 >> 로맨스 장르
name, writer, score의 정보를 가져와 보세요^^'''
''' 여러 페지의 내용을 가져오는 것'''

import requests
from bs4 import BeautifulSoup

#### 웹소설 베스트리그 로맨스

def crawl(url) :
    # http 요청 -> HTML 문서
    response = requests.get(url)
    # print(response.content)
    html_data = response.content

    soup = BeautifulSoup(html_data, 'html.parser')
    return soup
def naverWebFictions(start, end) :

    naverWebFictions = []

    for pageNum in range(start, end+1)  : #[1,2,3,4,5,6,7,8,9,10]
        url = "https://novel.naver.com/best/genre.nhn?genre=101&page={0}".format(pageNum)

        soup = crawl(url)

        tag_ul = soup.find("ul",{"class":"list_type1 v3 NE=a:lst_rom"})
        #print(tag_ul)

        tag_lis = tag_ul.findAll("li")
        #print(tag_lis)

        for tag_li in tag_lis :
            # 웹 소설 제목
            tag_a = tag_li.find("a")
            name = tag_a["title"]

            #tag_img = tag_li.find("img")
            #print(tag_img["alt"])

            # 웹소설 작가
            tag_span = tag_li.find("span",{"class":"ellipsis"})
            writer = tag_span.text

            # 웹 소설 평점
            #tag_span_score = tag_li.find("span",{"class":"score_area"})
            #print(tag_span_score)
            tag_em = tag_li.find("em")
            score = tag_em.text

            naverWebFictions.append(name)
        print(len(naverWebFictions))

    return naverWebFictions

print(naverWebFictions(1,20))

