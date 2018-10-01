#coding=utf-8
from bs4 import BeautifulSoup
import requests
import lxml
from urllib import request
from urllib import error
import ssl
import os
import threading

ssl._create_default_https_context = ssl._create_unverified_context
BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []
FACE_URL_LIST = []
gLock = threading.Lock()
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
           }
for i in range(1, 50):
    original_url = BASE_PAGE_URL + str(i)
    PAGE_URL_LIST.append(original_url)


def producer():
    while True:
        gLock.acquire()
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            gLock.release()
            response = requests.get(page_url, headers=headers)
            content = response.content
            soup = BeautifulSoup(content, 'lxml')
            img_list = soup.find_all('img', attrs={'class': 'img-responsive '
                                                            'lazy image_dta'
                                                   })
            gLock.acquire()
            for img in img_list:
                img_url = img['data-original']
                FACE_URL_LIST.append(img_url)
            gLock.release()


def customer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = url.split('/')
            name = split_list.pop()
            if name.endswith('!dta'):
                filename = name.strip('!dta')
            else:
                filename = name
            path = os.path.join('/Users/xiameilin/doutu',filename)
            try:
                request.urlretrieve(url, filename=path)
            except error.URLError as e:
                print(e.reason)


if __name__ == '__main__':
    for x in range(3):
        thread_producer = threading.Thread(target=producer)
        thread_producer.start()
    for x in range(5):
        thread_customer = threading.Thread(target=customer)
        thread_customer.start()