"""
영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.
"""
#2 'q'가 입력될 때까지 반복
while True:
    #1 소문자 입력
    word = input("영문 소문자 입력: ")

    #3 입력한 문자를 계속 출력
    if word == "q":
        print(word)
        break
    else:
        print(word)
        continue