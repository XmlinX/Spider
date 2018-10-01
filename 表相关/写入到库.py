import pymysql


id = 1
name = 'jeiwang'
author = 'jsonxia'
score = 9.65
country = 'beijing'
url = 'http://www.baidu.com'
pub_time = '2018-08-24'
pub_house = 'zhongxingchubanshe'
image = None

db = pymysql.connect(host='192.168.0.64',
                     port=3306,
                     user='root',
                     passwd='xml@195468',
                     db='my_collections',
                     charset='utf8'
)
cur = db.cursor()
sql = '''insert into douban_collections (id,b_name,b_author,
b_score,au_country,b_url,b_pub_time,b_pub_house,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

try:
    cur.execute(sql,(id,name,author,score,country,url,pub_time,pub_house,image))
    db.commit()
except:
    db.rollback()
finally:
    cur.close()
    db.close()
    print('insert success')

