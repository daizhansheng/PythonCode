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


s1 = Student("zhangsan")
s2 = Student("lisi", 50)
s3 = Student("wangwu")
s4 = Student("tianqi", 18)

lst = [s1, s2, s3, s4]

for item in lst:
    item.show()
