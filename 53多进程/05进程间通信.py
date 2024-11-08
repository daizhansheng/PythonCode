import os
import sys
import time
from multiprocessing import *
def process_handle1(child,pip1):
    while True:
        # Python子进程无法调用input，因为Python的终端只和主进程相关
        # 默认子进程的输入是关闭的，但是可以使用系统的函数代替input输入
        # s = input("input > ")
        s = child.recv()
        pip1.send(s)
        if s == "quit":
            exit(0)

def process_handle2(pip2):
    while True:
        s = pip2.recv()
        if s == "quit":
            exit(0)
        print(s,flush=True)

if __name__ == '__main__':
    parent, child = Pipe()
    pip1,pip2 = Pipe()
    p1 = Process(target=process_handle1,args=(child,pip1))
    p2 = Process(target=process_handle2,args=(pip2,))
    p1.start()
    p2.start()

    while True:
        x = input()
        parent.send(x)
        if x=='quit':
            break

    p1.join()
    p2.join()

