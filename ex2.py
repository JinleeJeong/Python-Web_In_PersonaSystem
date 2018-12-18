from bs4 import BeautifulSoup
import requests

rank = 20
header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
url = requests.get('https://www.naver.com', headers=header)

url_html = url.text
# text>html
url_parse = BeautifulSoup(url_html, 'html.parser')
# parse
list_1 = []

for t in url_parse.find_all("span", class_="ah_k"):
    list_1.append(t.get_text())

for i in range(rank):
        print('%2d위: %s ' % (i + 1, list_1[i]))