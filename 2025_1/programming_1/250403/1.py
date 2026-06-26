#정수 한 개를 입력 받아
#홀수 이면 -> "홀수 입니다."
#짝수 이면 -> "짝수 입니다."
#를 출력하는 함수를 작성하시오

#함수 정의
def prt_even_odd(arg_input):
    msg = ""
    #짝수이면 
    if arg_input % 2 == 0:
        msg = "짝수"

    #홀수이면면
    else:
        msg = "홀수"

    print(f"{msg}입니다.")

#정의된 호출
prt_even_odd(2) # -> "짝수 입니다"
prt_even_odd(3) # -> "홀수 입니다"