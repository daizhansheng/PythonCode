import my_module

# 导入my_module模块
print(my_module.module_var)

my_module.my_module()

m = my_module.ModuleSelf()

m.module_show()

import my_module as m

# 导入my_module模块并取别名为m
print(m.module_var)

from my_module import module_var

# 从my_module模块中导入module_var变量
print(module_var)

from my_module import my_module

# 从my_module中导入my_module函数
my_module()

from my_module import ModuleSelf

# 从my_module模块中带入ModuleSelf类
t = ModuleSelf()
t.module_show()

from my_module import *
# 导入模块中所有的内容，这里的*是一个通配符
my_module()

import math,time,random,my_module
# 同时导入多个模块
