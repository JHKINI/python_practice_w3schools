a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
print(a)

b = "Hello, World!"
print(b[1])        # 인덱스
print(b[2:5])      # 슬라이싱
print(b[-5:-2])    # 뒤에서부터
print(len(b))      # 길이

print("free" in "The best things in life are free!")

# 문자열 메서드
c = " Hello, World! "
print(c.upper())
print(c.lower())
print(c.strip())
print(c.replace("H", "J"))
print(c.split(","))

# 이어붙이기
first = "Hello"
second = "World"
print(first + " " + second)

# 반복문으로 한 글자씩
for ch in "banana":
    print(ch, end=" ")
print()
