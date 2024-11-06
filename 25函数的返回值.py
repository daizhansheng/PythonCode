# 100-999区间中的水仙花数
def get_narcissus():
    lst = []
    for item in range(100, 1000):
        b = item // 100
        s = item % 100 // 10
        g = item % 10
        if b**3 + s**3 + g**3 == item:
            lst.append(item)
    return lst


narc = get_narcissus()
print(narc, type(narc))


# 输入一个数，求1-num中的数的和，及奇数和，偶数和
def get_sum(num=10):
    sum = 0  # 总和
    odd = 0  # 奇数和
    even = 0  # 偶数和
    for item in range(1, num + 1):
        if item % 2 == 0:
            even += item
        else:
            odd += item
        sum += item
    return sum, odd, even


my_sum = get_sum()
print(my_sum, type(my_sum))  # (55, 25, 30) <class 'tuple'>

my_sum = get_sum(20)
print(my_sum, type(my_sum))  # (210, 100, 110) <class 'tuple'>

a, b, c = get_sum(20)  # 系列解包赋值
print(a, b, c)  # 210 100 110
