import threading
import inspect


def timer_func():
    f = inspect.currentframe()
    print(f"文件名:{f.f_code.co_filename},函数名:{f.f_code.co_name},行号：{f.f_lineno}")
    t = threading.Timer(2, timer_func)
    t.start()


if __name__ == "__main__":
    t = threading.Timer(2, timer_func)
    t.start()
