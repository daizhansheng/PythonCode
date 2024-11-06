import package.module as m

m.my_module()
# V1.0
# 代战胜
# this is module func

from package import module as m
m.my_module()
# this is module func

from package.module import *
my_module()
# this is module func

from package.module import my_module
my_module()
# this is module func