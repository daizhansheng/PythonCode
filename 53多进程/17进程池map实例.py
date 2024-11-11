import os
import time
from multiprocessing import pool


def task(var):
    return var**2


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    with pool.Pool(processes=4) as pool:
        lst = pool.map(task, lst)
        print(lst)
        # 结果如下：[1, 4, 9, 16]
