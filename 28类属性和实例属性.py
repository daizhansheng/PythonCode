class Person:
    # 类属性：定义在类中，方法外的变量
    city = "china"

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # 左侧是实例属性，右侧是局部变量
        self.age = age  # 实例属性变量名和局部变量名字可以重复

    # 定义在类中的方法，是实例化方法
    def show(self):
        print(f"name={self.name},age={self.age}")

    # 静态方法，是使用装饰器修饰的
    @staticmethod
    def self_method():
        print(f"这里是静态方法,不能调用实例化属性，也不能调用实例化方法,city = {Person.city}")

    # 类方法，使用装饰器修饰
    @classmethod
    def class_method(cls):
        print(f"这是类方法是，不能够调用实例化属性，也不能调用实例化方法,city = {cls.city}")

print(Person.city)  # 类属性可以通过类名访问的变量，它不属于对象它属于类
p1 = Person("张三", 20)  # 实例化对象
print(type(p1))
p1.show()
p1.self_method()

Person.class_method()
