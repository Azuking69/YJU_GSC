"""
사용자에게 최대 5번까지 로그인 시도를 허용하며
올바른 아이디와 비밀번호가 입력되면 로그인 성공 메시지를 출력
5번 실패하면 계정 잠금 메시지를 출력
"""

#1 5번 기회
count = 5

#2 while문으로 각 시도에 따라 결과 메시지 출력
# while문
while True:
    #입력
    user_ID = input("ID 입력: ")
    user_Pass = input("PW 입력: ")

    # 로그인 성공
    if user_ID == "user" and user_Pass == "1234":
        print("로그인 성공!")
        # 프로그램 종료
        break
        
    # 로그인 실패
    else:
        # 1번 줄음
        count -= 1
        # 남은 기회 출력
        print(f"ID 또는 PW가 잘못되었습니다. (남은 시도: {count})")

        # 5번 실패할 때 계정 잠금 안내
        if count == 0:
            #출력
            print("계정이 잠금되었습니다.")
            # 프로그램 종료
            break