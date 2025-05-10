"""
사용자로부터 입력받은 비밀번호가 안전한지를 검증

비밀번호가 다음 기준을 모두 충족해야 안전하다고 간주
1 비밀번호의 길이가 8자 이상
2 비밀번호에는 적어도 하나의 숫자가 포함
3 비밀번호에는 적어도 하나의 대문자가 포함
"""
import sys

#입력
password = input("비밀번호를 입력하세요: ")

# 문자열 길이 확인하기
if len(password) >= 8:
    #print("비밀번호 길이가 충분합니다.")
    print("비밀번호 길이가 충분합니다.")
else:
    print("비밀번어가 너무 짧습니다.")
    sys.exit()

#문자열에서 숫자 확인하기
has_number = False #下の条件出なかったらF
for char in password:
    if char.isdigit():
        has_number = True
        break #見つけた瞬間にTrue出すと無駄な処理が減る

# 문자열에서 대문자 확인하기
has_uppercase = False #下の条件じゃなかったらF
for char in password:
    if char.isupper():
        has_uppercase = True
        break

#출력
if len(password) >= 8 and has_number and has_uppercase:
    print("비밀번호가 안전합니다.")
else:
    print("비밀번호가 안전하지 않습니다.")
    