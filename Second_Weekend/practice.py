from bs4 import BeautifulSoup
import requests

header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
news = requests.get('https://media.daum.net/economic/', headers=header)

new = news.text

soup = BeautifulSoup(new, 'html.parser')

tag = soup.select('strong.tit_thumb')

for i in tag:
    print(i.get_text())
