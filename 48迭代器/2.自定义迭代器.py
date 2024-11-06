
class MyItor:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.start - 1

itor = MyItor(0,5)
print(itor,type(itor))
for item in itor:
    print(item)