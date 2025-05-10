"""
[도서관 이용권 나애를 판별하는 프로그램을 작성]
[어린이 이용권: 12세 이하 어린이 대상]
[청소년 이용권: 13세에서 18세 사이의 청소년 대상]
[성인 이용권: 19세 이상 성인 대상]
"""

#1 이용권 정의
def library_age(age):
    if age < 12:
        msg = "어린이"
        return msg
    elif 13 < age < 18:
        msg = "청소년"
        return msg
    elif 19 < age:
        msg = "성인"
        return msg
    else:
        pass
    
#2 나이 입력  
age = int(input("사용자의 나이를 입력해주세요:"))

#3 결과 출력
msg = library_age(age)
print(f"{msg} 이용권을 사용할 수 있습니다.")
