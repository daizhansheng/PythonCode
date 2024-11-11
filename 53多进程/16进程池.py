import os
import time
from multiprocessing import pool


def task(var):
    print(f"task invok string = {var},pid = {os.getpid()}")
    time.sleep(1)
    return os.getpid()


def print_end(result):
    print(f"进程执行结束,result = {result}")


if __name__ == "__main__":
    print(os.getpid())
    with pool.Pool(processes=4) as pool:
        pool.apply_async(task, args=("hello python",), callback=print_end)
        pool.apply_async(task, args=(12345,), callback=print_end)
        pool.apply_async(task, args=(8.347,), callback=print_end)
        pool.apply_async(task, args=(True,), callback=print_end)

        # 虽然with会自动管理资源，但是async异步执行不会等待子进程执行完毕
        # 所以需要调用close和join
        pool.close()
        pool.join()
