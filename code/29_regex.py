import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)
print(x is not None)

print(re.findall("ai", txt))

x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())

print(re.split(r"\s", txt))
print(re.sub(r"\s", "9", txt))

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.group())

# 활용: 전화번호에서 숫자만 뽑기
phone = "010-1234-5678"
print(re.findall(r"\d+", phone))
