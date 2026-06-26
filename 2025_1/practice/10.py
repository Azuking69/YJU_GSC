"""
사용자로부터 ID와 기존 비밀번호를 입력받고, 일치하면 새 비밀번호를 
등록할 수 있는 프로그램을 작성
"""
count = 3

#1 사전 설정: ID = user, 기존 비밀번호 = abc123
user_ID = "user"
old_user_PW = "abc123"

while count > 0: 
    #2 사용자로부터 ID와 기존 비밀번호를 입력받는다
    input_ID = input("ID를 입력하세요: ")
    input_PW = input("비밀번호를 입력하세요: ")

    #3 모두 일치하면 → 새 비밀번호를 입력받고, 
    #  비밀번호 확인 입력까지 받는다다
    if input_ID == user_ID and input_PW == old_user_PW:
        new_user_PW = input("새로운 비밀번호를 입력하세요: ")
        check_PW = input("확인하기 위해 다시 입력하세요: ")

        #4 일치해야 변경 완료
        if new_user_PW == check_PW:
            print("변경 완료!")
            break
        #5 비밀번호 확인이 일치하지 않으면 다시 입력
        else:
            print("새로운 비밀번호가 일치하지 않습니다. 다시 입력하십시오.")
            count -= 1
   
    #6 ID가 틀리면 → “등록되지 않은 ID입니다.”
    elif input_ID != user_ID:
        print("등록되지 않은 ID입니다.")
        count -= 1

    #7 비밀번호가 틀리면 → “비밀번호가 일치하지 않습니다.”
    else:
        print("비밀번호가 일치하지 않습니다.")
        count -= 1

    #8 3회 실패 시 “비밀번호 변경 실패” 출력 후 종료
    if count == 0:
        print("비밀번호 변경 실패.")