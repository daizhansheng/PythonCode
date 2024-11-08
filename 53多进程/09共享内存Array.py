import time
from multiprocessing import Process,Array

def task(shm,i):
    with shm.get_lock():
        shm[i] = shm[i] ** 2


if __name__ == '__main__':
    # 创建共享内存
    shm = Array('i',[1,2,3,4,5])

    p = [Process(target=task,args=(shm,i)) for i in range(5)]

    for i in p:
        i.start()

    for i in p:
        i.join()

    print(shm[:])