import requests
from bs4 import BeautifulSoup

with requests.Session() as s:
    req = s.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select('h3 > a')
    # my_titles는 list 객체
    for title in my_titles:
        # Tag안의 텍스트
        print(title.text)
        # Tag의 속성을 가져오기(ex: href속성)
        print(title.get('href'))

        #Session()을 이용해 로그인 후 크롤링 가능능