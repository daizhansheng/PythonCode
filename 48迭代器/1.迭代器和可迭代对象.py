# 在Python中列表，元组，字典，集合都是可迭代对象
# 但他们不是迭代器

lst = [11, 22, 33, 44, 55]

lst_itor = lst.__iter__()  # 返回一个迭代器
print(lst_itor)  # <list_iterator object at 0x10a69f6d0>

# print(lst_itor.__next__())  # 11
# print(lst_itor.__next__())  # 22
# print(lst_itor.__next__())  # 33
# print(lst_itor.__next__())  # 44
# print(lst_itor.__next__())  # 55
# print(lst_itor.__next__()) #StopIteration

# 如果打开上述print(lst_itor.__next__()),已经迭代到结尾
# 如下的for循环就不会有结果输出
for item in lst_itor:
    print(item)

itor = reversed(lst)
print(itor)  # <list_reverseiterator object at 0x10c470f10>
for item in itor:
    print(item)
