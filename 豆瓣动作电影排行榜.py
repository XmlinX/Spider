import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://movie.douban.com/explore#!'
type = 'movie'
tag = "动作"
sort = 'recommend'
page_limit = 20
page_start = 0

data = {'type':type,
        'tag':tag,
        'sort': sort,
        'page_limit': page_limit,
        'page_start': page_start
        }
data = urllib.parse.urlencode(data)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
           }
url_ = url + data
print(url_)
request = urllib.request.Request(url=url_, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)