# -*- coding: utf-8 -*-
"""
@Time   : 2018/12/17 21:27
@File   : config.py
@Author : ZZShi
程序作用：

"""
import os
import sys
import logging.handlers
from wxpy import Bot


# 防沉迷程序列表
DISALLOWED_PROCESS_LIST = ['chrome.exe', 'YoudaoDict.exe', 'IDMan.exe', 'pythonw.exe']

# ----------------------windows配置-------------------
DELAY_TIME = 120  # 休眠、关机、重启延迟时间

# ---------------------微信模块配置-------------------
BOT = Bot(True)
MASTER = BOT.file_helper           # 自己在微信机器人里面的备注
SMALL_ICE = BOT.mps().search('小冰')
MINE = 'Your Majesty'        # 通知时对自己的称呼
CONTROLLED = '小老弟'          # 通知时对被控者的称呼
MSG_LIST = {
    0: '{}, 我已经成功上线╰(●’◡’●)╮'.format(MINE),
    1: '测试成功，通讯正常，可以执行命令╭(●｀∀´●)╯',
    2: '检测到您的{}正在运行以下被禁止的程序(..•˘_˘•..)'.format(CONTROLLED),
    3: '没有被禁止的程序在运行，您的{}表现不错๑乛◡乛๑'.format(CONTROLLED),
    4: '休眠命令已执行(o-ωｑ)).oO 困',
    5: '关机命令已执行，延迟时间：{}s (_ _)( - . - )(~O~) ……( - . - )'.format(DELAY_TIME),
    6: '重启命令已执行，延迟时间：{}s (つω｀)～'.format(DELAY_TIME),
    7: '取消关机命令已执行，来不来得及我就说不来了 (o≖◡≖)',


    100: '目前还不支持此消息类型，请输入文字o(￣┰￣*)ゞ',
    101: '输入的命令不存在，无法解析，请输入111获取有效命令(*￣rǒ￣)',

}

# ----------------------命令字典配置-------------------
COMMAND = {
    0: {
        'command': '',
        'command_meaning': '测试通信',
        'command_result': ''
    },
    1: {
        'command': '',
        'command_meaning': '获得程序列表',
        'command_result': ''
    },
}

# ----------------------log配置----------------------
# 邮箱信息
MAILHOST = ('smtp.163.com', 25)
FROMADDR = '********@163.com'
TOADDRS = ['*********@qq.com']
SUBJECT = 'Error Record'
# 凭证，用户名和SMTP协议密码
CREDENTIALS = ('*******@163.com', '********')

logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)
# 开发日志处理器
DEVELOPMENT_LOGGER_PATH = './log/'
if not os.path.exists(DEVELOPMENT_LOGGER_PATH):
    os.mkdir(DEVELOPMENT_LOGGER_PATH)
f_development = DEVELOPMENT_LOGGER_PATH + 'development.log'

development_stream_handle = logging.StreamHandler(stream=sys.stdout)
development_stream_handle.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s'))

development_error_handle = logging.FileHandler(f_development)
development_error_handle.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s'))
development_error_handle.setLevel(logging.ERROR)
# 上线日志处理器
RUNNING_LOGGER_PATH = './logs/'
if not os.path.exists(RUNNING_LOGGER_PATH):
    os.mkdir(RUNNING_LOGGER_PATH)
f_running = RUNNING_LOGGER_PATH + 'running.log'

running_info_handle = logging.handlers.TimedRotatingFileHandler(f_running, when='midnight')
running_info_handle.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

running_error_handle = logging.handlers.SMTPHandler(MAILHOST, FROMADDR, TOADDRS, SUBJECT, CREDENTIALS)
running_error_handle.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s'))
running_error_handle.setLevel(logging.ERROR)

logger.addHandler(development_stream_handle)
logger.addHandler(development_error_handle)
# logger.addHandler(running_info_handle)
# logger.addHandler(running_error_handle)


