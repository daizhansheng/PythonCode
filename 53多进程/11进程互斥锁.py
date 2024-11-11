from multiprocessing import Lock, Queue, Process

# 定义任务函数，模拟取钱操作
def task(who, money, queue, lock):
    # 进入死循环，直到取钱失败
    while True:
        # 获取锁，确保只有一个进程可以取钱
        lock.acquire()

        # 检查队列是否为空
        if not queue.empty():
            # 从队列中获取当前余额
            all_money = queue.get()

        # 检查余额是否足够取钱
        if all_money - money >= 0:
            # 取钱成功，更新余额
            all_money -= money
            print(f"{who}成功取了{money}钱，账户余额为{all_money}")
            # 将更新后的余额放回队列
            queue.put(all_money)
        else:
            # 取钱失败，打印消息
            print(f"{who}取钱失败，账户余额{all_money}")
            # 释放锁，退出循环
            lock.release()
            break

        # 取钱成功后，释放锁
        lock.release()

if __name__ == '__main__':
    # 创建队列，用于存储余额
    q = Queue()
    # 初始化余额为10000
    q.put(10000)

    # 创建锁，用于同步访问队列
    l = Lock()

    # 创建两个进程，模拟两个用户取钱
    p1 = Process(target=task, args=("zhangsan", 50, q, l))
    p2 = Process(target=task, args=("lisi", 100, q, l))

    # 启动两个进程
    p1.start()
    p2.start()

    # 等待两个进程结束
    p1.join()
    p2.join()