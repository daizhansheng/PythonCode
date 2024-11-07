from multiprocessing import Process


def process(who,work):
    print(f"who = {who},work = {work}")
    exit(0)
if __name__ == '__main__':
    p = Process(target=process,args=("zhangsan", "执行进程"))
    p.start()
    p.join()
if __name__ == '__main__':
    p = Process(target=process,kwargs={"who": "zhangsan", "work": "执行进程"})
    p.start()
    p.join()