import threading
import time

money = 1000
# 在函数内可以直接读取全局变量
# 在函数内如果要修改全局变量的值必须加上global的修饰
# 这个实例中因为线程执行需要获取GIL锁，所以thread1和
# thread2并没有同步，但是可以验证两线程通信


def thread1():
    global money
    while money > 0:
        money -= 100
        print(f"{threading.current_thread().name} 修改money={money}")
        time.sleep(1)


def thread2():
    while money > 0:
        print(f"{threading.current_thread().name} 获取money={money}")
        time.sleep(2)


if __name__ == "__main__":
    t1 = threading.Thread(target=thread1, name="thread1")
    t2 = threading.Thread(target=thread2, name="thread2")
    t1.start()
    t2.start()

    t1.join()
    t2.join()
