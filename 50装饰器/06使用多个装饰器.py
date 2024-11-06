def out_func1(func):
    def inner_func1(*args, **kwargs):
        print(f"func.name = {inner_func1.__name__,func.__name__},start")
        ret = func(*args, **kwargs)
        print(f"func.name = {inner_func1.__name__,func.__name__},end")
        return ret

    return inner_func1
def out_func2(func):
    def inner_func2(*args, **kwargs):
        print(f"func.name = {inner_func2.__name__,func.__name__},start")
        ret = func(*args, **kwargs)
        print(f"func.name = {inner_func2.__name__,func.__name__},end")
        return ret
    return inner_func2

@out_func1
@out_func2
def say_hello(string):
    print("hello ", string)


say_hello("zhangsan")
