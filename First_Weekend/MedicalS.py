from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

question = []
rank = 10
driver = webdriver.Chrome('C:\Chrome Driver\Chrome Driver.exe')

driver.get('https://naver.com')
keyword = '치료'
driver.implicitly_wait(10)

driver.find_element_by_id('query').send_keys(keyword)
driver.implicitly_wait(10)
driver.find_element_by_id('search_btn').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="main_pack"]/div[8]/div[2]/a').click()

html1 = driver.page_source # 페이지를 동적으로 가져와서 크롤링 가능하게 함 (현재 페이지)
soup1 = BeautifulSoup(html1, 'html.parser')

for t in soup1.select('dt > a'):
    question.append(t.get_text().strip().replace('질문','\n'))

for i in range(rank):
    print('%s' % (question[i]))
