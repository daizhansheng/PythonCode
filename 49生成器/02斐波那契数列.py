# 数列的前几项为：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...

def FibClass(n):
        start=1
        a, b=0,1
        while start <= n:
            a,b = b,a+b
            yield a
            start += 1


for item in FibClass(10):
    print(item)

