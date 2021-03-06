#!/user/bin/env python3
# -*- coding: utf-8 -*-

# fork

# import os

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid, pid))

# result:
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.

# ============================================================================================

# multiprocessing

# from multiprocessing import Process
# import os

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# ============================================================================================

# Pool

# from multiprocessing import Pool
# import os
# import time
# import random


# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     # time.sleep(random.random() * 3)
#     time.sleep(random.random() * 50)
#     end = time.time()
#     print('Task %s run (%s)...' % (name, os.getpid()))
#     print('Task %s run %0.2f secords.' % (name, (end - start)))

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool() #默认大小是cpu核心数
#     for i in range(8):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# ============================================================================================

# 子进程

# import subprocess

# # print('$ nslookup www.python.org')
# # r = subprocess.call(['nslookup', 'www.python.org'])
# # print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
#                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# # print(output.decode('utf-8'))
# print(output.decode('gbk'))
# print('Exit code:', p.returncode)

# ============================================================================================

# 进程间通信

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
