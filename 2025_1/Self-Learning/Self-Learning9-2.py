#사용자로부터 문자열 입력 받기
text = input("문자열을 입력하세요:")

#문자열의 각 문자를 한 글자씩 가져와서 출력하기
for character in text:
    print(character)

#체크수
weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
total = 0

#계산
for i in range(12):
    total += int(text[i]) * weight[i]

#검증번호 계산
digit = ((11 - total) % 11) % 10

#검증번호와 체크
if digit == int(text[-1]):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")
