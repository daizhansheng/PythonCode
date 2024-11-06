# 定义一个 Person 类
class Person:
    # 定义一个 eat 方法
    def eat(self):
        # 打印出 "人爱吃饭"
        print("人爱吃饭")


# 定义一个 Cat 类
class Cat:
    # 定义一个 eat 方法
    def eat(self):
        # 打印出 "猫爱吃鱼"
        print("猫爱吃鱼")


# 定义一个 fun 函数，接受一个对象作为参数
def fun(obj):
    # 调用对象的 eat 方法
    # 这里使用了多态的概念，obj 可以是任何类的实例，只要它有 eat 方法
    obj.eat()


# 创建一个 Person 类的实例 p
p = Person()

# 创建一个 Cat 类的实例 c
c = Cat()

# 调用 fun 函数，传入 p 对象
fun(p)  # 输出：人爱吃饭

# 调用 fun 函数，传入 c 对象
fun(c)  # 输出：猫爱吃鱼
