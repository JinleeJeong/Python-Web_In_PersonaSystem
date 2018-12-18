from bs4 import BeautifulSoup
import requests

rank = 20
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
url = requests.get('https://sports.news.naver.com/index.nhn', headers=header)

url_html = url.text
# text>html
url_parse = BeautifulSoup(url_html, 'html.parser')
# parse
ul = url_parse.find("ul", class_='main_ranknews_list')
for i in ul.find_all("a"):
    print(i.get_text())

