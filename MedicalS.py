from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

question = []
rank = 10
driver = webdriver.Chrome('C:\Chrome Driver\Chrome Driver.exe')
url1 = 'https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EC%B9%98%EB%A3%8C&c_id=&c_name=&sm=tab_pge&kin_start={}'


driver.get('https://naver.com')
keyword = '치료'
driver.implicitly_wait(10)

driver.find_element_by_id('query').send_keys(keyword)
driver.implicitly_wait(10)
driver.find_element_by_id('search_btn').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="main_pack"]/div[8]/div[2]/a').click()

html1 = driver.page_source
soup1 = BeautifulSoup(html1, 'html.parser')

for t in soup1.find_all('dt', 'question'):
    question.append(t.get_text().strip().replace('질문','\n'))

for i in range(rank):
    print('%s' % (question[i]))






# -------------------------------------------------------------- data Get


# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
# url = requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EC%B9%98%EB%A3%8C&c_id=&c_name=&sm=tab_pge&kin_start=61', headers=header)


# url_html = url.text
# text>html
# url_parse = BeautifulSoup(url_html, 'html.parser')
# parse
# for t in url_parse.find_all('dt', 'question'):
#     question.append(t.get_text().strip().replace('질문',''))
#
# for i in range(rank):
#     print('%s' % (question[i]))
