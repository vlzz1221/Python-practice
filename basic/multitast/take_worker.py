#!/user/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager：


class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
try:
    m.connect()
except:
    print('请先启动task_master.py!')
    #sys.exit("sorry, goodbye!");
# 获取Queue的对象:
take = m.get_task_queue()
result = m.get_result_queue()
# 从take队列获取任务，并把结果写入result队列：
for i in range(10):
    try:
        n = take.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
#  处理结束:
print('worker exit.')