from module_my import *
from my_module import *
# 同时导入两个模块，但是模块中有相同的方法的或者变量，
# 规则是后者覆盖前者

module_func()
# 因为两个模块都存在module_func方法，调用这个函数的时候时候后者模块中的方法


#如何解决上述的冲问题？
#通过模块名.成员方式访问
import my_module
import module_my
module_my.module_func()
my_module.module_func()
