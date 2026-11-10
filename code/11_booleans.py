print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# 값이 있으면 True
print(bool("Hello"))
print(bool(15))
print(bool(["apple", "cherry"]))

# 비어있거나 0, None 이면 False
print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None))

def my_function():
    return True

if my_function():
    print("YES!")
