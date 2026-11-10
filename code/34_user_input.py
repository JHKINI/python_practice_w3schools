username = input("Enter username: ")
print("Username is: " + username)

num = input("Enter a number: ")
print(type(num))
num = float(num)
print("The square root is:", num ** 0.5)

# 숫자가 들어올 때까지 다시 입력받기
while True:
    value = input("Enter an integer: ")
    try:
        value = int(value)
        break
    except ValueError:
        print("Wrong input, please try again.")
print("Thank you!", value)
