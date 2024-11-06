# 数列的前几项为：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...

class FibClass:
    def __init__(self,n):
        self.n = n
        self.a,self.b = 0,1
        self.start=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.start > self.n:
            raise StopIteration
        else:
            self.a,self.b = self.b,self.a+self.b
            print(self.a,self.b)
            self.start += 1
            return self.a

fib = FibClass(5)

for item in fib:
    print(item)
