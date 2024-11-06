import re

s = "www.baidu.com"
partten = r"www"  # 这里的r表示原始字符串，不进行转义
match = re.match(partten, s)  # 从开头匹配，匹配成功返回，否则返回None
print(match)  # <re.Match object; span=(0, 3), match='www'>
print(match.group(0))  # www

s = "abc123sdfsadf3523435435"
partten = r"\d+"
# 从字符串中搜索第一次出现的满足一个或者多个0-9数字字符串
search = re.search(partten, s)
print(search)  # <re.Match object; span=(3, 6), match='123'>

s = "abc123sdfsadf352343erwer"
partten = r"\d+"
find = re.findall(partten, s)  # 搜索所有满足添加字符串，返回搜索到的列表
print(find)  # ['123', '352343']

partten = r"\D+"
find = re.findall(partten, s)  # 搜索所有满足添加字符串，返回搜索到的列表
print(find)  # ['abc', 'sdfsadf', 'erwer']

s = "abc123sdfsadf352343erwer"
partten = r"(?P<s1>\D+)(?:\d+)(?P<s2>\D+)(?:\d+)(?P<s3>\D+)"
match = re.search(partten, s)  # 搜索所有满足添加字符串，返回搜索到的列表
print(match.group(0))  # abc123sdfsadf352343erwer
print("s1:", match.group("s1"))  # 输出：s1: abc
print("s2:", match.group("s2"))  # 输出：s2: sdfsadf
print("s3:", match.group("s3"))  # 输出：s3: erwer

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.+[a-zA-Z]{2,}'
text = 'Please contact us at support@example.com'
match = re.search(pattern, text)
if match:
    print(match.group())  # 输出：support@example.com

pattern=r"\d{4}-\d{2}-\d{2}"
text = 'The date is 2023-04-05'
match = re.search(pattern, text)
print(match)
print(match.group())

pattern=r"https://(?:\w{3}\.)?[^/\s]+(?:/[^/\s]*)*"
text = 'Check this out: https://www.example.com/some/path'
match = re.search(pattern, text)
print(match.group())

x = "PasswFd1"
pattern = r"(?=[A-Z])(?=.*\d)[A-Za-z\d]{8,}"
match = re.search(pattern, x)
if match:
    print(match.group(0))
    #(?=[A-Z])：这是一个正向前瞻断言，确保字符串以大写字母开头。
    #(?=.*\d)：确保字符串中包含至少一个数字。
    #[A-Za-z\d]{8,}：匹配至少8个字符，加上前面的断言，总长度为至少8个字符。
else:
    print("密码输入错误")