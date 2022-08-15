from bs4 import BeautifulSoup
# API가 없는 웹 페이지에서 크롤링을 하려면 웹 페이지의 HTML 구조를 분석한 뒤 필요한 데이터를 직접 크롤링해야 한다.
# 웹 페이지의 HTML구조를 분석하는 작업을 HTML Parsing 이라고 한다

###TOY HTML###
html ='<h1 id="title">한빛출판네트워크</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html"class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li><li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify()) 
# 우리는 HTML 구조를 분석할 것이므로 분석기를 'html.parser'로 지정하였다.
# prettify함수를 사용하여 객체 soup에 저장된 내용을 HTML 문서 형태로 출력하여 확인한다
"""
<h1 id="title">
 한빛출판네트워크
</h1>
<div class="top">
 <ul class="menu">
  <li>
   <a class="login" href="http://www.hanbit.co.kr/member/login.html">
    로그인
   </a>
  </li>
 </ul>
 <ul class="brand">
  <li>
   <a href="http://www.hanbit.co.kr/media/">
    한빛미디어
   </a>
  </li>
  <li>
   <a href="http://www.hanbit.co.kr/academy/">
    한빛아카데미
   </a>
  </li>
 </ul>
</div>

"""
tag_h1 = soup.h1 #soup에 저장된 태그 중에서 첫번째 h1 태그 한개만 파싱하여 반환하기
tag_div = soup.div #soup에 저장된 태그 중에서 첫번째 div 태그 한개만 파싱하여 반환하기
tag_ul = soup.ul #soup에 저장된 태그 중에서 첫번째 ul 태그 한개만 파싱하여 반환하기
tag_li = soup.li #soup에 저장된 태그 중에서 첫번째 li 태그 한개만 파싱하여 반환하기
tag_a = soup.a #soup에 저장된 태그 중에서 첫번째 a 태그 한개만 파싱하여 반환하기

tag_ul_all = soup.find_all("ul") #soup에 저장된 태그중에서 ul 태그를 모두 찾아 '리스트' 로 반한하기
print(tag_ul_all)

tag_li_all = soup.find_all("li")
print(tag_li_all)

tag_a_all = soup.find_all("a")
print(tag_a_all)

### 다음과 같은 속성을 이용하여 파싱 할수도 있다 ###
# attrs: 속성 이름과 속성값으로 딕셔너리 구성
# find(): 속성을 이용하여 특정 태그 파싱
# select(): 지정한 태그를 모두 파싱하여 리스트 구성
#     - 태그#id 속성값
#     - 태그.class 속성값
print(tag_a.attrs) # 한 태그에 대해서 속성의 이름과 값으로 딕셔너리를 구성 EX> <a href(속성이름)="http://www.naver.com(속성값) class(속성이름)="top"(속성값)>
print(tag_div.attrs)

print(type(tag_div.attrs['class'])) #태그 의 속성중 클래스는 리스트 형태로 반환된다

tag_ul_2 = soup.find('ul',attrs={'class':'brand'})
print(tag_ul_2)
print(type(tag_ul_2)) #<class 'bs4.element.Tag'>
print(tag_ul_2.string) #->None

# tag_ul_3 = soup.find('ul')
# print(tag_ul_3)

# tag_a_all2= soup.find('a')
# print(tag_a_all2)

#-> find에 태그값만 입력하면 soup.(태그) 처럼 가장 처음에 있는 태그 하나만 반환한다

title = soup.find('h1',id="title")
print(title)
print(title.string) # 태그가 한개뿐 인것은 string 속성을 사용해서 string을 추출할 수 있다
print(type(title)) #<class 'bs4.element.Tag'>

li_list = soup.select("div>ul.brand>li") #div 태그 블록 안에서 'ul'태그인것중에서 'class' 속성값이 'brand'인 블록 안의 'li'태그 블록을 모두 추출해서 리스트로
print(li_list)


for li in li_list:
    print(li.string)
    print(type(li)) # li_list는 <class 'bs4.element.Tag'>를 모아놓은 리스트

li2_list = soup.select("h1#title")
print(li2_list)

### 크롤링 허용 여부 확인하기 ###
# 크롤링 허용 여부를 확인하기 위해 주소창에 '크롤링할 주소/robots.txt'를 입력한다 robots.txt는 검색 엔진이나 웹 크롤러 등의 웹 로봇이 
# 사이트를 방문했을 때 사이트의 수집 정책을 알려주기 위해 사용한다


### 전국 할리스 매장정보 찾기 ###
## www.hollys.co.kr의 크롤링 허용 여부
# User-agent: *

# Disallow: /membership 

# Disallow: /myHollys

# -> 멤버십과 myHollys를 제외하곤 크롤링이 가능하다

"""
EX>
<tr>
				<!--
				<td class="noline center_t">
																<a href="javascript:goLogin();"><img src="https://www.hollys.co.kr/websrc/images/store/ico_favorite_off.png" alt="즐겨찾기"></a>
									</td>
				 -->
				<td class='noline center_t'>경기 이천시</td>
				<td class='center_t'><a href="#" onclick="javascript:storeView(1001); return false;">이천마장점</a></td>
				<td class='center_t tdp0'>영업중</td>
				<td class='center_t'><a href="#" onclick="javascript:storeView(1001); return false;">경기도 이천시 마장면 오천로 65 오천리 56-55</a></td>
				<td class='center_t'>
																																														<img src='https://www.hollys.co.kr/websrc/images/store/img_store_s08.png' style='margin-right:1px' alt='주차' />
									</td>
				<td class='center_t'>070-4647-0081</td>
			</tr>

    td[0]는 매장이 있는지역
    td[1]는 매장이름
    td[2]는 영업정보
    td[3]는 매장 주소
    td[5]는 매장 전화번호
"""
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pandas as pd
result = []

#my self code

# for page in range(1,54):
#     Hollys_url = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={}&sido=&gugun=&store=".format(page)
#     print(Hollys_url)
#     url = urllib.request.Request(str(Hollys_url))
#     html = urllib.request.urlopen(url)
#     hollys_soup=BeautifulSoup(html,'html.parser')
#     hollys_name=hollys_soup.select("div.tableType01 > table.tb_store > tbody > tr > td.center_t > a")
#     # 태그 내 특정 속성 값
#     # 태그 내에 속성 명을 가지고 지정하는 방법입니다.
#     # soup.select('태그[속성명 = 속성값]') 방식으로 사용하면 된다
#     print(hollys_name)
#     hollys_name=np.array(hollys_name).reshape(-1,2)
#     hollys_name=hollys_name[:,0].tolist()
#     print(hollys_name)
#     result.extend(hollys_name)


# print(result)


for page in range(1,54):
    Hollys_url = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={}&sido=&gugun=&store=".format(page)
    html = urllib.request.urlopen(Hollys_url)
    soupHollys = BeautifulSoup(html,'html.parser')
    tag_tbody = soupHollys.find('tbody')
    for store in tag_tbody.find_all('tr'):
        store_td = store.find_all('td')
        store_name = store_td[1].string
        store_sido = store_td[0].string
        store_address=  store_td[3].string
        store_phone = store_td[5].string
        result.append([store_name]+[store_sido]+[store_address]+[store_phone])
print(len(result))
print(result[0])


### 크롤링한 데이터를 CSV 파일에 저장해서 보관해두기 ###
## CSV 파일은 table 형식이므로 판다스의 데이터프레임을 사용해서 저장해야된다

hollys_tbl = pd.DataFrame(result, columns = ('store', 'sido-gu', 'address', 'phone'))
hollys_tbl.to_csv("C:\Programming\CrawlingForUsingBeautifulSoup\hollys.csv",mode = "w", index = True)
"""
df.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None,
mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None,
doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)

***path_or_buf : csv파일이 생성되는 경로와 파일명 입니다.
***sep : csv 파일의 구분자 입니다. 기본값은 ' , ' 입니다.
***na_rep : 결측값을 어떻게 출력할지 지정할 수 있습니다. 기본값은 공백 입니다.
float_format : 부동소수점의 경우 어떤 형식으로 출력할지 지정할 수 있습니다.
***columns : 출력할 열을 지정하는 인수 입니다.
***header : 열 이름을 설정합니다. False일 경우 열 이름을 출력하지 않습니다.
***index : 인덱스의 출력 여부 입니다. False일 경우 인덱스를 출력하지 않습니다.
index_label : 인덱스의 레이블(인덱스명)을 설정합니다.
***mode : {'w' / 'a'} 쓰기 모드를 지정합니다. a로 지정할 경우 기존 파일 아래에 값을 추가하여 입력하게됩니다.
***encoding : 인코딩 설정입니다. 기본값은 utf-8입니다.
compression : {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None} 압축 설정을 지정합니다. 기본값은 'infer'로 적절한 압축형식을 추론합니다.
quoting : 값에 대해서 인용구 설정을 할 수 있습니다. 어떤 값에 대해서 인용구를 설정할지는 아래와 같습니다.
{0 : MINIMAL 문자와 특수문자 / 1 : ALL 모든필드 / 2 : NONNUMERIC 숫자가 아닌것 / 3 : NONE 안함}
quotechar : quoting에서 지정한 인용구에 대해서 인용구에 사용할 문자를 지정합니다. 기본값은 쌍따옴표 입니다.
chunksize : 한번에 불러올 행의 수를 지정합니다. 예를들어 100을 입력할 경우 한번에 100행씩 변환합니다. 속도 향상에 기여합니다.
***date_format : 값이 시계열(datetime) 데이터인 경우 그 값의 포맷을 지정합니다.(예 : '%Y-%m')
doublequoto : 값중에 quotechar과 같은 값이 있을때, 그 값을 인용구 처리할지의 여부 입니다.
escapechar : doublequoto=False인 경우 인용구와 중복되는 그 값을 어떤 값으로 변경할지 여부입니다.
decimal : 자리수로 쓰이는 문자를 지정합니다.즉, 100,000의 경우 decimal="."으로 할 경우100.000으로 표시합니다.
errors : 인코딩 오류에 대해서 오류 처리를 정할 수 있습니다. 가능한 값은 아래와 같습니다.
"""


 
