def fun(*args):  # 参数传递过来后是一个元组
    for item in args:
        print(item, end="|")


fun(11, 22, 33, 44)
print()

fun(10)
print()

fun([11, 22, 33, 44])  # 他会把这个列表当成一个成员
print()

fun(*[11, 22, 33, 44, 55])  # 加1个*解包为多个成员
print()