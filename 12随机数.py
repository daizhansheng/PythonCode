# 1.使用随机数生成列表，但是这里先讲解随机数的使用
import random as rd

# 生成随机浮点数：生成范围在 [0.0, 1.0) 之间的随机浮点数
print(rd.random())
# 生成特定范围内的随机整数：使用 randint(a, b) 函数，返回的随机整数在 a 和 b 之间，包括 a 和 b。
print(rd.randint(1, 100))
# 生成指定范围内的随机整数：使用 randrange(start, stop[, step])。
for _ in range(10):
    print(rd.randrange(1, 100, 6), end=" ")
print()
# 上述表达式表示从1开始步长为6中的随机整数，start包含，end不包含
# 1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97
# 例如上述10个数可能是：31 1 91 19 13 97 31 85 49 1

# 从序列中随机选择元素：使用 choice() 函数。
lst5 = list([1, 2.5, "hello", 4 + 3j, True])

print(rd.choice(lst5))
# 从序列中随机选择多个元素：使用 sample() 函数，返回指定数量的随机元素。
print(rd.sample(lst5, 2))  # 从列表中选择2个数

# 随机打乱序列：使用 shuffle() 函数，会原地打乱列表的顺序
rd.shuffle(lst5)  # 这个函数没有返回结果，所以需要单独打印列表
print(lst5)

# 随机数种子
# 为了确保随机数生成的可重复性，可以使用 seed() 函数设置随机种子
rd.seed(42)  # 设置种子为42
print(rd.random())  # 每次运行此代码将产生相同的结果
