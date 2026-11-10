price = 59
txt = f"The price is {price} dollars"
print(txt)

# 소수점 2자리
txt = f"The price is {price:.2f} dollars"
print(txt)

# 계산식도 넣을 수 있다
print(f"The price is {20 * 59} dollars")

# 천 단위 쉼표
print(f"The price is {59000:,} dollars")

# 조건식
price = 49
print(f"It is very {'Expensive' if price > 50 else 'Cheap'}")

# 함수 호출
fruit = "apples"
print(f"I love {fruit.upper()}")

# format() 메서드
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
