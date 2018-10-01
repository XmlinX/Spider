#coding=utf-8
from urllib import request
import urllib.parse
import ssl
import re
import os

url = 'https://www.doutula.com/photo/list/?'
ssl._create_default_https_context = ssl._create_unverified_context

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
           }
params = {'page': 2}
page_url = url + urllib.parse.urlencode(params)
req = request.Request(url=page_url, headers=headers)
response = request.urlopen(req)
html = response.read().decode('utf-8')
image_url_list = []
'''将正则表达式编译成Pattern对象'''
pattern = re.compile(r'[a-zA-Z]*://[^\s]*', re.S)
result = pattern.findall(html)

for i in result:
    base_url = i.strip('"')
    if base_url.endswith('jpg'):
        image_url_list.append(base_url)
    elif base_url.endswith('dta'):
        image_url_list.append(base_url)
    elif base_url.endswith('gif'):
        image_url_list.append(base_url)
    else:
        pass

for image_url in image_url_list:
    filename = image_url.split('/')[-1]
    if filename.endswith('!dta'):
        image_name = filename.strip('!dta')
    else:
        image_name = filename
    print(image_name)
    file_path = os.path.join('/Users/xiameilin/qiubai', image_name)
    urllib.request.urlretrieve(image_url, filename=file_path)
