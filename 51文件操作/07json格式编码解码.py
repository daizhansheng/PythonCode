import json

lst = [
    {"name": "zhangsan", "age": 20, "score": 88.6},
    {"name": "lisi", "age": 24, "score": 67.0},
    {"name": "wangwu", "age": 18, "score": 100},
]
# 控制 JSON 字符串的缩进级别。指定一个非负整数 n 表示每层缩进 n 个空格。
s = json.dumps(lst, indent=4)
print(type(s))
print(s)

lst1 = json.loads(s)
print(lst1)

with open("json.txt", "w+", encoding="utf-8") as file:
    json.dump(lst1, file, indent=4)

with open("json.txt","r") as file:
    lst3 = json.load(file)
    print(lst3)