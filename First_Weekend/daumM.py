from bs4 import BeautifulSoup
import requests
import time
from multiprocessing import Pool
url1 = 'https://search.daum.net/search'


question = []
start_time = time.time()
for page in range(1, 10) :
    parameter = {
        'q': '치료',
        'w': 'knowledge',
        # 'page': (page-1)*10+1,
        'page' : (page - 1) + 1,
    }
    response = requests.get(url1, params=parameter)
    html = response.text
    source = BeautifulSoup(html, 'html.parser')
    questions = source.find_all('a', 'f_link_b')

    for question in questions:
        print(question.get_text().strip())

print("--- %s seconds ---" % (time.time() - start_time))

