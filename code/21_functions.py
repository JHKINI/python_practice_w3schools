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
