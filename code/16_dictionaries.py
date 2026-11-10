thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))
print(len(thisdict))

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

# 수정 / 추가
thisdict["year"] = 2018
thisdict.update({"color": "red"})
print(thisdict)

# 삭제
thisdict.pop("model")
print(thisdict)

# 반복
for key, value in thisdict.items():
    print(key, value)

# 중첩 딕셔너리
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007}
}
print(myfamily["child2"]["name"])
