fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x, end=" ")
print()

print("--- break ---")
for x in fruits:
    if x == "banana":
        break
    print(x)

print("--- continue ---")
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("--- else ---")
for x in range(3):
    print(x)
else:
    print("Finally finished!")

print("--- 중첩 반복 ---")
adj = ["red", "big"]
fruits = ["apple", "banana"]
for a in adj:
    for f in fruits:
        print(a, f)
