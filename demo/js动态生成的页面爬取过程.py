#coding=utf-8
import urllib.parse
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://movie.douban.com/explore#!'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
           }

'''对浏览器进行初始化'''
driver = webdriver.Chrome()
type = 'movie'
tag = "动作"
sort = 'recommend'
page_limit = 20
page_start = 0
for i in range(10):
    data = {'type': type, 'tag': tag, 'sort': sort, 'page_limit': page_limit, 'page_star': page_start}
    data = urllib.parse.urlencode(data)
    url_ = url + data
    html = driver.get(url_)
