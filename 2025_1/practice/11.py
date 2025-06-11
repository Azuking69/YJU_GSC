"""
사용자로부터 ID, 비밀번호, 보안 질문의 답변을 입력받아 모두 일치하면 
로그인 성공하는 프로그램을 작성
"""
#1 사전 설정
user_ID = "azuki"
user_PW = "7777"
key_question = "당신이 좋아하는 과일은? "
key_answer = "사과"

#2 사용자로부터 ID, 비밀번호, 보안 질문의 답변을 입력받는다
input_ID = input("ID를 입력하세요: ")
input_PW = input("비밀번호를 입력하세요: ")
input_answer = input(key_question)

#3 ID 또는 PW가 틀리면 → “ID 또는 비밀번호가 틀렸습니다.”
if input_ID != user_ID or input_PW != user_PW:
    print("ID 또는 비밀번호가 틀렸습니다.")

#4 보안 질문의 답이 틀리면 → “보안 질문의 답이 틀렸습니다.”
elif input_answer != key_answer:
    print("보안 질문의 답이 틀렸습니다.")

#5 모두 일치하면 → “로그인 성공!”
else:
    print("로그인 성공!")