import urllib.request
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.baidu.com'

'''将Cookie保存到变量中'''
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open(url)
# for item in cookie:
#     print('name = %s' % item.name)
#     print('value = %s' % item.value)

'''保存Cookie到文件'''

'''设置保存cookie的文件名，同级目录下的cookie.txt'''
filename = 'cookie.txt'

'''声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件'''
cookie = http.cookiejar.MozillaCookieJar(filename)

'''利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler'''
handler = urllib.request.HTTPCookieProcessor(cookie)

'''通过CookieHandler创建opener'''
opener = urllib.request.build_opener(handler)

response = opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)