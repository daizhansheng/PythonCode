# 将lambda函数赋值给了f，f是函数类型
f = lambda x, y: x + y
print(type(f))  # <class 'function'>

print(f(100,200))

print((lambda x,y:x+y)(100,200))

d = [
    {"name": "zhangsan", "score": 90},
    {"name": "lisi", "score": 92},
    {"name": "wangwu", "score": 100},
    {"name": "tianqi", "score": 60},
]

print(d)
d.sort(key=lambda x:x.get("score"),reverse=True)
print(d)