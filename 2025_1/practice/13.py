"""
3회까지 로그인 시도 가능하며, 각 시도마다 “처리 중...”이라는 메시지와 함께 
3초 지연을 두고 결과를 알려주는 프로그램을 작성
"""
import time

#1 설정
user_ID = "azuki"
user_PW = "1234"
count = 3

#2 3회까지 로그인 시도 가능한 입력
while count > 0:
    input_ID = input("ID를 입력하세요: ")
    input_PW = input("비밀번호를 입력하세요: ")

    #3 처리 중 출력
    print("처리 중...", end=" ")
    for i in range(3, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    print()

    #4 로그인 성공 시
    if input_ID == user_ID and input_PW == input_PW:
        print("로그인 성공!")
        break

    #5 로그인 실패 시
    else:
        count -= 1
        print(f"로그인 실패! 남은 시도 횟수: {count}")

#6 3회 실수 하면
if count == 0:
    print("계정이 잠금 처리되었습니다.")