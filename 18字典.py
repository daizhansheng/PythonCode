# 字典的{}创建方式
dt = {"name": "zhangsan", "age": 30, "score": 88.9, (11, 22): 66}
print(dt)
# 字典的dict()字符串创建方式
dt1 = dict(name="zhangsan", age=22, score=66.8)  # 这种只适合字符串
print(dt1)
# 字典的dict()混合类型创建方式
dt2 = dict((("name", "zhangsan"), ("age", 22), ((11, 22), 33)))
print(dt2)

# 字典推导式
import random

dt3 = {i: random.randint(1, 100) for i in range(4)}
print(dt3)

# 使用zip函数创建字典
lst1 = ["name", "age", "score"]
lst2 = ["zhangsan", 24, 88.9]
# dt4 = {zip(lst1,lst2)} #这种写法是错误的，因为返回的是迭代器对象
dt4 = dict(zip(lst1, lst2))
print(dt4)  # {'name': 'zhangsan', 'age': 24, 'score': 88.9}

keys = ["name", "age", "city"]
values = ["David", 35, "Miami"]
my_dict = {key: value for key, value in zip(keys, values)}
print(my_dict)

#####################成员获取###################################
# 根据键获取值
print(my_dict["age"])  # 35
print(my_dict.get("age","成员不存在"))
# 获取键值对的视图items
print(
    my_dict.items()
)  # dict_items([('name', 'David'), ('age', 35), ('city', 'Miami')])

for item in my_dict.items():
    print(item)
for key,value in my_dict.items():
    print(key,value)

#########################常见操作函数#############################
# 获取所有键keys
print(my_dict.keys())  # dict_keys(['name', 'age', 'city'])
# 获取所有值values
print(my_dict.values())  # dict_values(['David', 35, 'Miami'])
# pop后删除键值对
print(my_dict.pop("city"))
print(my_dict)
# popitem()随机从字典中去除一个键值对，结果是元组
print(my_dict.popitem())
print(my_dict)
# update字典成员更新
my_dict.update({"age":35,"city":"beijing"})
print(my_dict)