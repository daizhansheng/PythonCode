import sys
import threading
import time
from threading import Thread


def thread1(num):
    print(f"num = {num},thread-name:{threading.current_thread().name}")
    sys.stdout.flush()  # 刷新缓冲区
    time.sleep(1)


if __name__ == "__main__":
    thread = Thread(target=thread1, name="www.baidu.com", args=(11,))

    thread.start()

    print(thread.is_alive())  # 线程是否在运行
    print(thread.name)  # 线程的名字
    print(thread.ident)  # 线程号

    thread.join()
