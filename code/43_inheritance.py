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
