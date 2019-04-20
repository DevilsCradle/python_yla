from selenium import webdriver
from bs4 import BeautifulSoup

### css selector를 이용하여 1등 당첨 점포명 가져오기 ~

driver = webdriver.Chrome('./chromedriver')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

url = "https://www.dhlottery.co.kr/store.do?method=topStore&pageGubun=L645"

## web page load
driver.get(url)

for num in range(500,854):
    #drop down option menu select
    driver.find_element_by_css_selector('#drwNo > option[value = "{}"]'.format(num)).click()

    #search click
    driver.find_element_by_css_selector('#searchBtn').click()

    html = driver.page_source

    bs_obj = BeautifulSoup(html,'html.parser')

    stores_name = bs_obj.select('#article > div:nth-child(2) > div > div:nth-child(4) > table > tbody > tr > td:nth-child(2)')

    for store in stores_name :
        print(num,"회차 로또 1등 당첨 상호명 : ",store.text)

