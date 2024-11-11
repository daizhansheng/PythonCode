import os
from multiprocessing import RLock, Process


# 定义任务函数
def task(who, lock):
    print(f"{who} 尝试获取锁")
    lock.acquire()
    try:
        print(f"{who} 获取锁成功")
        # 模拟递归获取锁
        nested_task(who, lock)
    finally:
        print(f"{who} 释放锁")
        lock.release()


# 定义嵌套任务函数
def nested_task(who, lock):
    print(f"{who} 尝试获取嵌套锁")
    lock.acquire()
    try:
        print(f"{who} 获取嵌套锁成功")
    finally:
        print(f"{who} 释放嵌套锁")
        lock.release()


if __name__ == "__main__":
    lock = RLock()  # 创建一个多进程共享的可重入锁
    p1 = Process(target=task, args=("zhangsan", lock))
    p2 = Process(target=task, args=("lisi", lock))

    p1.start()  # 启动第一个进程
    p2.start()  # 启动第二个进程

    p1.join()  # 等待第一个进程完成
    p2.join()  # 等待第二个进程完成
