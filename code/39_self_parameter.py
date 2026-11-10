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
