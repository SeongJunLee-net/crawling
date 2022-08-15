import requests
import json
url = requests.get("https://openapi.naver.com/v1/search/news")
text = url.text
print(type(text))
"""
requests라이브러리에는 URL을 매개 변수로 취한 다음GET요청을 지정된 URL로 보내는get()이라는 메소드가 있습니다.
서버에서받은 응답은url이라는 변수에 저장됩니다.
url변수 내에 저장된이 응답은url.text와 같은.text메소드를 사용하여 문자열로 변환해야합니다. 그런 다음 결과를text변수에 저장합니다. 
text변수의 유형을 인쇄하면<class 'str'>유형이됩니다.
"""
data = json.loads(text)
print(type(data))

user = data.keys()
print(user)
#print(user['errorMessage'])

