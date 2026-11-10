thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)
print(len(thistuple))
print(thistuple[1])

one_item = ("apple",)
print(type(one_item))
not_tuple = ("apple")
print(type(not_tuple))

# 튜플 수정하기 (리스트로 바꿨다가 다시 튜플로)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# 언패킹
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# * 로 나머지 받기
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(tropic)

# 메서드
print(thistuple.count("apple"))
print(thistuple.index("cherry"))
