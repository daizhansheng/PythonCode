def show_info(name, age, score):
    print(f"name = {name},age = {age},score = {score:.2f}")


show_info("zhangsan", 25, 88.6)  # 位置传参
show_info(age=35, name="lisi", score=87.123)  # 关键字传参
show_info(
    "王五", score=88.4312, age=34
)  # 位置和关键字传参混合，前面是位置传参后面是关键字传参，否则错误



#默认值传参,默认参数从又向左,否则错误
def show_person_info(name="zhangsan",age=22,score=66.78):
    print(f"name = {name},age = {age},score = {score:.2f}")

show_person_info()
show_person_info("lisi")
show_person_info(age=15)
show_person_info("田七",score=100)