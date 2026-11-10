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
