import struct

class MyClass:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def name_show(self):
        print("name = ",self.__name)
    def age_show(self):
        print("age = ",self.__age)

    def to_bytes(self):
        # 将 name 转换为 10 字节的 UTF-8 字节数组，不足补空格，age 转换为 4 字节整数
        name_bytes = self.__name.encode('utf-8').ljust(10, b' ')  # 固定 10 字节
        age_bytes = struct.pack('i', self.__age)  # 4 字节整数
        return name_bytes + age_bytes

    @classmethod
    def from_bytes(cls, byte_data):
        # 从 10 字节的 name 和 4 字节的 age 解析
        name =  bytes(byte_data[:10]).decode('utf-8').strip()  # 去除补充的空格
        age = struct.unpack('i', byte_data[10:14])[0]
        return cls(name, age)