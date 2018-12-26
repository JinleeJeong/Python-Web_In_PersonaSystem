from bs4 import BeautifulSoup
import requests

rank = 10
header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
melon = requests.get('https://www.melon.com/chart/index.htm', headers=header)
# 멜론차트 웹사이트
melon_html = melon.text
# text>html
melon_parse = BeautifulSoup(melon_html, 'html.parser')
# parse

titles = melon_parse.find_all("div", class_= "ellipsis rank01")
songs = melon_parse.find_all("div", class_= "ellipsis rank02")



title = []
song = []

for t in titles:
    title.append(t.find('a').text)
for s in songs:
    song.append(s.find('a').text)

for i in range(rank):
    if (i >= 10):
        print('-%3d위: %s  %s' % (i + 1, title[i], song[i]))
    else:
        print('Top 10 !! %3d위 : %s - %s' % (i + 1, title[i], song[i]))

