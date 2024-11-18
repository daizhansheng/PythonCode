import threading


def timer_func():
    print(f"定时时间到了")


if __name__ == "__main__":
    t = threading.Timer(5, timer_func)
    t.start()
    t.join()
