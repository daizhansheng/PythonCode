def get_num(num):
    start=1
    while start < num:
        yield start
        start+=1

creatitor = get_num(50)
print(creatitor)

for item in get_num(20):
    print(item)
