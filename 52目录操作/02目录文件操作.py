import os.path as op

print(op.abspath("./"))
# 获取当前的绝对路径

print("hello.txt 是否存在？", op.exists("./hello.txt"))
print("02目录文件操作.py 是否存在？", op.exists("./02目录文件操作.py"))

s = op.join(op.abspath("./"), "02目录文件操作.py")
print(s)
# 将文件名和目录拼接在一起

print(op.splitext(s))
# 拆分文件名和后缀

print(op.basename(s))
# 从路径中提取文件名

print(op.dirname(s))
# 从文件中提取路径

print("s 是否是目录 ？ ",op.isdir(s))
print("s 是否是文件 ？ ",op.isfile(s))