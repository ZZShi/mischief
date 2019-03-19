# -*- coding: utf-8 -*-
"""
@Time   : 2018/12/17 21:27
@File   : communicate.py
@Author : ZZShi
程序作用：

"""
from config import *

from wxpy import *


class Communicate(object):
    def __init__(self):
        self.bot = BOT
        self.master = MASTER
        self.small_ice = SMALL_ICE
        self.msg = MSG_LIST
        self.send_text(self.msg[0])

    def send_text(self, msg):
        self.master.send(msg)

    def send_image(self, img):
        self.master.send_image(img)

    def forward_msg(self, msg, to_master=True):
        """
        转发消息，默认转发给master
        :param msg: 转发的消息
        :param to_master: True: 转给master  False: 转给small_ice
        :return:
        """
        print(type(msg))
        if to_master:
            msg.forward(self.master)
        else:
            msg.forward(self.small_ice)


if __name__ == '__main__':
    c = Communicate()
    c.send_text('Yeah~')
    c.send_image(r'D:\life\amazing\cloud\origin.png')
    # for friend in bot.friends():
    #     print(friend)
