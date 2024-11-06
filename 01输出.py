# 测试输出
print(123)
print("hello world")
print(3.14)
print(True)
print('A')

# print测试分隔符和结束符
print(1, 2, 3, sep='|', end='\n')

# print测试想文件中写
'''
模式	含义
"r"	以读取模式打开文件。如果文件不存在，会抛出 FileNotFoundError。
"w"	以写入模式打开文件。如果文件存在，会清空文件内容；如果文件不存在，则会创建新文件。
"a"	以追加模式打开文件。如果文件不存在，会创建新文件。写入时，数据会追加到文件末尾，保留原有内容。
"x"	以新建模式打开文件。如果文件已经存在，会抛出 FileExistsError。
"b"	二进制模式。如果与其他模式组合使用（如 "rb" 或 "wb"），文件将以二进制格式处理（适合处理非文本文件，如图片、视频、音频）。
"t"	文本模式（默认）。如果与其他模式组合使用（如 "rt" 或 "wt"），文件将以文本格式处理。
"+"	读写模式。如果与其他模式组合使用（如 "r+"、"w+"），文件将同时支持读和写操作。
'''
fd = open("hello.txt", "w+")
print("hello world", file=fd)
fd.write("今天天气不错")
fd.seek(5)  # 0是文件开头，1光标当前位置，2文件结尾,文本文件只能是0
print(fd.read())
fd.close()

# print输出多个字符串
print("hello" + "world")

# print输出多个*
print('*' * 50)

# print输出小数点后有效位
# #f-string格式输出
pi = 3.1415926535
print(f"{pi:.2f}")
print(f"{pi:.4f}")
# #使用format函数
print("{:.2f}".format(pi))
print("{:.4f}".format(pi))
# #使用%格式化
print("%.2f %.4f" % (pi, pi))
# #使用round函数
print(round(pi, 2))

# 使用print输出多个类型的变量
# #%连续输出多个类型变量
name = "zhangsan"
age = 20
sex = 'm'
score = 59.9999
print("name=%s,age=%d,sex=%c,score=%.2f" % (name, age, sex, score))
# #f-string方式输出多个变量
print(f"{name},{age},{sex},{score:.2f}")
# #format函数输出多个变量
print("{0},{1},{2},{3:.2f}".format(name, age, sex, score))
