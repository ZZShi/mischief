# -*- coding: utf-8 -*-
"""
@Time   : 2018/12/17 23:02
@File   : run.py
@Author : ZZShi
程序作用：

"""
import time

from src.config import *
from src.scheduler import Scheduler


from threading import Thread
from multiprocessing import Process, Queue


def receive_msg(q):
    """
    用来接收master的消息，并将收到的消息存到消息队列中
    """
    @BOT.register(MASTER, except_self=False)
    def put_msg_to_queue(msg):
        msg = str(msg)
        q.put(msg)

    BOT.join()


def process_msg(q):
    """
    从消息队列中取出消息进行处理，检查消息队列时间为0.5s
    """
    s = Scheduler()
    while True:
        if q.empty():
            time.sleep(0.5)
        else:
            msg = q.get()
            try:
                t = Thread(target=s.execute_cmd, args=(msg, ))
                t.start()
            except Exception as e:
                logger.error(e.args)
                s.c.send_text('({}) 执行失败，失败原因：{}'.format(msg, e.args))


if __name__ == '__main__':
    msg_q = Queue()
    p1 = Process(target=receive_msg, args=(msg_q, ))
    p2 = Process(target=process_msg, args=(msg_q, ))
    p1.start()
    p2.start()
    # ---p1、p2都是死循环，若是还有其它进程可以继续添加在下面

