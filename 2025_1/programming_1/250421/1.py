"""
사용자에게 최대 5번까지 로그인 시도를 허용
올바른 아이디와 비밀번호가 입력되면 로그인 성공 메시지를 출력
5번 실패하면 계정 잠금 메시지를 출력
"""
#5회 기회
count = 5

while True:
    # 반복적으로 사용자로부터 ID와 비밀번호를 입력
    input_id = input("ID 입력: ")
    input_pw = input("PW 입력: ")

    #어느쪽이 틀릴 경우
    if input_id not in "admin" or input_pw != "1234": 
        #회수가 한번 줄음
        count -= 1
        #결과, 나머지 회수 출력
        print(f"ID 또는 PW가 잘못되었습니다.(남은 시도: {count})")
        print() #改行
        # 5회 실패 시
        if count == 0:
            print("계정이 잠금되었습니다.")
            break
    

# 두 개 맞을 경우
    elif input_id == "admin" and input_pw == "1234":
        print("로그인 성공")
        break