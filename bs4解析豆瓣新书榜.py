import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://book.douban.com/latest?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
          }
data = {'icn': 'index-latestbook-all'}
data = urllib.parse.urlencode(data)
url = url + data
requests = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(requests)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('a'))