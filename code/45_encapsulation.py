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
