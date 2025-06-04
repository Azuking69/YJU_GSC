"""
사용자로부터 ID와 비밀번호를 입력받아 로그인 여부를 확인하는 프로그램
"""
import sys

#1 사전 설정
user_ID = "admin"
user_PW = "1234"


# ID와 비밀번호를 비교하여 일치 여부를 확인
#2 로그인 시도 횟수가 5회 정의
count = 5
count_PW = 0 

while True:
    #3 사용자로부터 입력을 받는다
    input_ID = input("ID를 입력하세요: ")
    input_PW = input("비밀번호를 입력하세요: ")
    #4 ID가 맞지 않으면
    if input_ID != user_ID:
        count -= 1
        print(f"등록되지 않은 ID입니다. (남은 시도 {count}회)")

        if input_PW != user_PW:
            count_PW = 0

    #5 ID는 맞지만 비밀번호가 틀리면
    elif input_ID == user_ID and input_PW != user_PW:
        count -= 1
        count_PW += 1
        print(f"비밀번호 오류입니다. (남은 시도 {count}회)")
 
    #6 비밀번호가 3회 연속 오류 시
    elif count_PW == 3:
        print("비밀번호를 재설정하세요.")
        sys.exit()

    #7 로그인 시도 횟수가 5회 초과
    elif count == 0:
        print("계정이 잠금되었습니다")  

    #8 로그인 성공 시
    elif input_ID == user_ID and input_PW == user_PW:
        print("로그인 성공!")
        sys.exit()

