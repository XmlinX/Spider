#coding=utf-8
import urllib.request
import urllib.parse
import ssl
from lxml import etree
import os
import codecs
import re
import pymysql
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
base_url = 'https://book.douban.com/latest?'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
data = {
        'icn':'index-latestbook-all'
    }
data = urllib.parse.urlencode(data)
url = base_url + data
requests = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(requests)
html = response.read().decode('utf8')
html_tree = etree.HTML(html)
soup = BeautifulSoup(html,'lxml')
pattern = re.compile(r'[a-zA-Z]*://[^\s]*?.jpg', re.S)
#获取书名
b_name1 = html_tree.xpath("/html[@class='ua-mac ua-webkit book-new-nav']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-12-12 clearfix']/div[@class='article']/ul[@class='cover-col-4 clearfix']/li/div[@class='detail-frame']/h2/a/text()")
b_name2 = html_tree.xpath("/html[@class='ua-mac ua-webkit book-new-nav']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-12-12 clearfix']/div[@class='aside']/ul[@class='cover-col-4 pl20 clearfix']/li/div[@class='detail-frame']/h2/a/text()")
b_name_all = b_name1 + b_name2
#获取书的作者
# b_score = html_tree.xpath("/html[@class='ua-mac ua-webkit book-new-nav']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-12-12 clearfix']/div[@class='article']/ul[contains(@class,'cover-col-4')]/li/div[@class='detail-frame']/p[@class='rating']/span[@class='font-small  color-lightgray']/text()")
# print(b_score)
#获取书籍评分
scores = soup.find_all('span',class_='font-small color-lightgray')
b_score_all = []
for i in scores:
    score = i.string.strip()
    b_score_all.append(score)   
b_detail = soup.find_all('p',class_='color-gray')
b_url_all = pattern.findall(html)
db = pymysql.connect(host='192.168.0.100',
                    port=3306,
                    user='root',
                    passwd='xml@195468',
                    db='my_collections',
                    charset='utf8')
cur = db.cursor()
sql = '''insert into douban_collections (id,b_name,b_author,
b_score,au_country,b_url,b_pub_time,b_pub_house) values (%s,%s,%s,%s,%s,%s,%s,%s)'''
id = 1
for i in len(b_name_all):
    b_name = b_name_all[i]
    b_author = b_detail[i].string.split()[-5]
    b_score = b_score_all[i]
    if len(b_detail[i].string.split())==6:
        au_country = b_detail[i].string.split()[-6]
    else:
        au_country = ''
    b_url = b_url_all[i]
    b_pub_time = b_detail[i].string.split()[-1]
    b_pub_house = b_detail[i].string.split()[-3]
    #print(id,b_name,b_author,b_score,au_country,b_url,b_pub_time,b_pub_house)
    try:
        cur.execute(sql,(id,b_name,b_author,b_score,au_country,b_url,b_pub_time,b_pub_house))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    id +=1
    print(id,b_name,b_author,b_score,au_country,b_url,b_pub_time,b_pub_house)

cur.close()
db.close()
print('insert success')







