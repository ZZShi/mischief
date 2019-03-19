# -*- coding: utf-8 -*-
"""
@Time   : 2018/12/17 21:50
@File   : scheduler.py
@Author : ZZShi
程序作用：

"""
import re
import time

from config import *
from util import info_wrapper
from communicate import Communicate
from detection import Detection
from measure import Measure


class Scheduler(object, metaclass=type):
    def __init__(self):
        self.c = Communicate()
        self.d = Detection()
        self.m = Measure()
        self.msg_list = MSG_LIST  # 提示消息字典
        self.cmd_dict = {}  # 命令字典
        self._func_dict()  # 填充cmd_dict,将类方法名中后缀为'_(\d+)'的方法添加进命令字典

    def _func_dict(self):
        for func in dir(self):
            want_func = re.search(r'_\d+', func)
            if want_func:
                cmd_code = want_func.group()[-1]
                if self.cmd_dict.get(cmd_code):
                    logger.warning('{}与{}命令重复'.format(func, self.cmd_dict.get(cmd_code)))
                else:
                    self.cmd_dict[cmd_code] = func

    def _parse_msg(self, msg):
        if '(Text)' in msg:
            try:
                cmd_code = re.search(r'(\d+)', msg).group(1)
                return cmd_code
            except AttributeError:
                logger.warning('输入的命令不存在，无法解析：{}'.format(msg))
                self.c.send_text(self.msg_list[101])
        else:
            logger.warning('不支持的消息类型，只支持字符型: {}'.format(msg))
            self.c.send_text(self.msg_list[100])

    def execute_cmd(self, msg):
        cmd_code = self._parse_msg(msg)
        func = self.cmd_dict.get(cmd_code)
        if func:
            eval('self.{}()'.format(func))

    @info_wrapper
    def test_communicate_0(self):
        self.c.send_text(self.msg_list[1])

    @info_wrapper
    def get_disallowed_process_list_1(self):
        lst = self.d.get_disallowed_process_running()
        print(lst)
        if lst:
            self.c.send_text(lst)
        else:
            self.c.send_text(self.msg_list[3])

    @info_wrapper
    def get_screenshot_2(self):
        f_name = self.m.get_screenshot()
        self.c.send_image(f_name)

    @info_wrapper
    def get_camera_3(self):
        f_name = self.m.get_camera()
        self.c.send_image(f_name)

    @info_wrapper
    def sleep_computer_4(self):
        self.m.sleep_computer()
        self.c.send_text(self.msg_list[4])

    @info_wrapper
    def close_computer_5(self):
        self.m.close_computer()
        self.c.send_text(self.msg_list[5])

    @info_wrapper
    def reboot_computer_6(self):
        self.m.reboot_computer()
        self.c.send_text(self.msg_list[6])

    @info_wrapper
    def cancel_reboot_computer_7(self):
        self.m.cancel_reboot_computer()
        self.c.send_text(self.msg_list[7])


if __name__ == '__main__':
    s = Scheduler()
    for code in range(4):
        s.execute_cmd(str(code) + '(Text)')
        time.sleep(1)



