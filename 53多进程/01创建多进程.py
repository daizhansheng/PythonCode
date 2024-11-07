from multiprocessing import *

if __name__ == '__main__':
    # 创建多进程
    p = Process()
    # 运行多进程
    p.start()
    p.join()
