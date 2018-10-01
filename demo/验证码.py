#coding=utf-8
import random


def random_code():
    code = ''
    for i in range(5):
        ran1 = random.randint(0, 9)
        ran2 = chr(random.randint(65, 91))
        add = random.choice([ran1, ran2])
        code = ''.join([code, str(add)])
    print(code)


random_code()