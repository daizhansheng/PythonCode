import time
from multiprocessing import Process, Condition, Queue


def product_task(con, q):
    data = 0
    while True:
        con.acquire()
        time.sleep(1)
        if data < 5:
            data += 1
        else:
            data = 1
        q.put(data)
        con.notify()
        con.release()


def comsumer_task(con, q, i):
    while True:
        con.acquire()
        con.wait()
        data = q.get()
        print(f"{i}进程获取到data = {data}")
        con.release()


if __name__ == "__main__":
    con = Condition()
    q = Queue()
    product = Process(target=product_task, args=(con, q))
    comsumer = [Process(target=comsumer_task, args=(con, q, i)) for i in range(5)]

    product.start()
    for c in comsumer:
        c.start()

    product.join()
    for c in comsumer:
        c.join()
