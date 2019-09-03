# -*- coding: utf-8 -*-
"""
@Time   : 2018/12/17 21:32
@File   : detection.py
@Author : ZZShi
程序作用：

"""
import os
import time

from config import *


class Detection(object):
    """
    实现被禁用程序的检测与关闭
    """
    def __init__(self):
        self.disallowed_process_list = DISALLOWED_PROCESS_LIST
        self.path = DEVELOPMENT_LOGGER_PATH
        self.running_process_lst = []

    def has_disallowed_process_running(self):
        """
        判断是否有被禁止的程序在运行
        :return: True or False
        """
        has_process = False
        self.running_process_lst = []
        for process in self.disallowed_process_list:
            if process in os.popen('tasklist').read():
                logger.info('{} is running...'.format(process))
                self.running_process_lst.append(process)
                has_process = True
        return has_process

    def get_disallowed_process_running(self):
        """
        得到正在运行的禁止程序列表
        :return: list
        """
        if self.running_process_lst is None:
            self.has_disallowed_process_running()
        return self.running_process_lst

    def close_disallowed_process(self):
        """
        关闭被禁止运行的程序
        :return: 要是全部关闭返回True
        """
        for process in self.running_process_lst:
            cmd = 'taskkill /f /t /im {}'.format(process)
            res = os.popen(cmd).read()
            if '成功' in res:
                self.running_process_lst.remove(process)
                logger.info('{} has closed...'.format(process))
            else:
                logger.warn('{} has not closed...'.format(process))
        # 貌似os.popen()同时只能打开两个进程，只能递归调用直到关闭所有程序
        if self.has_disallowed_process_running():
            self.close_disallowed_process()


if __name__ == '__main__':
    d = Detection()
    print(d.has_disallowed_process_running())
    print(d.get_disallowed_process_running())
    print(d.close_disallowed_process())
    time.sleep(10)
    print(d.has_disallowed_process_running())
    print(d.get_disallowed_process_running())
    print(d.close_disallowed_process())
