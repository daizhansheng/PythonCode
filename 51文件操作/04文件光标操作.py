"""
city	weather
北京	晴天
上海	多云
city	weather
北京	晴天
上海	多云
"""

# 0（os.SEEK_SET）：从文件开头开始计数。
# 1（os.SEEK_CUR）：从当前位置开始计数。
# 2（os.SEEK_END）：从文件结尾开始计数。

file = open("file_lines.txt", "r+")
print(file.read(1))
file.seek(30, 0)
# file.seek(10,1) # 当前位置偏移，错误，因为文本文件编码格式问题
print(file.read(1))
print(file.tell())
file.close()
