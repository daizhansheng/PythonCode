# 当前文件夹：31类的权限.py
# ======================================

# 定义一个 Student 类
class Student:
    # 构造函数，用于初始化类的实例
    def __init__(self, name, age, sex):
        # 将 name、age 和 sex 参数赋值给实例的 name、_age 和 __sex 属性
        # name 属性是公有的，可以直接访问
        self.name = name  
        # _age 属性是受保护的，可以通过类本身或子类访问，但是也可以强制访问
        self._age = age  
        # __sex 属性是私有的，只能通过类本身访问
        self.__sex = sex  

    # 受保护的方法
    def _fun(self):
        # 打印出“这是受保护的方法”
        print("这是受保护的方法")

    # 私有的方法
    def __fun(self):
        # 打印出“这是私有的方法”
        print("这是私有的方法")

    # 公有的方法
    def show(self):
        # 打印出实例的 name、_age 和 __sex 属性
        print(f"name={self.name},age={self._age},sex={self.__sex}")

# 创建一个 Student 类的实例 s1
s1 = Student("张三", 20, "M")

# 访问实例的 name 属性
print(s1.name)

# 访问实例的 _age 属性（注意：这是受保护的属性）
print(s1._age)  # 警告：访问类的 protected 成员 _age

# 尝试访问实例的 __sex 属性（注意：这是私有的属性）
# print(s1.__sex) #AttributeError: 'Student' object has no attribute '__sex'

# 调用实例的 show 方法
s1.show()

# 调用实例的 _fun 方法（注意：这是受保护的方法）
s1._fun()

# 尝试调用实例的 __fun 方法（注意：这是私有的方法）
# s1.__fun() #AttributeError: 'Student' object has no attribute '__fun'. Did you mean: '_fun'?

# 受保护的一定不能访问吗？答案是否定的
# 可以通过 dir() 函数获取这个类中的所有属性及方法
print(dir(s1))  # ['_Student__fun', '_Student__sex'...

# 访问实例的 __sex 属性（注意：这是私有的属性）
print(s1._Student__sex)  # M

# 调用实例的 __fun 方法（注意：这是私有的方法）
s1._Student__fun()  # 这是私有的方法