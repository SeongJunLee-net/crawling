###스타벅스 매장 주소 크롤링해오기###
from telnetlib import EC
from unittest import result
from urllib.request import urlopen
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from urllib.request import Request
from bs4 import BeautifulSoup
import time
result=[]
wd = Chrome("C:\WebDriver\chromedriver.exe")
wd.get("https://www.starbucks.co.kr/store/store_map.do")
time.sleep(0.5)
element = wd.find_element_by_link_text("지역 검색")
element.click()
time.sleep(0.5)
element_seoul = wd.find_element_by_xpath("//*[@id='container']/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a")
element_seoul.click()
time.sleep(0.5)
element_all = wd.find_element_by_xpath("//*[@id='mCSB_2_container']/ul/li[1]/a")
element_all.click()
WebDriverWait(wd,40).until(expected_conditions.presence_of_all_elements_located((By.XPATH,"//*[@id='mCSB_3_container']/ul/li[1]")))

urls = wd.page_source
soup = BeautifulSoup(urls,'html.parser')

with open("starbucks",'w',encoding='utf-8') as outfile:
    outfile.write(soup.prettify())
result_seoul=soup.select("div#mCSB_3_container > ul.quickSearchResultBoxSidoGugun > li.quickResultLstCon > p")
for location in result_seoul:
    print(location.text) # -> string은 태그 내 문자열을 반환하는데 태그 내에 하위 태그가 두개이상일경우 무엇을 반환해야하는지 명확하지 않아서 None을 반환
    result.append(location.text)
    

