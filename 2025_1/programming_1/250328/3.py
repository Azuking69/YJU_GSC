#Truthy, Falsy 예제
temp_1 = 1   #정수형 변수
temp_2 = -1  #정수형 변수
temp_3 = 0   #정수형 변수
temp_4 = -0  #정수형 변수

if temp_1:
    print("참")
else:
    print("거짓")

if temp_2:
    print("참")
else:
    print("거짓")

if temp_3:
    print("참")
else:
    print("거짓")

if temp_4:
    print("참")
else:
    print("거짓")


if 2 > 3:
    print("참")
else:
    print("거짓")

if 2 + 3:
    print("참")
else:
    print("거짓")

bar = True
if bar:
    print("참")
else:
    print("거짓")

if 3 > 5:
    print("참")
else:
    print("거짓")


input_value = input("값을 입력하세요:")

#입력 값이 0 이면 "0 입니다"
#입력 값이 0이 아니면 0이 아니에요~~""
value = int(input_value)
if value == 0:
    print("0 입니다")
else:
    print("0이 아니에요~~")


input_value = int(input("입력 값:"))

#입력 값이 양수이면 "양수" 출력
#입력 값이 음수이면 "음수" 출력
#입력 값이 0이면 "0" 출력
if input_value > 0:
    print("양수")
elif input_value < 0:
    print("음수")
else:
    print("0")


#입력 값이 짝수이면 "짝수" 출력
#입력 값이 홀수이면 "홀수" 출력
#조건식 : input_value % 2 == 0 -> 짝수를 판별하는 조건식
input_value = int(input("입력 값:"))

if input_value % 2 == 0:
    print("짝수")
else:
    print("홀수")


input_value = input("입력 값:") #文字の時はinputだけでOK
#암호를 입력하세요 : "0539405442"
#암호가 일치 할 경우 "로그인 성공"
#암호가 일치 하지 않은 경우 "로그인 실패"

if input_value == "0539405442":
    print("로그인 성공")
else:
    print("로그인 실패")"

    

#사용자로부터 문자 1개를 입력 받습니다.
#그 다음, 사용자로부터 정수 1개를 입력 받습니다.
#입력 받은 문자를 입력 받은 정수만큰 반복 출력합니다.

#실행 예)
#문자 하나를 입력 하세요 : $
#문자를 반복 출력할 정수를 임력하세요 : 5
#print("h" * 10)#hhhhhhhhhh
#출력 결과 : $$$$$

input_character = input("문자 하나를 입력 하세요 :")
input_value = int(input("문자를 반복 출력할 정수를 임력하세요 :"))
result = input_character * input_value
print(result)



#정사각형의 면적을 구하세요

#가로 또는 섀로의 길이를 입력 : 5
size_of_rect = int(input("가로 또는 세로의 길이:"))

#정사각형의 면적 : 5 * 5 -> 25
print(size_of_rect * size_of_rect)
