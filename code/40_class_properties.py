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
