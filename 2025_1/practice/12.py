"""
미리 등록된 여러 사용자 정보를 기반으로 ID와 비밀번호를 비교하여 
로그인 여부를 판단하는 프로그램을 작성
"""
#1 조건
users = {
    "azuki" : "1234",
    "saki" : "5678",
    "taro" : "9999"
}

#2 입력 받는다
input_ID = input("ID를 입력하세요: ")
input_PW = input("비밀번호를 입력하세요: ")

#3 ID와 비밀번호를 비교하여 로그인 여부를 판단
#4 로그인 성공 시
if input_ID in users and input_PW == users[input_ID]:
    print("로그인 성공!")

#5 로그인 실폐 시
else:
    print("ID 또는 비밀번호가 틀렸습니다.")