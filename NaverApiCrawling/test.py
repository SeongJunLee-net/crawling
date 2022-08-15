from urllib.request import urlopen    
response = urlopen('http://www.naver.com')  
print(response.read().decode("utf-8"))