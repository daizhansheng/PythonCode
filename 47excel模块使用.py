from openpyxl import *
from get_weather import *
wb = Workbook()
ws = wb.active

result = get_info_from_url()
lst = get_weather(result)

for item in lst:
    ws.append(item)

wb.save("天气.xlsx")

wb = load_workbook("天气.xlsx")
ws = wb['Sheet']

lst=[]
for row in ws.rows:
    sublst=[]
    for item in row:
        sublst.append(item.value)
    lst.append(sublst)

print(lst)

