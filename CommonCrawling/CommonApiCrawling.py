import pandas as pd
import urllib
import urllib.request
import json
import datetime



ServiceKey = "nXd5MQbl1v8mEzMMjMMr+m8GQ542nme4N0b2saxiCv/XVasaBsWFgF6MAxtZDYcqylEjixzwj/aMKo2wpQVSkA=="
def getTourismStatsItem(yyyymm,nat_cd,ed_cd):
    service_url="http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?_type=json&"
    service_url=service_url+"YM={}".format(str(yyyymm))
    service_url=service_url+"&NAT_CD={}".format(int(nat_cd))
    service_url=service_url+"&ED_CD={}".format(str(ed_cd))
    url = service_url + "&serviceKey={}".format(ServiceKey)
    
    print(url) #엑세스 거부 여부 확인용 출력
    responseDecode = getRequestUrl(url)

    if(responseDecode==None):return None
    else: return json.loads(responseDecode)    


def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode()==200:
            print("{} Url Request Success".format(str(datetime.datetime.now())))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("{} Error for URL: {}".format(str(datetime.datetime.now()),str(url)))
        return None

def getTourismStatsService(nat_cd,ed_cd,nStartyear,nEndYear):
    jsonResult = []
    result = []
    natName = ''
    dataEND="{0}{1:0>2}".format(str(nEndYear),str(12)) # 수집할 데이터의 끝 날짜인 dataEND를 nEndYear의 12월로 설정한다
    isDataEnd = 0 #데이터 끝 플래그인 isDataEnd
    for year in range(nStartyear, nEndYear+1):
        for month in range(1,13):
            if(isDataEnd==1): break
            yyyymm = "{0}{1:0>2}".format(str(year),str(month))
            jsonData = getTourismStatsItem(yyyymm,nat_cd,ed_cd)
            print(jsonData['response']['header']['resultMsg'])
            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                if jsonData['response']['body']['items'] == '':
                    isDataEnd = 1
                    dataEND = "{0}{1:0>2}".format(str(year),str(month-1))
                    print("데이터 없음.... \n 제공되는 통계 데이터는 {}년 {}월까지입니다.".format(str(year),str(month-1)))
                    break
                print(json.dumps(jsonData,indent=4,sort_keys=True,ensure_ascii=False))
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ','')
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']
                print(ed)
                print('[ {}_{} : {}]'.format(str(natName), str(yyyymm), str(num)))
                print('----------------------------------------------------')
                jsonResult.append({'nat_name': natName,'nat_cd': nat_cd,'yyyymm': yyyymm, 'visit_cnt': num})
                result.append([natName,nat_cd,yyyymm,num])
            
    return jsonResult,result,natName,ed,dataEND


def main():
    jsonResult = [] # 수집한 데이터를 저장할 리스트 객체로 JSON 파일 저장용
    result = []     # 수집한 데이터를 저장할 리스트 객체로 csv 파일 저장용
    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국: 112 / 일본: 130/ 미국: 275) : ')
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
    ed_cd = "E" #E : 방한외래관광객, D : 해외출국
    jsonResult,result,natName,ed,dataEND = getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)
    
    #파일저장1 : json파일
    with open('./{}_{}_{}_{}.json'.format(natName, ed, nStartYear, dataEND),'w',encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult,indent = 4, sort_keys=True,ensure_ascii=False)
        outfile.write(jsonFile)
    
    columns = ["입국자국가", "국가코드", "입국연월", "입국자 수 "]
    result_df= pd.DataFrame(result,columns=columns)
    result_df.to_csv('./{}_{}_{}_{}.csv'.format(str(natName),str(ed),int(nStartYear),int(dataEND)),index=False, encoding ='cp949')


if __name__=='__main__':
    main()