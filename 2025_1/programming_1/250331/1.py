#키보드로부터 3개의 정수를 입력받아 평균을 계산하는 프로그램을 작성한다

#1 정수 입력
num1 = int(input("정수1 입력:"))
num2 = int(input("정수2 입력:"))
num3 = int(input("정수3 입력:"))

#2 평균 계산
avg = round((num1 + num2 + num3) / 3, 2)

#3 출력
print(f"평균:{avg}")