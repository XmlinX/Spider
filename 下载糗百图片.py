#coding=utf-8
import urllib.request
import re
import ssl
import os


def handle_url(url, page):
    url = url + str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def handle_content(request):
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    pattern = re.compile(r'<div class="thumb">.*?<img src=(.*?) '
                         r'alt=.*?></div>', re.S)
    src_list = pattern.findall(html)
    for src in src_list:
        src.strip('"')
        image_url = 'https:'+src
    return image_url


def download_image(image_url):
    dir_path = '/Users/xiameilin/qiubai'
    file_name = os.path.basename(image_url)
    file_path = os.path.join(dir_path, file_name)
    urllib.request.urlretrieve(image_url, file_path)
    print(file_path + 'ä¸‹è½½å®Œæ¯•')