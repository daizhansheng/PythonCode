import time

t = time.localtime()
print(type(t),t)
print(time.strftime("%Y-%m-%d %H:%M:%S week=%A  month=%B",t))

print(time.strptime("2024-11-04 11:56:18 week=Monday  month=November","%Y-%m-%d %H:%M:%S week=%A  month=%B"))