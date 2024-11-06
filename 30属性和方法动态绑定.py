class Student:
    school = "hqyj"

    def __init__(self, name, age=23):
        self.name = name
        self.age = age

    def show(self):
        print(f"name={self.name},age={self.age}")

    @staticmethod
    def static_student():
        print("这是Student的静态方法")

    @classmethod
    def class_student(cls):
        print("这是Student的类方法，可以访问类中的属性和方法")


s1 = Student("张三", 20)
s2 = Student("李四", 30)
s2.sex = "m"  # 动态绑定了属性
print(s1.name, s1.age)
print(s2.name, s2.age, s2.sex)


def hello(name):
    print(f"{name} say hello!!!")


s2.hello = hello  # 动态绑定了方法
s2.hello(s2.name)  # 李四 say hello!!!
