from abc import ABC, abstractmethod
from sysconfig import get_path


# 定义一个抽象基类 Animal，它定义了一个抽象方法 speak
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# 定义一个狗类 DogAnimal，它继承自 Animal，并实现了 speak 方法
class DogAnimal(Animal):
    def speak(self):
        print("wang wang wang !")


# 定义一个猫类 CatAnimal，它继承自 Animal，并实现了 speak 方法
class CatAnimal(Animal):
    def speak(self):
        print("miao miao miao !")


# 定义一个抽象基类 AnimalFactory，它定义了一个抽象方法 create_animal
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


# 定义一个狗工厂类 DogFactory，它继承自 AnimalFactory，并实现了 create_animal 方法
class DogFactory(AnimalFactory):
    def create_animal(self):
        return DogAnimal()


# 定义一个猫工厂类 CatFactory，它继承自 AnimalFactory，并实现了 create_animal 方法
class CatFactory(AnimalFactory):
    def create_animal(self):
        return CatAnimal()


# 定义一个工厂函数 get_peat，它接受一个 AnimalFactory 对象作为参数，并返回该工厂创建的动物实例
def get_peat(factory: AnimalFactory) -> AnimalFactory:
    return factory.create_animal()


# 创建一个狗工厂对象 dogfact
dogfact = DogFactory()

# 创建一个猫工厂对象 catfact
catfact = CatFactory()

# 使用 get_peat 函数创建一个狗实例对象 dog
dog = get_peat(dogfact)

# 使用 get_peat 函数创建一个猫实例对象 cat
cat = get_peat(catfact)

# 调用狗实例的 speak 方法
dog.speak()

# 调用猫实例的 speak 方法
cat.speak()
