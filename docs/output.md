# 아웃풋
```
# Print "Hello World!"
print("Hello, World!")
# Print "Have a good day."
print("Have a good day.")
# Print "Learning Python is fun!"
print("Learning Python is fun!")
```
### 실행 결과
```
Hello, World!
Have a good day.
Learning Python is fun!
```


# 주석처리 하기
```
# Write a single-line comment
#This is a comment
# Comment out this line so it does not run:
#print("This should not run")#
```
# Add a multiline comment
```
"""
This is a multiiline
comment
"""
```

# 변수
```
x=5
y="John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)
```
### 실행 결과
```
5
John
Sally
```

# 변수_캐스팅
```
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
```
### 실행 결과
```
3
3
3.0
```
# 변수_타입구하기
```
x=5
y="John"
print(type(x))
print(type(y))
```
### 실행 결과
```
<class 'int'>
<class 'str'>
```

# "" 와''차이
```
a = "John"
b = 'John'
print(a)
print(b)
```
### 실행 결과
```
John
John
```

# 대소문자 구분
```
a=4
A="Sally"
print(a)
print(A)
```
### 실행 결과
```
4
Sally
```
# 변수이름

```
import random
a=[1,2,3]
선택= random.choice(a)
print(선택)
```

# 반복문을 활용한 데이터 처리 기초

## 1. range()

range()는 연속된 숫자 범위를 생성하는 함수이다.

- 기본 형태: range(시작, 끝, 간격)
- 끝 값은 포함되지 않는다.

```python
nums = list(range(0, 10))
print(nums)
```

### 실행 결과
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 2. for문을 이용한 데이터 처리

리스트 데이터를 반복문으로 하나씩 꺼내 처리할 수 있다.

```python
nums = [1, 2, 3, 4, 5]

for i in nums:
    print(i)
```

### 실행 결과
```
1
2
3
4
5
```

---

## 3. 반복문 활용 예시 (합계 구하기)

반복문을 이용하면 여러 값의 합을 쉽게 구할 수 있다.

```python
nums = [1, 2, 3, 4, 5]
total = 0

for i in nums:
    total = total + i

print(total)
```

### 실행 결과
```
15
```

---

## 📌 느낀 점

- 반복문을 이용하면 여러 데이터를 효율적으로 처리할 수 있다.
- 특히 합계 계산처럼 데이터 분석의 기초 작업에 활용될 수 있다.
- 아직은 익숙하지 않지만 점점 이해하고 있다.

---

# 📚 W3Schools Python Tutorial 정리

[W3Schools Python Tutorial](https://www.w3schools.com/python/) 목차를 따라 공부한 내용을 정리했다.
예제 코드는 `code/` 폴더에 번호 순서대로 저장되어 있다.

**Python Tutorial**

1. 파이썬 시작하기 & 문법(Syntax)
2. 데이터 타입
3. 숫자 (Numbers)
4. 캐스팅 (Casting)
5. 문자열 (Strings)
6. 불리언 (Booleans)
7. 연산자 (Operators)
8. 리스트 (Lists)
9. 튜플 (Tuples)
10. 세트 (Sets)
11. 딕셔너리 (Dictionaries)
12. 조건문 (If...Else)
13. Match 문
14. While 반복문
15. For 반복문
16. 함수 (Functions)
17. range() 함수
18. 배열 (Arrays)
19. 이터레이터 (Iterators)
20. 모듈 (Modules)
21. 날짜 (Dates)
22. 수학 (Math)
23. JSON
24. 정규표현식 (RegEx)
25. PIP
26. 예외 처리 (Try...Except)
27. 문자열 포매팅 (String Formatting)
28. None
29. 사용자 입력 (User Input)
30. 가상환경 (VirtualEnv)

**Python Classes**

1. 객체지향 프로그래밍 (OOP)
2. 클래스 / 객체 (Classes/Objects)
3. __init__ 메서드
4. self 매개변수
5. 클래스 속성 (Class Properties)
6. 클래스 메서드 (Class Methods)
7. 매직 메서드 (Magic Methods)
8. 상속 (Inheritance)
9. 다형성 (Polymorphism)
10. 캡슐화 (Encapsulation)
11. 내부 클래스 (Inner Classes)

---

# 파이썬 시작하기 & 문법(Syntax)

- 파이썬은 인터프리터 언어라서 코드를 작성하고 바로 실행할 수 있다.
- 설치 확인은 터미널에서 `python --version` 으로 한다.
- 파이썬은 중괄호 `{}` 대신 **들여쓰기(Indentation)** 로 코드 블록을 구분한다.
- 들여쓰기 칸 수는 자유지만 같은 블록 안에서는 반드시 똑같아야 한다. (보통 4칸)

📁 `code/06_syntax.py`

```python
# Indentation: 들여쓰기로 블록을 구분한다
if 5 > 2:
    print("Five is greater than two!")

# 같은 블록 안에서는 들여쓰기 칸 수가 같아야 한다
if 5 > 2:
    print("Five is greater than two!")
    print("Still inside the if block")

print("Outside the if block")
```
### 실행 결과
```
Five is greater than two!
Five is greater than two!
Still inside the if block
Outside the if block
```

---

# 데이터 타입

- 파이썬의 기본 자료형: 문자(str), 숫자(int, float, complex), 시퀀스(list, tuple, range), 매핑(dict), 집합(set, frozenset), 불(bool), 바이너리(bytes...), None
- 변수에 값을 넣는 순간 타입이 자동으로 정해진다.
- `type()` 으로 타입을 확인할 수 있다.

📁 `code/07_data_types.py`

```python
x1 = "Hello World"
x2 = 20
x3 = 20.5
x4 = 1j
x5 = ["apple", "banana", "cherry"]
x6 = ("apple", "banana", "cherry")
x7 = range(6)
x8 = {"name": "John", "age": 36}
x9 = {"apple", "banana", "cherry"}
x10 = True
x11 = None

print(type(x1))
print(type(x2))
print(type(x3))
print(type(x4))
print(type(x5))
print(type(x6))
print(type(x7))
print(type(x8))
print(type(x9))
print(type(x10))
print(type(x11))
```
### 실행 결과
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'list'>
<class 'tuple'>
<class 'range'>
<class 'dict'>
<class 'set'>
<class 'bool'>
<class 'NoneType'>
```

---

# 숫자 (Numbers)

- 숫자 타입은 int(정수), float(실수), complex(복소수) 3가지이다.
- int → float 처럼 타입 변환이 가능하지만 complex는 다른 숫자로 바꿀 수 없다.
- `random` 모듈로 난수를 만들 수 있다.

📁 `code/08_numbers.py`

```python
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
```
### 실행 결과
```
<class 'int'>
<class 'float'>
<class 'complex'>
1.0
2
35000.0
8
```

※ 마지막 줄은 난수라서 실행할 때마다 값이 달라진다.

---

# 캐스팅 (Casting)

- 캐스팅 = 변수의 타입을 직접 지정/변환하는 것
- `int()` : 정수로 (실수는 소수점 버림, 문자열은 정수 형태여야 함)
- `float()` : 실수로
- `str()` : 문자열로

📁 `code/09_casting.py`

```python
x = int(1)
y = int(2.8)
z = int("3")
print(x, y, z)

a = float(1)
b = float(2.8)
c = float("3")
d = float("4.2")
print(a, b, c, d)

e = str("s1")
f = str(2)
g = str(3.0)
print(e, f, g)
```
### 실행 결과
```
1 2 3
1.0 2.8 3.0 4.2
s1 2 3.0
```

---

# 문자열 (Strings)

- 문자열은 `""` 나 `''` 로 감싼다. 여러 줄은 `"""` 를 쓴다.
- 문자열은 문자들의 배열이라서 인덱스와 슬라이싱 `[시작:끝]` 이 가능하다.
- `upper()`, `lower()`, `strip()`, `replace()`, `split()` 같은 메서드가 있다.
- `in` 으로 포함 여부를 확인하고, `+` 로 이어붙인다.

📁 `code/10_strings.py`

```python
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
```
### 실행 결과
```
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
e
llo
orl
13
True
 HELLO, WORLD! 
 hello, world! 
Hello, World!
 Jello, World! 
[' Hello', ' World! ']
Hello World
b a n a n a 
```

---

# 불리언 (Booleans)

- 불리언은 `True` 또는 `False` 두 값만 가진다.
- 비교 연산의 결과는 불리언이다.
- `bool()` 은 값이 있으면 대부분 True, 비어 있거나 0/None이면 False를 돌려준다.

📁 `code/11_booleans.py`

```python
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
```
### 실행 결과
```
True
False
False
b is not greater than a
True
True
True
False
False
False
False
YES!
```

---

# 연산자 (Operators)

- 산술: `+ - * / % ** //`
- 대입: `= += -= *= /=` ...
- 비교: `== != > < >= <=`
- 논리: `and or not`
- 식별: `is`, `is not` (같은 객체인지)
- 멤버십: `in`, `not in`
- 비트: `& | ^ ~ << >>`

📁 `code/12_operators.py`

```python
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
```
### 실행 결과
```
19
11
60
3.75
3
225
3
18
False
True
True
True
False
True
False
True
True
True
2
7
```

---

# 리스트 (Lists)

- 리스트는 `[]` 로 만들고 **순서 O, 변경 O, 중복 O** 이다.
- 인덱스로 접근/수정하고, `append()`, `insert()`, `extend()` 로 추가한다.
- `remove()`, `pop()`, `del`, `clear()` 로 삭제한다.
- `sort()` 로 정렬, `copy()` 로 복사, 리스트 컴프리헨션으로 새 리스트를 짧게 만들 수 있다.

📁 `code/13_lists.py`

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist[0])
print(thislist[-1])
print(thislist[1:3])

# 값 변경
thislist[1] = "blackcurrant"
print(thislist)

# 추가
thislist.append("orange")
thislist.insert(1, "lemon")
print(thislist)

tropical = ["mango", "pineapple"]
thislist.extend(tropical)
print(thislist)

# 삭제
thislist.remove("lemon")
thislist.pop()          # 마지막 삭제
del thislist[0]
print(thislist)

# 반복
for x in thislist:
    print(x)

# 리스트 컴프리헨션
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# 정렬
nums = [100, 50, 65, 82, 23]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# 복사 & 합치기
copy_list = fruits.copy()
print(copy_list)
print([1, 2] + [3, 4])
```
### 실행 결과
```
['apple', 'banana', 'cherry']
3
apple
cherry
['banana', 'cherry']
['apple', 'blackcurrant', 'cherry']
['apple', 'lemon', 'blackcurrant', 'cherry', 'orange']
['apple', 'lemon', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple']
['blackcurrant', 'cherry', 'orange', 'mango']
blackcurrant
cherry
orange
mango
['apple', 'banana', 'mango']
[23, 50, 65, 82, 100]
[100, 82, 65, 50, 23]
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[1, 2, 3, 4]
```

---

# 튜플 (Tuples)

- 튜플은 `()` 로 만들고 **순서 O, 변경 X, 중복 O** 이다.
- 값이 하나인 튜플은 반드시 `("apple",)` 처럼 쉼표를 붙인다.
- 바꾸고 싶으면 리스트로 변환 → 수정 → 다시 튜플로 변환한다.
- 언패킹(Unpacking)으로 값을 변수에 나눠 담을 수 있다.

📁 `code/14_tuples.py`

```python
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
```
### 실행 결과
```
('apple', 'banana', 'cherry', 'apple')
4
banana
<class 'tuple'>
<class 'str'>
('apple', 'kiwi', 'cherry')
apple
banana
cherry
['mango', 'papaya', 'pineapple']
2
2
```

---

# 세트 (Sets)

- 세트는 `{}` 로 만들고 **순서 X, 변경 X(추가/삭제는 가능), 중복 X** 이다.
- 순서가 없어서 인덱스로 접근할 수 없고 출력 순서도 매번 다를 수 있다.
- `add()`, `update()` 로 추가, `remove()`, `discard()` 로 삭제한다.
- `union()`(합집합), `intersection()`(교집합), `difference()`(차집합) 을 지원한다.

📁 `code/15_sets.py`

```python
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
```
### 실행 결과
```
3
True
['apple', 'cherry', 'orange']
6
{'apple'}
['banana', 'cherry']
['banana', 'cherry', 'google', 'microsoft']
3
```

---

# 딕셔너리 (Dictionaries)

- 딕셔너리는 `{키: 값}` 형태로 **순서 O(3.7+), 변경 O, 키 중복 X** 이다.
- `dict[키]` 또는 `get(키)` 로 값을 꺼낸다.
- `keys()`, `values()`, `items()` 로 전체를 볼 수 있다.
- `update()` 로 추가/수정, `pop()`, `del` 로 삭제한다.

📁 `code/16_dictionaries.py`

```python
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
```
### 실행 결과
```
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Ford
Mustang
3
dict_keys(['brand', 'model', 'year'])
dict_values(['Ford', 'Mustang', 1964])
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}
{'brand': 'Ford', 'year': 2018, 'color': 'red'}
brand Ford
year 2018
color red
Tobias
```

---

# 조건문 (If...Else)

- `if` → `elif` → `else` 순서로 조건을 검사한다.
- 한 줄로 쓰는 축약형(삼항 연산자)도 있다.
- `and`, `or` 로 조건을 묶고, 빈 블록은 `pass` 로 채운다.

📁 `code/17_if_else.py`

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# 한 줄 if
if a > b: print("a is greater than b")

# 삼항 연산자
print("A") if a > b else print("B")

# and / or
c = 500
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one of the conditions is True")

# 중첩 if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# pass
if b > a:
    pass
```
### 실행 결과
```
a is greater than b
a is greater than b
A
Both conditions are True
At least one of the conditions is True
Above ten,
and also above 20!
```

---

# Match 문

- 파이썬 3.10부터 생긴 문법으로, 다른 언어의 switch 문과 비슷하다.
- `case _:` 는 어떤 경우에도 맞지 않을 때 실행되는 기본값이다.
- `|` 로 여러 값을 한 번에 검사하고, `if` 로 조건(가드)을 추가할 수 있다.

📁 `code/18_match.py`

```python
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend")

# | 로 여러 값 묶기
day = 6
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

# if 가드
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
```
### 실행 결과
```
Thursday
I love weekends!
A weekday in May
```

---

# While 반복문

- `while` 은 조건이 True인 동안 계속 반복한다.
- 조건 변수를 바꿔주지 않으면 무한 반복이 되니 주의!
- `break` 는 반복 종료, `continue` 는 이번 회차만 건너뛰기, `else` 는 조건이 False가 되면 한 번 실행된다.

📁 `code/19_while_loops.py`

```python
i = 1
while i < 6:
    print(i)
    i += 1

print("--- break ---")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("--- continue ---")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("--- else ---")
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("i is no longer less than 4")
```
### 실행 결과
```
1
2
3
4
5
--- break ---
1
2
3
--- continue ---
1
2
4
5
6
--- else ---
1
2
3
i is no longer less than 4
```

---

# For 반복문

- `for` 는 리스트, 튜플, 문자열 같은 시퀀스를 하나씩 꺼내며 반복한다.
- `break`, `continue`, `else` 를 while과 똑같이 쓸 수 있다.
- 반복문 안에 반복문을 넣는 중첩 반복도 가능하다.

📁 `code/20_for_loops.py`

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x, end=" ")
print()

print("--- break ---")
for x in fruits:
    if x == "banana":
        break
    print(x)

print("--- continue ---")
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("--- else ---")
for x in range(3):
    print(x)
else:
    print("Finally finished!")

print("--- 중첩 반복 ---")
adj = ["red", "big"]
fruits = ["apple", "banana"]
for a in adj:
    for f in fruits:
        print(a, f)
```
### 실행 결과
```
apple
banana
cherry
b a n a n a 
--- break ---
apple
--- continue ---
apple
cherry
--- else ---
0
1
2
Finally finished!
--- 중첩 반복 ---
red apple
red banana
big apple
big banana
```

---

# 함수 (Functions)

- `def 함수이름():` 으로 함수를 만들고 `함수이름()` 으로 호출한다.
- 매개변수(parameter)로 값을 받고 `return` 으로 결과를 돌려준다.
- 기본값 매개변수, 키워드 인자, `*args`(개수 모를 때), `**kwargs`(키워드 개수 모를 때) 를 쓸 수 있다.
- `lambda` 로 한 줄짜리 익명 함수를 만들 수 있다.

📁 `code/21_functions.py`

```python
def my_function():
    print("Hello from a function")

my_function()

# 매개변수
def greet(fname):
    print(fname + " Refsnes")

greet("Emil")
greet("Tobias")

# 반환값
def times_five(x):
    return 5 * x

print(times_five(3))

# 기본값 매개변수
def my_country(country="Norway"):
    print("I am from " + country)

my_country("Sweden")
my_country()

# 키워드 인자
def kids(child3, child2, child1):
    print("The youngest child is " + child3)

kids(child1="Emil", child2="Tobias", child3="Linus")

# *args
def youngest(*kids):
    print("The youngest child is " + kids[2])

youngest("Emil", "Tobias", "Linus")

# **kwargs
def last_name(**kid):
    print("His last name is " + kid["lname"])

last_name(fname="Tobias", lname="Refsnes")

# 재귀 함수
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)

# lambda
add_ten = lambda a: a + 10
print(add_ten(5))
multiply = lambda a, b: a * b
print(multiply(5, 6))
```
### 실행 결과
```
Hello from a function
Emil Refsnes
Tobias Refsnes
15
I am from Sweden
I am from Norway
The youngest child is Linus
The youngest child is Linus
His last name is Refsnes
3
2
1
Done!
15
30
```

---

# range() 함수

- `range(끝)`, `range(시작, 끝)`, `range(시작, 끝, 간격)` 형태로 쓴다.
- 끝 값은 포함되지 않는다.
- 간격에 음수를 넣으면 거꾸로 셀 수 있다.

📁 `code/22_range.py`

```python
for x in range(5):
    print(x, end=" ")
print()

for x in range(3, 8):
    print(x, end=" ")
print()

for x in range(0, 20, 5):
    print(x, end=" ")
print()

for x in range(10, 0, -2):
    print(x, end=" ")
print()

r = range(10)
print(list(r))
print(len(r))
print(r[3])
print(7 in r)
```
### 실행 결과
```
0 1 2 3 4 
3 4 5 6 7 
0 5 10 15 
10 8 6 4 2 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
10
3
True
```

---

# 배열 (Arrays)

- 파이썬에는 기본 배열 대신 **리스트** 를 배열처럼 사용한다.
- (진짜 배열이 필요하면 NumPy 같은 라이브러리를 쓴다.)
- 배열 = 하나의 변수에 여러 값을 담는 것.

📁 `code/23_arrays.py`

```python
cars = ["Ford", "Volvo", "BMW"]

print(cars[0])
cars[0] = "Toyota"
print(cars)
print(len(cars))

for x in cars:
    print(x)

cars.append("Honda")
print(cars)

cars.pop(1)
print(cars)

cars.remove("BMW")
print(cars)
```
### 실행 결과
```
Ford
['Toyota', 'Volvo', 'BMW']
3
Toyota
Volvo
BMW
['Toyota', 'Volvo', 'BMW', 'Honda']
['Toyota', 'BMW', 'Honda']
['Toyota', 'Honda']
```

---

# 이터레이터 (Iterators)

- 이터레이터 = `__iter__()` 와 `__next__()` 를 가진, 값을 하나씩 꺼낼 수 있는 객체
- 리스트, 튜플, 문자열 등은 `iter()` 로 이터레이터를 만들 수 있다.
- 직접 클래스를 만들 때 `__next__()` 에서 `StopIteration` 을 일으키면 반복이 끝난다.

📁 `code/24_iterators.py`

```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# 직접 만든 이터레이터
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
for x in myclass:
    print(x)
```
### 실행 결과
```
apple
banana
cherry
1
2
3
4
5
```

---

# 모듈 (Modules)

- 모듈 = 함수/변수를 모아둔 `.py` 파일
- `import 모듈명` 으로 불러오고 `모듈명.함수()` 로 사용한다.
- `as` 로 별명을 붙이고, `from 모듈 import 이름` 으로 일부만 가져올 수 있다.
- `dir()` 로 모듈 안에 있는 이름들을 볼 수 있다.
- 예제용 모듈 파일: `code/mymodule.py`

📁 `code/25_modules.py`

```python
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
```
### 실행 결과
```
Hello, Jonathan
36
Norway
John
<class 'str'>
['greeting', 'person1']
```

---

# 날짜 (Dates)

- `datetime` 모듈로 날짜와 시간을 다룬다.
- `datetime.datetime.now()` 는 현재 시각, `datetime.datetime(년, 월, 일)` 은 원하는 날짜를 만든다.
- `strftime()` 으로 원하는 형식의 문자열로 바꾼다. (`%Y` 연도, `%m` 월, `%d` 일, `%A` 요일, `%B` 월 이름...)

📁 `code/26_dates.py`

```python
import datetime

# 현재 시각 (실행할 때마다 달라짐)
now = datetime.datetime.now()
print(type(now))

# 날짜 만들기
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.year)
print(x.strftime("%A"))

# strftime 형식
y = datetime.datetime(2018, 6, 1)
print(y.strftime("%B"))
print(y.strftime("%Y-%m-%d"))
print(y.strftime("%Y년 %m월 %d일"))

# 날짜 계산
d1 = datetime.date(2026, 1, 1)
d2 = datetime.date(2026, 12, 25)
print((d2 - d1).days)
```
### 실행 결과
```
<class 'datetime.datetime'>
2020-05-17 00:00:00
2020
Sunday
June
2018-06-01
2018년 06월 01일
358
```

---

# 수학 (Math)

- 내장 함수: `min()`, `max()`, `abs()`, `pow()`
- `math` 모듈: `math.sqrt()`, `math.ceil()`(올림), `math.floor()`(내림), `math.pi`

📁 `code/27_math.py`

```python
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

print(abs(-7.25))
print(pow(4, 3))

import math

print(math.sqrt(64))
print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi)
```
### 실행 결과
```
5
25
7.25
64
8.0
2
1
3.141592653589793
```

---

# JSON

- JSON = 데이터를 저장/전송하기 위한 텍스트 형식
- `json.loads()` : JSON 문자열 → 파이썬 딕셔너리
- `json.dumps()` : 파이썬 객체 → JSON 문자열
- `indent`, `sort_keys` 옵션으로 보기 좋게 출력할 수 있다.
- 한글이 깨지면 `ensure_ascii=False` 를 준다.

📁 `code/28_json.py`

```python
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
```
### 실행 결과
```
30
{"name": "John", "age": 30, "married": true, "children": ["Ann", "Billy"], "pets": null}
{
    "age": 30,
    "children": [
        "Ann",
        "Billy"
    ],
    "married": true,
    "name": "John",
    "pets": null
}
{"\uc774\ub984": "\uc9c4\ud76c"}
{"이름": "진희"}
```

---

# 정규표현식 (RegEx)

- `re` 모듈로 문자열 패턴을 검색한다.
- `findall()` : 모두 찾아 리스트로, `search()` : 처음 하나 찾기, `split()` : 패턴으로 나누기, `sub()` : 바꾸기
- 자주 쓰는 패턴: `^` 시작, `$` 끝, `\d` 숫자, `\s` 공백, `\w` 문자, `+` 1개 이상, `*` 0개 이상

📁 `code/29_regex.py`

```python
import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)
print(x is not None)

print(re.findall("ai", txt))

x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())

print(re.split(r"\s", txt))
print(re.sub(r"\s", "9", txt))

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.group())

# 활용: 전화번호에서 숫자만 뽑기
phone = "010-1234-5678"
print(re.findall(r"\d+", phone))
```
### 실행 결과
```
True
['ai', 'ai']
The first white-space character is located in position: 3
['The', 'rain', 'in', 'Spain']
The9rain9in9Spain
(12, 17)
Spain
['010', '1234', '5678']
```

---

# PIP

- PIP = 파이썬 패키지(라이브러리) 관리 도구
- 터미널(명령 프롬프트)에서 사용한다. 아래는 터미널 명령어이다.
- 설치한 패키지는 `import` 해서 쓴다.

📁 `code/30_pip.sh`

```bash
# 버전 확인
pip --version

# 패키지 설치
pip install camelcase

# 패키지 삭제
pip uninstall camelcase

# 설치된 패키지 목록
pip list
```

---

# 예외 처리 (Try...Except)

- `try` : 에러가 날 수 있는 코드
- `except` : 에러가 났을 때 실행 (에러 종류별로 나눌 수 있다)
- `else` : 에러가 없을 때 실행, `finally` : 에러 여부와 상관없이 항상 실행
- `raise` 로 직접 에러를 발생시킬 수 있다.

📁 `code/31_try_except.py`

```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("The 'try except' is finished")

# raise
y = -1
try:
    if y < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print(e)

z = "hello"
try:
    if not type(z) is int:
        raise TypeError("Only integers are allowed")
except TypeError as e:
    print(e)
```
### 실행 결과
```
Variable x is not defined
Hello
Nothing went wrong
Error: division by zero
The 'try except' is finished
Sorry, no numbers below zero
Only integers are allowed
```

---

# 문자열 포매팅 (String Formatting)

- f-string: 문자열 앞에 `f` 를 붙이고 `{변수}` 로 값을 넣는다. (파이썬 3.6+)
- `{값:.2f}` 처럼 형식 지정자로 소수점 자리수 등을 정할 수 있다.
- `format()` 메서드 방식도 있다.

📁 `code/32_string_formatting.py`

```python
price = 59
txt = f"The price is {price} dollars"
print(txt)

# 소수점 2자리
txt = f"The price is {price:.2f} dollars"
print(txt)

# 계산식도 넣을 수 있다
print(f"The price is {20 * 59} dollars")

# 천 단위 쉼표
print(f"The price is {59000:,} dollars")

# 조건식
price = 49
print(f"It is very {'Expensive' if price > 50 else 'Cheap'}")

# 함수 호출
fruit = "apples"
print(f"I love {fruit.upper()}")

# format() 메서드
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
```
### 실행 결과
```
The price is 59 dollars
The price is 59.00 dollars
The price is 1180 dollars
The price is 59,000 dollars
It is very Cheap
I love APPLES
I want 3 pieces of item number 567 for 49.00 dollars.
I have a Ford, it is a Mustang.
```

---

# None

- `None` 은 '값이 없음'을 나타내는 특별한 값이다. (0이나 빈 문자열과 다름)
- 타입은 `NoneType` 이다.
- None 확인은 `is None` / `is not None` 으로 한다.
- return이 없는 함수는 None을 돌려준다.

📁 `code/33_none.py`

```python
x = None
print(x)
print(type(x))

if x is None:
    print("x is None")
else:
    print("x has a value")

print(bool(None))

def my_function():
    x = 1

print(my_function())
```
### 실행 결과
```
None
<class 'NoneType'>
x is None
False
None
```

---

# 사용자 입력 (User Input)

- `input()` 으로 사용자에게 값을 입력받는다.
- 입력값은 항상 **문자열(str)** 이라서 숫자로 쓰려면 `int()`, `float()` 로 변환해야 한다.
- 잘못된 값이 들어올 수 있으니 try/except 와 함께 쓰면 좋다.

📁 `code/34_user_input.py`

```python
username = input("Enter username: ")
print("Username is: " + username)

num = input("Enter a number: ")
print(type(num))
num = float(num)
print("The square root is:", num ** 0.5)

# 숫자가 들어올 때까지 다시 입력받기
while True:
    value = input("Enter an integer: ")
    try:
        value = int(value)
        break
    except ValueError:
        print("Wrong input, please try again.")
print("Thank you!", value)
```
### 실행 결과
```
Enter username: Jinhee
Username is: Jinhee
Enter a number: 16
<class 'str'>
The square root is: 4.0
Enter an integer: abc
Wrong input, please try again.
Enter an integer: 7
Thank you! 7
```

※ 입력값으로 `Jinhee`, `16`, `abc`, `7` 을 차례대로 넣었을 때의 결과 (입력한 값도 같이 표시함)

---

# 가상환경 (VirtualEnv)

- 가상환경 = 프로젝트마다 따로 쓰는 독립된 파이썬 환경
- 프로젝트별로 패키지 버전이 충돌하지 않게 해준다.
- `.venv` 폴더는 `.gitignore` 에 넣어서 깃허브에 올리지 않는다. (이 저장소도 `/.venv` 를 제외하고 있음)
- 아래는 터미널 명령어이다.

📁 `code/35_virtualenv.sh`

```bash
# 가상환경 만들기
python -m venv .venv

# 활성화 (Windows)
.venv\Scripts\activate

# 활성화 (macOS / Linux)
source .venv/bin/activate

# 가상환경 안에서 패키지 설치
pip install cowsay

# 설치된 패키지 목록 저장 / 복원
pip freeze > requirements.txt
pip install -r requirements.txt

# 비활성화
deactivate
```

---

# 객체지향 프로그래밍 (OOP)

- OOP = 데이터(속성)와 기능(메서드)을 하나의 **객체** 로 묶어서 프로그래밍하는 방식
- **클래스** 는 설계도, **객체** 는 설계도로 만든 실제 물건이다.
- 장점: 코드 재사용, 구조가 명확함, 유지보수가 쉬움 (DRY: Don't Repeat Yourself)
- 예) 클래스 `Fruit` → 객체 `apple`, `banana`, `mango`

📁 `code/36_oop.py`

```python
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        print(self.name + " is " + self.color)

apple = Fruit("Apple", "red")
banana = Fruit("Banana", "yellow")

apple.describe()
banana.describe()
```
### 실행 결과
```
Apple is red
Banana is yellow
```

---

# 클래스 / 객체 (Classes/Objects)

- `class 클래스이름:` 으로 클래스를 만든다.
- `클래스이름()` 으로 객체를 만든다.
- 같은 클래스로 만든 객체라도 각각 독립적이다.
- `del` 로 객체를 삭제할 수 있고, 빈 클래스는 `pass` 를 쓴다.

📁 `code/37_classes_objects.py`

```python
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
```
### 실행 결과
```
5
5
10
p2 is deleted
<class '__main__.Person'>
```

---

# __init__ 메서드

- `__init__()` 은 객체가 만들어질 때 **자동으로 실행** 되는 함수(생성자)이다.
- 객체의 속성에 처음 값을 넣을 때 사용한다.
- 매개변수에 기본값을 줄 수도 있다.

📁 `code/38_init_method.py`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# 기본값
class Person2:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p2 = Person2("Emil")
p3 = Person2("Tobias", 25)
print(p2.name, p2.age)
print(p3.name, p3.age)
```
### 실행 결과
```
John
36
Emil 18
Tobias 25
```

---

# self 매개변수

- `self` 는 **현재 객체 자기 자신** 을 가리킨다.
- 클래스 안의 메서드는 첫 번째 매개변수로 항상 self를 받는다.
- 이름이 꼭 self일 필요는 없지만 관례상 self를 쓴다.
- self로 같은 객체의 다른 속성이나 메서드에 접근한다.

📁 `code/39_self_parameter.py`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

    def welcome(self):
        self.greet()    # self로 다른 메서드 호출
        print("Welcome!")

p1 = Person("Emil", 25)
p2 = Person("Linus", 30)
p1.greet()
p2.greet()
p1.welcome()

# self 대신 다른 이름도 가능 (권장 X)
class Person2:
    def __init__(myobject, name):
        myobject.name = name

    def greet(abc):
        print("Hello, my name is " + abc.name)

Person2("Tobias").greet()
```
### 실행 결과
```
Hello, my name is Emil
Hello, my name is Linus
Hello, my name is Emil
Welcome!
Hello, my name is Tobias
```

---

# 클래스 속성 (Class Properties)

- **인스턴스 속성** : `__init__` 안에서 `self.이름` 으로 만든 속성 → 객체마다 다름
- **클래스 속성** : 클래스 바로 아래에 만든 속성 → 모든 객체가 공유
- 속성은 수정/삭제(`del`)/추가가 가능하다.

📁 `code/40_class_properties.py`

```python
class Person:
    species = "Human"   # 클래스 속성 (모두 공유)

    def __init__(self, name):
        self.name = name   # 인스턴스 속성

p1 = Person("Emil")
p2 = Person("Tobias")
print(p1.name, p1.species)
print(p2.name, p2.species)

# 클래스 속성을 바꾸면 모든 객체에 적용
Person.species = "Homo sapiens"
print(p1.species)
print(p2.species)

# 속성 수정 / 추가 / 삭제
p1.name = "Linus"
p1.age = 40
print(p1.name, p1.age)

del p1.age
print(hasattr(p1, "age"))
```
### 실행 결과
```
Emil Human
Tobias Human
Homo sapiens
Homo sapiens
Linus 40
False
```

---

# 클래스 메서드 (Class Methods)

- 메서드 = 클래스 안에 정의된 함수
- 메서드에서 객체의 속성을 읽거나 바꿀 수 있다.
- `__str__()` 을 만들면 `print(객체)` 했을 때 보여줄 문자열을 정할 수 있다.

📁 `code/41_class_methods.py`

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Linus", 30)
p1.celebrate_birthday()
p1.celebrate_birthday()
print(p1)
```
### 실행 결과
```
8
28
Happy birthday! You are now 31
Happy birthday! You are now 32
Linus (32)
```

---

# 매직 메서드 (Magic Methods)

- 매직 메서드 = 이름 앞뒤에 `__` (던더, dunder) 가 붙은 특별한 메서드
- 파이썬이 특정 상황에서 자동으로 호출한다.
- `__init__` 생성, `__str__` print용 문자열, `__repr__` 개발자용 문자열, `__len__` len(), `__add__` + 연산, `__eq__` == 비교

📁 `code/42_magic_methods.py`

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __eq__(self, other):
        return self.pages == other.pages

b1 = Book("Python Basics", 300)
b2 = Book("Python OOP", 300)

print(b1)          # __str__
print(repr(b1))    # __repr__
print(len(b1))     # __len__
print(b1 + b2)     # __add__
print(b1 == b2)    # __eq__
```
### 실행 결과
```
Book: Python Basics
Book('Python Basics', 300)
300
600
True
```

---

# 상속 (Inheritance)

- 상속 = 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 것
- `class 자식(부모):` 형태로 만든다.
- `super()` 로 부모의 메서드(`__init__` 등)를 호출한다.
- 자식 클래스에 새 속성/메서드를 추가할 수 있다.

📁 `code/43_inheritance.py`

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# 부모를 그대로 물려받기
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

# super()로 부모 __init__ 호출 + 속성/메서드 추가
class Student2(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)

y = Student2("Mike", "Olsen", 2024)
y.printname()
y.welcome()
print(isinstance(y, Person))
```
### 실행 결과
```
Mike Olsen
Mike Olsen
Welcome Mike Olsen to the class of 2024
True
```

---

# 다형성 (Polymorphism)

- 다형성 = 같은 이름의 메서드가 객체에 따라 다르게 동작하는 것
- 예) `len()` 은 문자열/리스트/딕셔너리 모두에 쓸 수 있다.
- 상속받은 메서드를 자식 클래스에서 다시 정의(오버라이딩)할 수 있다.

📁 `code/44_polymorphism.py`

```python
# 함수의 다형성
print(len("Hello World!"))
print(len(("apple", "banana", "cherry")))
print(len({"brand": "Ford", "model": "Mustang"}))

# 클래스의 다형성
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

for x in (Car("Ford", "Mustang"), Boat("Ibiza", "Touring 20"), Plane("Boeing", "747")):
    x.move()

# 상속 + 오버라이딩
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Move!")

class Bike(Vehicle):
    pass

class Train(Vehicle):
    def move(self):
        print("Ride the rails!")

for v in (Bike("Giant"), Train("KTX")):
    print(v.brand, end=": ")
    v.move()
```
### 실행 결과
```
12
3
2
Drive!
Sail!
Fly!
Giant: Move!
KTX: Ride the rails!
```

---

# 캡슐화 (Encapsulation)

- 캡슐화 = 객체 내부 데이터를 외부에서 함부로 바꾸지 못하게 보호하는 것
- `_이름` : protected (관례상 내부용이라는 표시)
- `__이름` : private (클래스 밖에서 직접 접근 불가)
- getter / setter 메서드로 값을 검증하며 읽고 쓴다. `@property` 를 쓰면 속성처럼 사용할 수 있다.

📁 `code/45_encapsulation.py`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age     # private

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Emil", 25)
print(p1.name)
print(p1.get_age())

try:
    print(p1.__age)
except AttributeError:
    print("Cannot access private property directly")

p1.set_age(26)
print(p1.get_age())
p1.set_age(-5)

# @property 사용
class Student:
    def __init__(self, score):
        self._score = score   # protected

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            print("Score must be 0~100")

s = Student(90)
print(s.score)
s.score = 95
print(s.score)
s.score = 150
```
### 실행 결과
```
Emil
25
Cannot access private property directly
26
Age must be positive
90
95
Score must be 0~100
```

---

# 내부 클래스 (Inner Classes)

- 내부 클래스 = 클래스 안에 정의한 클래스
- 서로 밀접하게 관련된 클래스를 묶어서 정리할 때 사용한다.
- `바깥클래스.안쪽클래스()` 로 객체를 만든다.

📁 `code/46_inner_classes.py`

```python
class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer.name)

inner = Outer.Inner()
print(inner.name)
inner.display()

# 활용 예: Car 안에 Engine
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

    def drive(self):
        self.engine.start()
        print(f"Driving {self.brand} {self.model}")

car = Car("Toyota", "Corolla")
car.drive()
print(car.engine.status)
```
### 실행 결과
```
Outer Class
Inner Class
This is the inner class
Engine started
Driving Toyota Corolla
Running
```

---
