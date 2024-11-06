import requests
import re

def get_info_from_url():
    url = "https://www.weather.com.cn/forecast/"
    result = requests.get(url)
    result.encoding = "utf-8"
    return result.text

def get_weather(result):
    city = re.findall('<span class="name">([\u4e00-\u9fff]*)</span>', result)
    weather = re.findall('<span class="weather">([\u4e00-\u9fff]*)</span>', result)
    wd = re.findall('<span class="wd">(.*)</span>', result)
    zs = re.findall('<span class="zs">([\u4e00-\u9fff]*)</span>', result)
    lst = []
    for a, b, c, d in zip(city, weather, wd, zs):
        lst.append([a, b, c, d])
    return lst

