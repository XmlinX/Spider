#coding='utf-8'
import urllib.request
import ssl
import requests


url = 'https://www.baidu.com/'
headers = {'User‐Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3)'
                        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
'''全局取消证书验证'''
ssl._create_default_https_context = ssl._create_unverified_context
'''构造一个请求'''
#方法一
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
#方法二
request = urllib.request.Request(url=url)
request.add_header('User‐Agent', 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0')
response = urllib.request.urlopen(request)

urllib.request.urlretrieve(url=url,filename='baidu.html')
