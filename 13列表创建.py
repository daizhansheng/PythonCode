# 1.列表的[]创建方式
import sys

lst1 = [1, 2.5, "hello", 4 + 3j, True]
print(lst1, sys.getsizeof(lst1), id(lst1))
# del lst1  # 删除列表

# 2.使用list()函数创建列表
lst2 = list([1, 2.5, "hello", 4 + 3j, True])
print(lst2, sys.getsizeof(lst2), id(lst2))

# 3.使用列表推导式
lst3 = [i + 100 for i in range(5)]  # 将0-4数据加上100放到列表中
print(lst3)  # [100, 101, 102, 103, 104]

lst4 = [i for i in range(10) if i % 2 == 0]  # 将0-9中偶数放在列表中
print(lst4)

# 4.随机数和推导式结合
import random

lst5 = [random.randint(1, 100) for i in range(10)]
print(lst5)
