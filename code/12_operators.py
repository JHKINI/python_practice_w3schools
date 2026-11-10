x = 15
y = 4

# 산술 연산자
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)    # 나머지
print(x ** 2)   # 거듭제곱
print(x // y)   # 몫

# 대입 연산자
x += 3
print(x)

# 비교 연산자
print(x == y)
print(x != y)

# 논리 연산자
a = 5
print(a > 3 and a < 10)
print(a > 3 or a < 4)
print(not(a > 3 and a < 10))

# 식별 연산자
list1 = ["apple", "banana"]
list2 = ["apple", "banana"]
list3 = list1
print(list1 is list3)   # 같은 객체
print(list1 is list2)   # 내용은 같지만 다른 객체
print(list1 == list2)

# 멤버십 연산자
print("banana" in list1)
print("cherry" not in list1)

# 비트 연산자
print(6 & 3)
print(6 | 3)
