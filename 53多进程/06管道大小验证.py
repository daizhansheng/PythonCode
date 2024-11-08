from multiprocessing import *


def send(pipe):
    n=0
    while True:
        pipe.send('a')
        print(n)
        n+=1

if __name__ == '__main__':
    p,c = Pipe()
    process = Process(target=send,args=(c,))
    process.start()
    while True:
        x = input()
        p.recv()
        if x == "quit":
            process.terminate()
            break
    process.join()