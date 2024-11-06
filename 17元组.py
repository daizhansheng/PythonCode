# 使用()创建元组
tp = (1, 2, 3, 4)
print(tp, type(tp))  # (1, 2, 3, 4) <class 'tuple'>

# 使用()创建单元素的元组
tp1 = (5,)  # 这里的,号一旦省略就变成了int类型
print(tp1, type(tp1))  # (5,) <class 'tuple'>

# 使用逗号创建元组
tp2 = 11, [22], "abc", True, 5 + 2j, 4.31
print(tp2, type(tp2))  # (11, [22], 'abc', True, (5+2j), 4.31) <class 'tuple'>

# 使用tuple()函数创建元组
tp3 = tuple((11, "abc", True, 5 + 2j, 4.31))
print(tp3, type(tp3))  # (11, 'abc', True, (5+2j), 4.31) <class 'tuple'>

# 使用生成器表达式解包创建
import time

print(time.ctime(time.time()))
# tp4 = (time.ctime(time.time()) for _ in range(2))
# 这种写法是错误的，元组不支持生成器表达式，因为它一旦创建就不能修改，所以可以使用tuple函数转为元组
tp4 = tuple(time.ctime(time.time()) for _ in range(2))
print(tp4)

##########################################################
tp5 = ([11, 22], 33, "helloworld", 4.13, True)
# 切片
print(tp5[0 : len(tp5) : 2])  # ([11, 22], 'helloworld', True)
# in
print(4.13 in tp5)
# not in
print([11, 22] not in tp5)
# len()
print(len(tp5))  # 5
# max()
# print(max(tp5)) #有列表类型不支持比大小
# min()
# s.index()
print(tp5.index(True))
# s.count()
print(tp5.count(True))

#######################################################
# 元组成员的遍历
for index,item in enumerate(tp5):
    print(f"tp5[{index}]={item}")

#######################################################
tp5 = (11,22,33,44)
a,b,*c = tp5 # a=11,b=22,*c=[33,44]
print(a,b,c)