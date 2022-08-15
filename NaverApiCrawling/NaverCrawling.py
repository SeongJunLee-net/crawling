import json
import urllib.request
import urllib.parse
import datetime
import os
import sys
import time
client_id='DJwmrDkykCEG56iJJ5Zv'
client_secret='E1dX6NlhqY'
def main():
    node = 'news' #네이버 뉴스 검색을 위해 검색 API 대상을 'news'로 설정
    srcText = input('검색어를 입력하세요: ')
    #파이썬 쉘창에서 검색어를 입력받아 srcText에 저장한다.
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node,srcText,1,100)
    print(jsonResponse)
    total = jsonResponse['total']
    #getNaverSearch()함수를 호출하여 start = 1, display = 100에 대한
    #검색결과를 반환받아 jsonResponse에 저장한다.
    

    #display는 '검색 결과 출력 건수 지정'을 의미함
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post,jsonResult,cnt)
            #jsonResponse(검색결과)에 데이터가 있는동안 for문으로
            #결과를 하나씩 처리하는 작업(getPostData)를 반복한다

        start = jsonResponse['start'] + jsonResponse['display']
        # 다음 검색 결과 100개를 가져 오기 위해 start 위치를 변경한다
        jsonResponse = getNaverSearch(node,srcText,start,100)


    print('전체검색 : {}건'.format(total))
    with open('{0}_naver_{1}.json'.format(srcText, node),'w',encoding='UTF-8') as outfile:
        jsonFile= json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        ###  json encoding ! ###
        # json.dumps로 파이썬 데이터를 json 포맷 데이터를 만들어 놓음
        # indent는 들여쓰기
        # sort_keys는 key를 기준으로 정렬
        # ensute_ascii가 true(default값)이면 ascii코드가 아닌것을 escape한다
        outfile.write(jsonFile)
    
    print("가져온 데이터 : {}".format(cnt))
    print('{0}_naver_{1}.json SAVED'.format(srcText,node))


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)
    """
    urlopen은 string이나 Request 객체인 URL을 열어준다. 수많은 옵션들이 있지만,
    사실 대부분 url을 많이 쓴다. 예시를 통해 이해해보자. 
    url부분만 넣어서 보내면 html을 돌려준다. read를 통해 읽을 수 있다.
    실제로 결과 값을 보고 싶다면 read 함수를 실행해 주면 된다. 이때 아래와 같이 decode를 하지 않으면 인코딩된 페이지의 결과가 보이지 않기 때문에 읽기가 어렵다.
    -------------------------------------------
    from urllib.request import urlopen    
    response = urlopen('http://www.naver.com')  
    response.read().decode("utf-8")
    --------------------------------------------
    urlopen 함수에 URL을 바로 넣어도 되고, Request 클래스에 URL을 넣은 뒤에
    req를 생성해서 urlopen 함수에 넣어도 됩니다.
    """
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200: #200이면 정상 400이면 비정상
            print("{} Url Request Success".format(datetime.datetime.now()))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("{} Error for URL : {}".format(datetime.datetime.now(),url))
        return None

def getNaverSearch(node,srcText,start,display):
    base = "https://openapi.naver.com/v1/search"
    node ="/{}.json".format(str(node))
    parameters = "?query={0}&start={1}&display={2}".format(
        urllib.parse.quote(srcText) ,str(start),str(display)
    )
    print(parameters)
    #urllib.parse.quote()는 아스키코드 형식이 아닌 글자를 URL 인코딩 시켜줍니다
    #url 구성 요소를 보면 다음과 같이 나타낼수 있다\
    #뛰어쓰기 하나하나가 url을 작동 안시킬수도 있다
    """
    1. 프로토콜
    2. 호스트주소
    3. 포트번호 
    4. 경로
    5. ?
    6. 쿼리
    ------------------------------
    https://leesungjoon.com/products/201900278?itemid=200
    프로토콜(://) -> https
    호스트주소(:)포트번호(/) -> leesungjoon.com
    경로(?) -> 201900278
    쿼리 -> itemid=200
    ------------------------------
    1. 프로토콜
    컴퓨터끼리 네트워크 통신을 할때 규격이다
    2. 호스트 주소 
    컴퓨터의 주소를 표시하는 영역
    3. 포트 번호
    포트번호는 컴퓨터에서 실행되고 있는 수많은 프로세스들의 주소,
    그런데 우리가 사용하는 url에는 포트번호가 보이지 않는다
    기본적으로 포트번호를 입력하지 않을경우에는 기본 포트번호가 적용된다
    HTTP의 경우 80번 HTTPS의 경우 443번의 포트번호가 적용된다
    따라서 https://www.naver.com 은 https://www.naver.com:443
    으로 봐도 무방하다
    4. 경로
    경로는 서버 프로그램 내에 짜인 로직으로 가는 영역이다.
    서버를 개발할때는 이 경로에 맞춰 코드를 짠다
    5. query
    쿼리는 url에서 추가적인 데이터를 표현할때 사용된다
    path뒤에 ?을 기점으로 key=vlaue 형태로 데이터를 표현한다
    """

    url = base + node + parameters
    responseDecode = getRequestUrl(url)
    

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)
        ###  json decoding ! ###
        #json 디코딩은 json.loads() 메서도를 사용해 문자열을 python타입으로 변경한다

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'],'%a, %d %b %Y %H:%M:%S +0900')
    # %a: 요일을 로케일의 축약된 이름으로 Ex> Sun, Mon, Sat
    # %d: 월중 일을 0으로 채워진 10진수로 Ex> 01,02,.., 31
    # %b: 월을 로케일의 축약된 이름으로 Ex> Jan,Feb,.. Dec
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    #날짜와 시간(datetime)을 문자열로 출력하려면 strftime
    #날짜와 시간 형식의 문자열을 datetime으로 변환하려면 strptime을 사용
    jsonResult.append({'cnt':cnt, 'title':title,'description':description,
                       'org_link':org_link, 'link':org_link, 'pDate':pDate})
    return


if __name__ == '__main__':
    main()
