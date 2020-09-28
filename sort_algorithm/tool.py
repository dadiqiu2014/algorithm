# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-09-24 11:38

from time import time


def time_dec(func):
    def decorator(*args):
        start = time()
        res = func(*args)
        end = time()
        print('消耗时间：%s' % (end - start))
        return res

    return decorator