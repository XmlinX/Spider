'''使用Xpath解析下载的网页'''
import urllib.request
import urllib.parse
import ssl
from lxml import etree
import os
import codecs

ssl._create_default_https_context = ssl._create_unverified_context


def get_url(base_url):
    data = {
        'icn':'index-latestbook-all'
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    return url


def get_page(url):
    headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    requests = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(requests)
    html = response.read().decode()
    return html


def analyze_page(html):
    html_tree = etree.HTML(html)
    #获取所有的书名
    book_name = html_tree.xpath("/html[@class='ua-mac ua-webkit book-new-nav']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-12-12 clearfix']/div[@class='article']/ul[@class='cover-col-4 clearfix']//li/div[@class='detail-frame']/h2/a/text()")
    #author = html_tree.xpath("/html[@class='ua-mac ua-webkit book-new-nav']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-12-12 clearfix']/div[@class='article']/ul[@class='cover-col-4 clearfix']//li/div[@class='detail-frame']/p[@class='color-gray']")
    return book_name


def save_spider(book_name):
    file_path = os.path.join('/Users/xiameilin/personal/Data_Learning/Spider', 'book_name.txt')
    with codecs.open(file_path, 'a', encoding='utf-8') as f:
        for name in book_name:
            f.write(name + '\n')

if __name__ == '__main__':
    base_url = 'https://book.douban.com/latest?'
    url = get_url(base_url)
    print(url)
    html = get_page(url)
    book_name = analyze_page(html)
    save_spider(book_name)
