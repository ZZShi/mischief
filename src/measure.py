# -*- coding: utf-8 -*-
"""
@Time   : 2018/12/17 21:39
@File   : measure.py
@Author : ZZShi
程序作用：

"""
from config import *

import os
import time

from PIL import ImageGrab
import cv2


class Measure(object):
    def __init__(self):
        self.path = RUNNING_LOGGER_PATH
        self.time = time.strftime('%Y-%m-%d_%H-%M-%S')
        self.delay_time = DELAY_TIME

    def get_screenshot(self):
        f_name = '{}{}_screenshot.jpg'.format(self.path, self.time)
        ImageGrab.grab().save(f_name)
        logger.info('Saved ' + f_name)
        return f_name

    def get_camera(self):
        f_name = '{}{}_camera.jpg'.format(self.path, self.time)
        # 参数0表示调用笔记本摄像头
        cap = cv2.VideoCapture(0)
        f, img = cap.read()
        # 关闭摄像头
        cap.release()
        if f:
            cv2.imwrite(f_name, img)
            logger.info('Saved ' + f_name)
        else:
            logger.warning('Get camera Failed...')
        return f_name

    @staticmethod
    def sleep_computer():
        cmd = 'shutdown -h'
        os.popen(cmd)

    def close_computer(self):
        cmd = 'shutdown -sg -t {}'.format(self.delay_time)
        os.popen(cmd)

    def reboot_computer(self):
        cmd = 'shutdown -g -t {}'.format(self.delay_time)
        os.popen(cmd)

    @staticmethod
    def cancel_reboot_computer():
        cmd = 'shutdown -a'
        os.popen(cmd)


if __name__ == '__main__':
    m = Measure()
    logger.info(m.get_camera())
    logger.warning(m.get_screenshot())


