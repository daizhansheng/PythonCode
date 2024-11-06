
def write_file_line(fn,s):
    file = open(fn,"a+",encoding="utf-8")
    file.write(s)
    file.write('\n')
    file.close()

def write_file_lines(fn,lst):
    file = open(fn,"a+",encoding="utf-8")
    file.writelines(lst)
    file.close()

# 这行代码检查当前脚本是否是主程序（不是被其他脚本导入）
if __name__ == '__main__':
    write_file_line("file_line.txt","hello world")
    write_file_line("file_line.txt","hello Python")
    lst = ["city\t","weather\n","北京\t","晴天\n","上海\t","多云\n"]
    write_file_lines("file_lines.txt",lst)
