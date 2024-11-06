# 创建二维列表
from random import randint

lst = [
    ["姓名", "性别", "年龄"],
    ["张三", "男", 30],
    ["李四", "女", 22],
    ["王五", "男", 28],
    ["田七", "女", 18],
]

for row in lst:
    for item in row:
        print(item, end=" ")
    print()
# 结果如下:
# 姓名 性别 年龄
# 张三 男 30
# 李四 女 22
# 王五 男 28
# 田七 女 18

# 二维列表推导式
import random

lst = [[randint(1, 101) for _ in range(4)] for _ in range(3)]
print(lst)  # [[15, 52, 21, 99], [19, 38, 87, 77], [9, 67, 26, 43]]
print(type(lst))  # <class 'list'>
