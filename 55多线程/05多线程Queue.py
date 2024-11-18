import threading
import queue
import time


def producer(q):
    n = 1
    while True:
        if q.empty():
            q.put(f"item{n}")
            if n == 15:
                break
            n += 1
            time.sleep(1)


def consumer(q):
    while True:
        item = q.get()
        q.task_done()
        print(item)
        if item == "item15":
            break


if __name__ == "__main__":
    q = queue.Queue(maxsize=5)

    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    q.join()  # 如果队列数据取出后没有标记为task_done,这里会永久阻塞
