# for循环对象是字符串
for i in "Python":
    print(i, end=" ")  # P y t h o n

# for循环和range结合
# range(stop)
# range(start, stop)
# range(start, stop, step)
# start：可选，序列开始的数值，默认为 0。
# stop：序列的结束位置（不包含该值）。
# step：可选，步长，默认是 1，即每次递增 1。步长可以是正数，也可以是负数。
# 求三位数中的水仙花数
import math

for num in range(100, 1000):
    b = num // 100
    s = num // 10 % 10
    g = num % 10
    if math.pow(b, 3) + math.pow(s, 3) + math.pow(g, 3) == num:
        print(num, end=" ")
print("")

str1 = "Python"
for index, data in enumerate(str1, start=100):
    print(index, data)  # 打印下标，和数值
# 上述结果如下
# 100 P
# 101 y
# 102 t
# 103 h
# 104 o
# 105 n


s = 0
for i in range(1, 5):
    if s != 0 and i == 1:  # 如果s初值不为0就不进行求和，否则求和
        break
    s += i
else:
    print(s)  # 10
