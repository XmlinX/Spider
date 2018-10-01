import urllib.request
import ssl


url = 'https://www.baidu.com/'

ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen(url=url)
print(type(response))
ret = response.read().decode('utf-8')
urllib.request.urlretrieve(url=url, filename='/Users/xiameilin/Downloads/baidu.html')
