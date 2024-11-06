class MyIterInstance:
    def __init__(self, *items):
        self.lst = list(items)

    def __iter__(self):
        return MyIterInstanceIterator(self)

class MyIterInstanceIterator:
    def __init__(self, my_iter_instance):
        self.my_iter_instance = my_iter_instance
        self.index = 0

    def __next__(self):
        if self.index < len(self.my_iter_instance.lst):
            result = self.my_iter_instance.lst[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

myiter = MyIterInstance(1, 2, 3, 4)
print(myiter)

for item in myiter:
    print(item)