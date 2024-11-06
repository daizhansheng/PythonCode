# 输入字符，判断是否是a-z
x = input("input chr > ")

if ord('a') <= ord(x) <= ord('z'):
    print(x)
else:
    print("input error")

#输入整数获取个十百位
try:
    y = input("input num> ")
    if len(y) > 3:
        raise ValueError("input not three num")

    y = int(y)
    bai = y//100
    shi = y//10%10
    ge = y%10
    print(f"百位={bai},十位 = {shi},ge = {ge}")
except ValueError as e:
    print("error:",e)

# if的双分支结构，输入开机密码，判断是否正确
pd = input("input passwd > ")
if pd == "abc123":
    print("密码输入正确，正在开机")
else:
    print("密码输入错误请重试")

print("密码输入正确，正在开机") if pd == "abc123" else print("密码输入错误请重试")
print("密码输入正确，正在开机" if pd == "abc123" else "密码输入错误请重试")


# if的多分支结构，输入学生的成绩输出等级
try:
    score = int(input("input score> "))
    if score < 0 or score > 100:
        print("输入的学生成绩不合法，range[0-100]")
        exit(-1)
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")
except ValueError as e:
    print("input score error:", e)
