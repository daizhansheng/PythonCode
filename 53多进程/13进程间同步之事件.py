import multiprocessing
import time

# 创建一个 Event 对象
event = multiprocessing.Event()


def worker(event, wait_time):
    print(f"进程 {multiprocessing.current_process().name} 正在等待事件")
    event_is_set = event.wait(timeout=wait_time)
    if event_is_set:
        print(f"进程 {multiprocessing.current_process().name} 收到事件信号")
    else:
        print(f"进程 {multiprocessing.current_process().name} 等待超时")


def setter(event, wait_time):
    print(
        f"进程 {multiprocessing.current_process().name} 将在 {wait_time} 秒后设置事件"
    )
    time.sleep(wait_time)
    event.set()
    print(f"进程 {multiprocessing.current_process().name} 已设置事件")


if __name__ == "__main__":
    # 创建和启动等待进程
    wait_times = [5, 5, 5]
    processes = []
    for i, wait_time in enumerate(wait_times):
        p = multiprocessing.Process(
            target=worker, args=(event, wait_time), name=f"Worker-{i}"
        )
        processes.append(p)
        p.start()

    # 创建和启动设置进程
    setter_process = multiprocessing.Process(
        target=setter, args=(event, 2), name="Setter"
    )
    setter_process.start()

    # 等待所有进程完成
    for p in processes:
        p.join()
    setter_process.join()
