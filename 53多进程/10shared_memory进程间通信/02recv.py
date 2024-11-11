import os

from MyClass import *
from multiprocessing import shared_memory

if __name__ == "__main__":
    print(os.getpid())
    shm = shared_memory.SharedMemory(name="shm",)
    ba = shm.buf[:14]
    p = MyClass.from_bytes(ba)
    p.name_show()
    p.age_show()

    del ba
    try:
        shm.close()
        shm.unlink()
    except BufferError as e:
        print(e)
