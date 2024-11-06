# 输入学生的成绩，输出学生的等级
score = int(input("input score > "))
match (score//10):
    case 10 | 9:
        print("A")
    case 8:
        print("B")
    case 7:
        print("C")
    case 6:
        print("D")
    case _:
        print("E")


# 输入整数判断和另外一个整数是否相等
x=1234
num = int(input("input number > "))

match num:
    case x:
        print(x,num)

# 匹配模式可以是构造类型
# 匹配模式匹配列表,匹配模式匹配元组
# x = input("input list > ").split(sep=',')
# x = list(map(int, x))  # 将列表中的字符串转为整数，重新构造列表
# x = eval(input("input  > "))
# print(x, type(x))
# match x:
#     case [11, 22, 33]:
#         print("匹配列表成功")
#     case (11, 22, 33):
#         print("匹配元组成功")
# 上述的代码区分不出来元组和列表，因为匹配的时候是根据值匹配的
x = eval(input("input type > "))
print(x, type(x))
match type(x).__name__:
    case "list":
        print("这是列表", x)
    case "tuple":
        print("这是元组", x)
    case "int":
        print("这是整形",x)
    case "str":
        print("这是字符串类型",x)
    case _:
        print("这是其他类型",x)