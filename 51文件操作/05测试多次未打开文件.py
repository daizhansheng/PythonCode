# 在 Python 中，文件对象可以多次打开，但是如果文件对象没有被关闭，系统资源会被占用。
# 但是，Python 有一个垃圾回收机制，当文件对象不再被使用时，系统会自动关闭文件对象并释放资源。
# 因此，即使文件对象没有被显式关闭，也不会报错。
# 但是，这并不意味着你可以忽略关闭文件对象，关闭文件对象是良好的编程习惯。
# 例如：
file1 = open("file_lines.txt","r")
print(file1.read())

file2 = open("file_lines.txt","r")
print(file2.read())