# 定义一个外部函数 out_func，它接受另一个函数 pass_func 作为参数
def out_func(pass_func):
    # 定义一个内部函数 inner_func，它会在被调用时执行 pass_func
    def inner_func():
        # 在调用 pass_func 之前，打印 "hello"（不换行）
        print("hello", end=" ")
        # 调用 pass_func
        pass_func()

    # 返回内部函数 inner_func
    return inner_func


# 定义一个函数 hello，它打印 "world"
@out_func
def hello():
    print("world")


# 调用扩充后的 hello 函数
hello()