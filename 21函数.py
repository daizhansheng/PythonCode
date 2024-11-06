# 封装求n个数和的代码
def getsum(num):
    assert isinstance(num, int), "类型不正确，请重试"
    s = 0
    for i in range(1, num + 1):
        s += i
    return s


print(getsum(100))
print(getsum(1000))
try:
    print(getsum(1.0))
except AssertionError as e:
    print(e)
