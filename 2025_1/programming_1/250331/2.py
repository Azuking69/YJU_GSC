#사용자로부터 정수와 실수를 각각 하나씩 입력받아 두 의 차를 계산
#결과 값과 그 자료형을 출력

#1 입력
input_value1 = int(input("정수를 입력하세요:"))
input_value2 = float(input("실수를 입력하세요:"))

#2 차를 계산
difference = input_value1 - input_value2

#3 결과
print(f"차이 : {difference}")
print(f"자료형 :{type(difference)}")