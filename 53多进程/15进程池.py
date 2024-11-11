import os
import time
from multiprocessing import pool


def task(var):
    print(f"task invok string = {var},pid = {os.getpid()}")
    time.sleep(1)


if __name__ == "__main__":
    print(os.getpid())
    with pool.Pool(processes=4) as pool:
        pool.apply(task, args=("hello python",))
        pool.apply(task, args=(12345,))
        pool.apply(task, args=(8.347,))
        pool.apply(task, args=(True,))

# 执行的结果：
# 22504
# task invok string = hello python,pid = 22507
# task invok string = 12345,pid = 22509
# task invok string = 8.347,pid = 22510
# task invok string = True,pid = 22508
