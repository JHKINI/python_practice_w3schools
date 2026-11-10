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
