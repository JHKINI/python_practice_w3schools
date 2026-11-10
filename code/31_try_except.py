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
