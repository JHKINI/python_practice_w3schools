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
