"""
월이 입력될 때 계절 이름이 출력되도록 해보자.
월 : 계절 이름
12, 1, 2 : winter
 3, 4, 5 : spring
 6, 7, 8 : summer
 9, 10, 11 : fall
"""
#1 월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)
month = int(input("월을 의미하는 1개의 정수가 입력된다.(1 ~ 12): "))

#2 계절 이름이 출력
if month == 12 or month == 1 or month == 2:
    print("winter")
elif month == 3 or month == 4 or month == 5:
    print("spring")
elif month == 6 or month == 7 or month == 8:
    print("summer")
elif month == 9 or month == 10 or month == 11:
    print("fall")

season = ["winter", "spring", "summer", "fall", "winter"]
print(season[month//3])