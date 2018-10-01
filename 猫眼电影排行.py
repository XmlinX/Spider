import requests
import os
import ssl
import re

base_url = 'https://maoyan.com/board/4'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

data = {'offset': 0}
s = requests.Session()
req = requests.Request('GET', url=base_url, data=data, headers=headers)
prepped = s.prepare_request(req)
response = s.send(prepped)
html = response.text
pattern = re.compile('<dd>.*?class="board-index.*?">('
                     '\d+)</i>.*?<a.*?title="(.*?)".*?<img '
                     'data-src="(.*?)".*?<p class="star">(.*?)</p>.*?<p '
                     'class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)'
                     '</i><i class="fraction">(\d)</i>', re.S)
items = pattern.findall(html)
for item in items:
    index = item[0]
    image = item[1]
    title = item[2]
    actor = item[3]
    time = item[4]
    score = item[5].strip()+item[6].strip()
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write()