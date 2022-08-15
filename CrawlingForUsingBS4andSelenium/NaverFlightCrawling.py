import time
from unittest import result
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome("C:\WebDriver\chromedriver.exe")

browser.get("https://flight.naver.com/")
time.sleep(3)
browser.find_element_by_class_name("tabContent_route__1GI8F.select_City__2NOOZ.start").click()
time.sleep(0.5)
browser.find_element_by_class_name("autocomplete_input__1vVkF").send_keys("대한민국")
time.sleep(0.5)
browser.find_elements_by_class_name("autocomplete_search_item__2WRSw")[0].click()
time.sleep(0.5)

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
time.sleep(0.5)
browser.find_element_by_class_name("autocomplete_input__1vVkF").send_keys("미국")
time.sleep(0.5)
browser.find_elements_by_class_name("autocomplete_search_item__2WRSw")[1].click()
time.sleep(0.5)
browser.find_elements_by_class_name("tabContent_option__2y4c6.select_Date__1aF7Y")[0].click()
time.sleep(0.5)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/button").click()
time.sleep(0.5)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button").click()  
time.sleep(0.5)
browser.find_element_by_class_name("searchBox_search__2KFn3").click()
# 드라이버가 실행이 다되기전에 코드가 실행되는 경우가 발생하므로 안될경우에 time으로 딜레이를 줘보자
# f12로 확인을 하다보면 클래스명에 띄어쓰기가 있는경우가 있다. 이때 해당 기능에 커서를 올리면 정확한 클래스 name을 알수있다
# 복잡한경우 xpath를 활용하자

# 로딩이 되는동안 코딩이 진행돼서 검색이 안되는 경우도 있다
# 이경우 해결방법은 두가지 인데
# 그냥 무작정 기다리는 경우가 있고
# 두번째는 기다리는 도중에 로딩이 끝나면 동작을 처리 하라고 할수있다
    # 필요한 import
    # -from selenium.webdriver.common.by import By
    # -from selenium.webdriver.support.ui import WebDriverWait
    # -from selenium.webdriver.support import expected_conditions as EC
### 3:35

try:
    WebDriverWait(browser,40).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[5]/div/div[3]/div[1]/div/button")))
    # presence_of_element_located(tuple) 어떤 엘리먼트가 위치할때까지 기다려줘라   
    # tuple에 들어가는것은 ID,XPATH,CLASS_NAME,LINK_TEXT 등이 사용 가능하다
    element = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[5]/div/div[3]/div[1]/div/div[1]/div")
    print(element.text)
finally:
    browser.quit()

# elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[5]/div/div[3]/div[1]/div/button")
# print(elem.text)




