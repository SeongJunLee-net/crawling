
###selenium 사용법###
# >>> from selenium import webdriver
# >>> browser = webdriver.Chrome("C:\WebDriver\chromedriver.exe")

# DevTools listening on ws://127.0.0.1:56923/devtools/browser/97dcfb93-c986-4096-a712-1671d4524147
# >>> [12048:9148:0813/162221.504:ERROR:device_event_log_impl.cc(214)] [16:22:21.504] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
# [12048:9148:0813/162221.511:ERROR:device_event_log_impl.cc(214)] [16:22:21.511] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)   
# browser.get("http://naver.com")
# >>> [12048:9428:0813/162319.368:ERROR:util.cc(127)] Can't create base directory: C:\Program Files\Google\GoogleUpdater
# [7604:13228:0813/162419.414:ERROR:gpu_init.cc(486)] Passthrough is not supported, GL is disabled, ANGLE is 
# element = browser.find_element_by_class_name("link_login")
# >>> element
# <selenium.webdriver.remote.webelement.WebElement (session="24695be846adb8dec7cb1ec217197dc5", element="71e2fea5-125f-46d8-a0e2-57f0d59fab59")>
# >>> element.click()
# >>> browser.back()
# >>> browser.forward()
# >>> browser.refresh()
# >>> browser.back()
# >>> element = browser.find_element_by_id("query")
# >>> element
# <selenium.webdriver.remote.webelement.WebElement (session="24695be846adb8dec7cb1ec217197dc5", element="965ee902-6321-42c9-a390-754ad5d469eb")>
# >>> from selenium.webdriver.common.keys import Keys
# >>> element.send_keys("이준석")
# >>> element.send_keys(Keys.ENTER)


# # ---------------------------------------
# >>> element=browser.get("http://daum.net") 
# >>> browser.get("http://daum.net")
# >>> element = browser.find_element_by_name("q")
# >>> from selenium.webdriver.common.keys import Keys    
# >>> element.send_keys("이성준")
# >>> element.send_keys(Keys.ENTER) 
# >>> browser.back()
# >>> element = browser.find_element_by_xpath("//*[@id="daumSearch"]/fieldset/div/div/button[3]")
#   File "<stdin>", line 1
#     element = browser.find_element_by_xpath("//*[@id="daumSearch"]/fieldset/div/div/button[3]")
#                                             ^^^^^^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> element = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[3]")
# >>> element
# <selenium.webdriver.remote.webelement.WebElement (session="24695be846adb8dec7cb1ec217197dc5", element="e2fa170c-86a4-447f-b246-3a11a6d4a740")>
# >>> element.click()
# >>> browser.close() #브라우저중 탭하나를 닫는것
# >>> browser.quit() #브라우저를 아예 닫는것

### Selenium을 활용한 네이버 자동로그인 ###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome("C:\WebDriver\chromedriver.exe")
# 1. 네이버 이동
browser.get("http://www.naver.com")

# 2. 로그인 버튼 클릭
elem1 = browser.find_element_by_class_name("link_login")
elem1.click()
# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("dsd0919")
browser.find_element_by_id("pw").send_keys("a@a@0919")
# 4. 로그인 버튼 클릭
browser.find_element_by_class_name("btn_login").click()

time.sleep(3)
# 5. id를 새로 입력
# id 가 자동저장 되므로
#browser.find_element_by_id("id").clear()
#browser.find_element_by_id("id").send_keys("")

# 6. html 정보 출력
print(browser.page_source) #page_source를 하면 현재 페이지에 있는 모든 html 문서를 가져온다
 
#7. 브라우저 종료
# browser.close() 현재 탭만 종료
# browser.quit()  전체 브라우저 종료