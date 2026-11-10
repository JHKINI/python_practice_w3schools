# mymodule.py 파일 내용
# def greeting(name):
#     print("Hello, " + name)
#
# person1 = {"name": "John", "age": 36, "country": "Norway"}

import mymodule
mymodule.greeting("Jonathan")
print(mymodule.person1["age"])

# 별명 붙이기
import mymodule as mx
print(mx.person1["country"])

# 일부만 가져오기
from mymodule import person1
print(person1["name"])

# 내장 모듈
import platform
print(type(platform.system()))

print([name for name in dir(mymodule) if not name.startswith("__")])
