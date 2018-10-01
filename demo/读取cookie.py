#coding=utf-8
import urllib.request
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.baidu.com'

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar()
cookie.load(filename, ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)



