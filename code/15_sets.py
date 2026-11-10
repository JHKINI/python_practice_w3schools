thisset = {"apple", "banana", "cherry", "apple"}
print(len(thisset))            # 중복은 하나로
print("banana" in thisset)

thisset.add("orange")
thisset.remove("banana")
thisset.discard("kiwi")        # 없어도 에러 X
print(sorted(thisset))         # 순서가 없으니 정렬해서 확인

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(len(set3))

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.intersection(y))
print(sorted(x.difference(y)))
print(sorted(x.symmetric_difference(y)))

# True 와 1 은 같은 값으로 취급된다
myset = {"apple", True, 1, 2}
print(len(myset))   # 4개를 넣었지만 3개
