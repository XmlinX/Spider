#coding=utf-8
from urllib.request import build_opener
from urllib.request import ProxyHandler
from urllib import error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

proxy_handler = ProxyHandler({
    'http': '192.168.1.120:9743',
    'https': '192.168.1.120:9743'
                            })

opener = build_opener(proxy_handler)
url = 'https://www.baidu.com/'
try:
    res = opener.open(url)
    print(res.read().decode('utf-8'))
except error.URLError as e:
    print(e.reason)