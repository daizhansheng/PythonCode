# Python中单例模式就是一个类只能实例化一个对象
# 在实例化对象的时候先调用__new__方法，如果当前类中
# 没有实现__new__则直接调用父类的__new__方法,目的给对象分配内存
# __new__(,*args,**kwargs)参数会被直接传递给__init__方法完成初始化
class Singleton:
    _instance=None
    def __new__(cls, *args, **kwargs):
        print(f"__new__:args = {args},kwargs = {kwargs}")
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self,value):
        self.value = value
    def show(self):
        print(f"value = {self.value}")

s1 = Singleton(10)
s2 = Singleton(100)

print(f"s1 addr = {hex(id(s1))},s2 addr = {hex(id(s2))}")
print(f"s1 is s2??",s1 is s2)
s1.show()
s2.show()

# 程序输出的结果如下：
# __new__:args = (10,),kwargs = {}
# __new__:args = (100,),kwargs = {}
# s1 addr = 0x10df41940,s2 addr = 0x10df41940
# s1 is s2?? True
# value = 100
# value = 100