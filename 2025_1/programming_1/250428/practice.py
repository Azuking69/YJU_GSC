"""
사용자로부터 ID와 비밀번호를 입력받아 로그인 여부를 확인하는 프로그램
"""

# 사전 설정
ID = "admin"
PW = "1234"
# count 정의
count = 0
PW_count = 0 

# while문으로 5회까지 반복
while count < 5:
    #입력
    user_input_ID = input("ID를 입력하세요: ")
    user_input_PW = input("비밀번호를 입력하세요: ")
    # 로그인 성공 시
    if user_input_ID == ID and user_input_PW == PW:
        print("로그인 성공!")
        break

    # ID가 맞지 않으면
    elif user_input_ID != ID:
        count += 1
        #reset
        PW_count = 0
        print(f"등록되지 않은 ID입니다. (남은 시도 {5 - count}회)")

    # ID는 맞지만 비밀번호가 틀리면
    elif user_input_ID == ID and user_input_PW != PW:
        count += 1
        PW_count +=1
        print(f"비밀번호 오류입니다. (남은 시도 {5 - count}회)")
        # 
        if PW_count == 3:
            print("비밀번호를 재설정하세요.")
            break

if count == 5:
    print("계정이 잠금되었습니다.")