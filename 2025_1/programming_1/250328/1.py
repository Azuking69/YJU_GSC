#입력 값이 3의 배수이면 "3의 배수 입니다"
#입력 값이 4의 배수이면 "4의 배수 입니다"
#그 이외에는 아무것도 출력허지 않음

#3의 배수를 확인하는 조건식 -> input_value % 3 ==0
#4의 배수를 확인하는 조건식 -> input_value % 4 ==0

input_value = int(input("입력 값:"))

if input_value % 3 == 0:
    print("3의 배수 입니다")

elif input_value % 4 == 0:
    print("4의 배수 입니다")


if input_value % 3 == 0:
    pass #출력 하지 않음

if input_value % 4 == 0: #上のifとの関係性がなくなる
    pass
    