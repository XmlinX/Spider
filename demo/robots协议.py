#coding=utf-8
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
#读取robots.txt文件进行分析
rp.read()