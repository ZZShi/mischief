# -*- coding: utf-8 -*-
"""
@Time   : 2018/12/20 22:26
@File   : util.py
@Author : ZZShi
程序作用：

"""
import time
import requests
from wxpy import TEXT, RECORDING

from config import *


def info_wrapper(func):
    """
    函数运行信息打印装饰器
    """
    def wrapper(*args, **kw):
        print('------------[{}] is Start-------------'.format(func.__name__))
        func_start = time.time()
        rst = func(*args, **kw)
        func_end = time.time()
        print('----[{}] is Ended, Run Time: {}s----'.format(func.__name__, func_end - func_start))
        return rst
    return wrapper


if __name__ == '__main__':
    bot = BOT
    small_ice = bot.mps().search('小冰')[0]
    print(small_ice)
    small_ice.send('Hello')

    @bot.register(MASTER, except_self=False)
    @info_wrapper
    def receiver(msg):
        print(msg)
        print(type(msg))
        nmsg = str(msg)
        if '(Text)' in nmsg:
            print("It's text...")
        if '(Recording)' in nmsg:
            print("It's voice...")
        if '(Picture)' in nmsg:
            print("It's picture...")
            msg.get_file('1.jpg')
        small_ice.send(msg)

    @bot.register(small_ice)
    def recv_small_ice(msg):
        print(msg)
        MASTER.send(msg)

    bot.join()



