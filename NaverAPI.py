import urllib.request
import json

client_id = "Zj_DCYbRgGqqhripFXKm"
client_secret = "Q7KKdUgOcB"

encText = urllib.parse.quote("아플때")
url = "https://openapi.naver.com/v1/search/kin?query=" + encText + "&start=31" + "&display=100"  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8').replace("<b>", "").replace("</b>",""))
    retdata = response_body.decode('utf-8') #Decording Json > Python
    jsonresult = json.loads(retdata)
    for i in jsonresult['items']:
        print(i['title'].replace('<b>','').replace('</b>',''))
else:
    print("Error Code:" + rescode)