def out_times_func(num):
    def out_func(func):
        def inner_func():
            for _ in range(num):
                func()
        return inner_func
    return out_func

@out_times_func(3)
def say_hello():
    print("hello world")

say_hello()