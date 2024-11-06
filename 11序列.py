# Python中序列就是连续存储多个值的空间
s = "Python"
# 通过所以访问上述序列
for i in range(0, len(s)):
    print(s[i], end="\t")  # P	y	t	h	o	n
print()

# 序列的切片
# [start,end,step]
# 起始位置0，结束位置5，步长2
print(s[0:6:2])  # Pto

# 序列相关操作及函数
# in
print("Py" in s)  # True
# not in
print("Py" not in s)  # False
# len()
print(len(s))  # s
# max()
print(max(s))  # y
# min()
print(min(s))  # P
# s.index()
print(s.index("th"))  # 2
# s.count()
print(s.count("P"))  # P在字符串中出现的次数
