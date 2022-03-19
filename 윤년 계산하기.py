##2019038042 이도경
year=int(input("연도 입력:"))

if year % 4 == 0 and year % 100 != 0:
    print("%d년은 윤년입니다." %year)
elif year % 400 == 0:
    print("%d년은 윤년입니다." %year)
else:
    print("%d년은 윤년이 아닙니다." %year)