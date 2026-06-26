"""
For 문을 사용하여 아래 문자열 내 ‘h’의 개수를 출력하는 프로그램을 작성
"""

#1 입력한 문자
myStrings = "hello hyundai hoho"

#2 list화
list_myStrings = list(myStrings)

#3 h가 있는지 확인
h_char = [character for character in list_myStrings if character == "h"]

#4 h 개수를 확인
h_count = len(h_char)

#5 출력
print("문자열 내 h갯수 :", h_count)