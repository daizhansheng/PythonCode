from random import randint

# import random
# 这两种导入模块的区别是 import random将这个模块中所有的函数都导入
# from random import randint表示只导入模块中的randint函数
lst = [i for i in range(1, randint(1, 100), 4)]
print(lst)
# in
print(5 in lst)
# not in
print(5 not in lst)
# len()
print(len(lst))
# max()
print(max(lst))
# min()
print(min(lst))
# lst.index()
try:
    print(lst.index(17))  # 获取17的下标，结果是4或者，错误
except ValueError as e:
    print(e)
# lst.count()
print(lst.count(1))  # 统计1的个数
