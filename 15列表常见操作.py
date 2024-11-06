from random import randint

lst = [1, 3.14, "hello", 4 - 2j, False]
print(lst)
# 1.列表追加append(x)
lst.append("Python")
print(lst)  # [1, 3.14, 'hello', (4-2j), False, 'Python']
# 2.列表插入insert(index,x)
lst.insert(2, 6.72)  # [1, 3.14, 6.72, 'hello', (4-2j), False, 'Python']
print(lst)
# 3.列表成员取出pop(x),取出后会列表中删除成员
print(lst.pop(0))
print(lst)  # [3.14, 6.72, 'hello', (4-2j), False, 'Python']
# 4.列表中成员移除remove(x),移除第一次出现的成员
lst.remove("hello")
print(lst)  # [3.14, 6.72, (4-2j), False, 'Python']
# 5.列表元素翻转reverse(x)
lst.reverse()
print(lst)  # ['Python', False, (4-2j), 6.72, 3.14]
# 6.拷贝列表函数copy(),生成一个新的列表
lst1 = lst.copy()
print(lst1)  # ['Python', False, (4-2j), 6.72, 3.14]
# 7.列表成员清空clear()
lst.clear()
print(lst)  # []
print(lst1)  # ['Python', False, (4-2j), 6.72, 3.14]

# 8.对列表成员排序
lst = [randint(1, 100) for _ in range(5)]
print(lst)  # [98, 87, 15, 43, 91]
lst.sort()  # 默认是升序排序
print(lst)  # [15, 43, 87, 91, 98]
lst.sort(reverse=True)  # 降序排序
print(lst)  # [98, 91, 87, 43, 15]

# 9.排序是key的设置
lst = ["apple", "orange", "banana", "pear"]
lst.sort(key=len)  # 按照长度排序
print(lst)
for index, item in enumerate(lst):
    lst[index] = item.capitalize()  # 首字母大写
print(lst)  # ['Pear', 'Apple', 'Orange', 'Banana']

lst.sort(key=str.lower)  # 按字符串小写排序
print(lst)  # ['Apple', 'Banana', 'Orange', 'Pear']

lst.sort(key=lambda x: x[1])  # 按第1个字符大小排序
print(lst)  # ['Banana', 'Pear', 'Apple', 'Orange']
