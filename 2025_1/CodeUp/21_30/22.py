"""
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
"""
#1 6자리의 연월일(YYMMDD)을 입력
user_birth = input("연월일(YYMMDD)을 입력: ")

#2 나누어 출력
i = 0
for _ in range(len(user_birth)):
    print(user_birth[i : i + 2], end=" ")
    i += 2