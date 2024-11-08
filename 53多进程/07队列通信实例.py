import time
from multiprocessing import *

def producer(queue):
    for i in range(5):
        queue.put(f"我是生产者，我发送的消息id = {i}")
        time.sleep(1)

def consumer(queue):
    while True:
        msg = queue.get()
        print(msg)
        i = msg.index("id")
        if msg[i+5:] == "4":
            break


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=producer,args=(q,))
    p2 = Process(target=consumer,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()