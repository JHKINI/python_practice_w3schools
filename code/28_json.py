import json

# JSON → Python
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

# Python → JSON
person = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ("Ann", "Billy"),
    "pets": None
}
print(json.dumps(person))

# 보기 좋게
print(json.dumps(person, indent=4, sort_keys=True))

# 한글
print(json.dumps({"이름": "진희"}))
print(json.dumps({"이름": "진희"}, ensure_ascii=False))
