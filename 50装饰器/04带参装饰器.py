def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)  # 调用原始函数
        print("After the function call")
        return result

    return wrapper


@my_decorator
def greet(name):
    print(f"Hello, {name}!")


@my_decorator
def multi_arg(a, b):
    print(f"a = {a},b = {b}")


greet("Alice")
multi_arg(b=5, a=100)
