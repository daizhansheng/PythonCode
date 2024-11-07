import os
import sys
import time
from multiprocessing import Process


def say_hello(who):
    time.sleep(2)
    print(f"{who,os.getpid()} say hello",flush=True)

    # 刷新缓冲区
    sys.stdout.flush()

if __name__ == '__main__':
    pnames = ['zhangsan','lisi','wangwu']
    plist = []
    for i in range(len(pnames)):
        p = Process(target=say_hello,args=(pnames[i],))
        p.start()
        plist.append(p)

    for p in plist:
        print(f"等待{p.pid}进程结束")
        p.join()