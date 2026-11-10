thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist[0])
print(thislist[-1])
print(thislist[1:3])

# 값 변경
thislist[1] = "blackcurrant"
print(thislist)

# 추가
thislist.append("orange")
thislist.insert(1, "lemon")
print(thislist)

tropical = ["mango", "pineapple"]
thislist.extend(tropical)
print(thislist)

# 삭제
thislist.remove("lemon")
thislist.pop()          # 마지막 삭제
del thislist[0]
print(thislist)

# 반복
for x in thislist:
    print(x)

# 리스트 컴프리헨션
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# 정렬
nums = [100, 50, 65, 82, 23]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# 복사 & 합치기
copy_list = fruits.copy()
print(copy_list)
print([1, 2] + [3, 4])
