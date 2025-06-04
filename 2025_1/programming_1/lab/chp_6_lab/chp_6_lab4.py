"""
For 문을 사용하여 아래 문자열 내 단어 개수를 출력하는 프로그램을 작성
"""

#1 문자열 작성
myStrings = "It is a great weather with you"

#2 문자를 나누기
words = myStrings.split()

#3 문자 개수를 확인
count = 0
for i in words:
    count += 1

#4 출력
print(f"문자열 단어 갯수: {count}")