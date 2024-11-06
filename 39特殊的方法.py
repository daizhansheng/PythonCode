class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b, a):
        super().__init__(a)
        self.b = b


class C(B, A):  # 解决菱形继承，注意继承顺序问题
    def __init__(self, c, b, a):
        super().__init__(b, a)
        self.c = c


a = A(1)
b = B(3, 2)
c = C(6, 5, 4)

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
print(a.__class__)
print(b.__class__)
print(c.__class__)
print("*" * 50)
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)
print(A.__base__)
print(B.__base__)
print(C.__base__)  # 父类按顺序显示第一个
print("*" * 50)
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())
