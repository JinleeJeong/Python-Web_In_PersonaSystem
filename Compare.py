from bs4 import BeautifulSoup
import requests
import time
from threading import Thread


def do_work(start, end, result):

    url1 = 'https://search.naver.com/search.naver'

    question = []

    for page in range(1, 50) :
        parameter = {
            'query': '통증',
            'where': 'kin',
            'kin_start': (page-1)*10+1,
        }
        response = requests.get(url1, params=parameter)
        html = response.text
        source = BeautifulSoup(html, 'html.parser')
        questions = source.find_all('dt', 'question')


        for question in questions:
            print(question.get_text().strip().replace("질문",""))

    return

if __name__=='__main__':
    START, END = 0, 2000000
    result = list()
    s_time = time.time()


    th1 = Thread(target=do_work, args=(START, END/2, result))
    th2 = Thread(target=do_work, args=(START,END,result))
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    sum = 0

    print ('time = ', time.time()-s_time)
