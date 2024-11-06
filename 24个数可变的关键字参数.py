def fun(**args):  # 这里是字典
    for key, value in args.items():
        print(f"{key}={value}", end="|")


fun(name="lisi", age=50, score=88.6)
print()

d={"name":"lisi","age":50,"score":88}
fun(**d)  # 系列解包
