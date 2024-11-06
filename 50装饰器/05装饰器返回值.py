def out_func(func):
    def inner_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret**2

    return inner_func


@out_func
def cal(x, y):
    return x * y


print(cal(3, 4))
