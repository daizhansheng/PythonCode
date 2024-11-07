import os
import time
from multiprocessing import *


def process1():
    n = 0
    print(f"子进程 process1 pid = {os.getpid()},ppid = {os.getppid()}")
    while True:
        print("我是子进程")
        time.sleep(1)
        n += 1
        if n == 5:
            exit(0)


if __name__ == "__main__":
    print(f"父进程的pid = {os.getpid()}")
    # 默认情况下，子进程是非守护进程，这意味着主进程会等待所有非守护子进程完成后再退出。
    # 即使父进程没有调用join()方法，只要子进程仍在运行，主进程就不会退出。
    p = Process(target=process1, name="child_process")
    p.start()
    # 阻塞等待子进程结束
    p.join()
    print("子进程退出了")
