import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

rank = 6
driver = webdriver.Chrome('C:\Chrome Driver\Chrome Driver.exe')

driver.get('https://member.inven.co.kr/user/scorpio/mlogin')
driver.implicitly_wait(10)
driver.find_element_by_name('user_id').send_keys('ziznaki')

driver.find_element_by_name('password').send_keys('cwsok045')
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

# ------------------------------------------------------------
driver.find_element_by_xpath('//*[@id="comHeadlink"]/div[2]/a[2]').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
title_list = soup.find("div", class_='hiddenArea')
for title in title_list.select("a"):
    print(title.getText())
