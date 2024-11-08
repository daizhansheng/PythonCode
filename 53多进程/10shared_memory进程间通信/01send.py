import os
import time
from  MyClass  import *
from multiprocessing import shared_memory
if __name__ == '__main__':
    print(os.getpid())
    p = MyClass("zhangsan",20)
    shm = shared_memory.SharedMemory(name="shm",create=True,size=14)
    shm.buf[:14] = p.to_bytes()
    time.sleep(10)
    try:
        shm.close()
        shm.unlink()
    except BufferError as e:
        print(e)
