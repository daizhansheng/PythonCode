import os
import time
from idlelib.run import flush_stdout

print(os.getcwd())
# /Users/dzs/Desktop/Py_work/52目录操作

print(os.listdir("../"))
# 结果存放到了列表中，效果和ls相同
try:
    os.mkdir("./testdir")
except FileExistsError as e:
    print("文件存在，创建失败", e)
# 在当前目录下创建testdir,类似于mkdir命令
try:
    os.makedirs("./testdir/aaa/111")
except FileExistsError as e:
    print(e)
# 创建具备层级关系的目录，类似于mkdir -p

os.rmdir("./testdir/aaa/111")
# 只能用来删除空目录，类似于rmdir命令

os.removedirs("./testdir/aaa")

os.chdir("../")
print(os.getcwd())

ll = os.walk("./")
print(type(ll))
for item in ll:
    print(item)
# 上述的功能类似于tree

os.chdir("./52目录操作")
print(os.getcwd())
with open("hello.txt", "w", buffering=1) as file:
    file.write("hello")
    file.close()

time.sleep(1)

os.rename("hello.txt", "new_hello.txt")

time.sleep(1)

os.remove("./new_hello.txt")

st = os.stat("./01目录操作实例1.py")
print(type(st))
print(st.st_ino)

# os.startfile("./startfile.py")
# os.startfile() 是 Windows 独有的功能，在 macOS 和 Linux 等非 Windows 系统上不可用。
