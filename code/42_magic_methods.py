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
