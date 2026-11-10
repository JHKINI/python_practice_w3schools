class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# 객체는 서로 독립적
p2 = MyClass()
p2.x = 10
print(p1.x)
print(p2.x)

# 객체 삭제
del p2
try:
    print(p2)
except NameError:
    print("p2 is deleted")

# 빈 클래스
class Person:
    pass

print(type(Person()))
