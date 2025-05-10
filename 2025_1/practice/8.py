"""
미리 정의된 여러 개의 ID와 각각의 
    비밀번호(admin / 1234, guest / 0000, user / pass)를 저장
사용자에게 최대 5번까지 로그인 시도를 허용
올바른 ID와 해당하는 PW가 입력되면 로그인 성공 메시지와 
    함께 어떤 계정으로 로그인했는지 출력
5번 실패하면 계정 잠금 메시지를 출력
"""

#1 ID, PW 리스트화
ID_PassWord = {"admin" : "1234", 
               "guest" : "0000", 
               "user" : "pass"}

#2 5회 기회
count = 5

#3 실패 할 때 반복
while True:
    #4 입력
    input_ID = input("ID 입력: ")
    input_PW = input("PW 입력: ")

    #5 성공 조건
    if input_ID in ID_PassWord and input_PW == ID_PassWord[input_ID]:
        print(f"{input_ID}으로 로그인 성공!")
        break

    #6 실패 조건
    else:
        count -= 1
        print(f"오류: ID 또는 PW가 잘못되었습니다. (남은 시도: {count})")
        #7 5회 실패 하면
        if count == 0:
            print("계정 잠금되었습니다.")
            break