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
driver.get("https://it.inven.co.kr/")


header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
url = requests.get("http://it.inven.co.kr/", headers=header)

html = url.text
soup = BeautifulSoup(html, 'html.parser')

title_list = soup.find("div", class_='hiddenArea')
for title in title_list.find_all("a"):
    print(title.getText())
