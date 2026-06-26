# 모듈 사용
import random
# 정답 숫자는 랜덤 함수를 이용
CPU_number = random.randint(1, 100 + 1)

#정답 나올 때까지 반복
while True:
    # 숫자 입력
    input_number = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    # 정답였을 때
    if CPU_number == input_number:
        print("정답입니다!")
        # 반복을 종료
        break
    # 정답 < 입력된 숫자
    elif CPU_number < input_number:
        print("더 작은 숫자입니다.")
    # 정답 > 입력된 숫자
    else:
        print("더 큰 숫자입니다.")