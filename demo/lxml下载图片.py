#coding=utf-8
import urllib.request
from urllib import parse
import os
from lxml import etree


def handle_url(url):
    headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


# def download_image(image_url,name_list):
#     dirpath = '/Users/xiameilin/saotu'
#     for i in range(len(name_list)):


def handle_data(request):
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    html_tree = etree.HTML(html)
    image_url = html_tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    name_list = html_tree.xpath('//div[@id="container"]/div/div/a/@alt')
    return image_url,name_list