#사용자로부터 두 개의 입력값을 받습니다
#첫 번째 입력은 정수로,
num1 = int(input("첫 번째 숫자(정수)를 입력하세요:"))
#두 번째 입력은 부동 소수점 수
num2 = float(input("두 번째 숫자(부동 소수점 수)를 입력하세요:"))

#int를 float로 변황
num1_float = float(num1)

#두 수의 합이 100을 초과하는지 검사하는 프로그램을 작성

if num1_float + num2 > 100:
    print(f"합이 100 초과합니다:{num1_float + num2}")
else:
    print(f"합이 100 이하입니다:{num1_float + num2}")
