#coding=utf-8
import re

content_full = 'Hello, my phone number is 010-86432100 and email is ' \
          'cqc@cuiqingcai.com, and my website is http://cuiqingcai.com.'

content1 = 'Hello 123 4567 World_This is a Regex Demo'
result1 = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content1)
print(result1)
print(result1.group())