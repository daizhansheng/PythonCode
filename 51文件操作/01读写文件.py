def write_file(filename):
     file = open(filename,"w+",encoding="utf-8")
     file.write("祝贺神州19号法神成功")
     file.close()

def read_file(filename):
     file = open(filename,"r",encoding="utf-8")
     s = file.read()
     file.close()
     return s

if __name__ == '__main__':
     write_file("hello.txt")
     print(read_file("hello.txt"))

