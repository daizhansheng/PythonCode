import os
from multiprocessing import Lock,Queue,Process

def task(who,money,queue,lock):
    while True:
        lock.acquire()
        all_money = queue.get()
        if all_money - money  >= 0:
            all_money -= money
            print(f"{who}成功取了{money}钱，账户余额为{all_money}")
            queue.put(all_money)
        else:
            print(f"{who}取钱失败，账户余额{all_money}")
            lock.release()
            os.exit(1)
        lock.release()

if __name__ == '__main__':
    q = Queue()
    q.put(10000)
    l = Lock()
    p1 = Process(target=task,args=("zhangsan",50,q,l))
    p2 = Process(target=task, args=("lisi", 100,q,l))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("111111111")