#coding=utf-8
from bs4 import BeautifulSoup
import bs4


soup = BeautifulSoup(open('/Users/xiameilin/personal/Data_Learning/Spider/demo/wechat.html',encoding='utf-8'),'lxml')
print(soup.decode('utf-8'))