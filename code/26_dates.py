import datetime

# 현재 시각 (실행할 때마다 달라짐)
now = datetime.datetime.now()
print(type(now))

# 날짜 만들기
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.year)
print(x.strftime("%A"))

# strftime 형식
y = datetime.datetime(2018, 6, 1)
print(y.strftime("%B"))
print(y.strftime("%Y-%m-%d"))
print(y.strftime("%Y년 %m월 %d일"))

# 날짜 계산
d1 = datetime.date(2026, 1, 1)
d2 = datetime.date(2026, 12, 25)
print((d2 - d1).days)
