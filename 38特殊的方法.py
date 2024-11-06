# 定义两个数字变量
a = 100
b = 200

# 使用 dir() 函数获取 a 对象的所有属性和方法
print(dir(a))  # Python中一切皆对象

# 使用特殊方法 __add__ 来进行加法运算
print(a.__add__(b))  # 等价于 a + b

# 使用特殊方法 __sub__ 来进行减法运算
print(a.__sub__(b))  # 等价于 a - b

# 使用特殊方法 __gt__ 来进行大于运算
print(f"a > b吗？", a.__gt__(b))  # 等价于 a > b

# 使用特殊方法 __ge__ 来进行大于或等于运算
print(f"a >= b吗？", a.__ge__(b))  # 等价于 a >= b

# 使用特殊方法 __lt__ 来进行小于运算
print(f"a < b吗？", a.__lt__(b))  # 等价于 a < b

# 使用特殊方法 __le__ 来进行小于或等于运算
print(f"a <= b吗？", a.__le__(b))  # 等价于 a <= b

# 使用特殊方法 __eq__ 来进行等于运算
print(f"a == b吗？", a.__eq__(b))  # 等价于 a == b

# 使用特殊方法 __ne__ 来进行不等于运算
print(f"a != b吗？", a.__ne__(b))  # 等价于 a != b

# 使用特殊方法 __mul__ 来进行乘法运算
print("a * b = ", a.__mul__(b))  # 等价于 a * b

# 使用特殊方法 __truediv__ 来进行除法运算
print("a / b = ", a.__truediv__(b))  # 等价于 a / b

# 使用特殊方法 __floordiv__ 来进行整除运算
print("a // b = ", a.__floordiv__(b))  # 等价于 a // b

# 使用特殊方法 __mod__ 来进行取余运算
print("a % b = ", a.__mod__(b))  # 等价于 a % b