import time
from multiprocessing import Process,Value,Semaphore

def task(shm,sem):
    while True:
            sem[1].acquire()
            shm.value+=1
            time.sleep(1)
            sem[0].release()

if __name__ == '__main__':
    # 创建共享内存
    shm = Value('i',0)
    sem = [Semaphore(i) for i in range(2)]
    p = [Process(target=task,args=(shm,sem)) for _ in range(1)]

    for i in p:
        i.start()
    while True:
        sem[0].acquire()
        print(shm.value)
        sem[1].release()
