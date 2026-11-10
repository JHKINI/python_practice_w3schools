import random

x = 1      # int
y = 2.8    # float
z = 1j     # complex

print(type(x))
print(type(y))
print(type(z))

# 타입 변환
a = float(x)
b = int(y)    # 소수점 아래는 버려진다
print(a)
print(b)

# 과학적 표기법 (e = 10의 거듭제곱)
c = 35e3
print(c)

# 1~9 사이 난수
print(random.randrange(1, 10))
