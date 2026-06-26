import random

# 1. 컴퓨터 난수 생성 (중복 없는 3자리)
computer_numbers = random.sample(range(0, 10), 3)

# 2. 게임 상태 변수
attempts = 0
strike_outs = 0
MAX_ATTEMPTS = 5
MAX_OUTS = 2

print("숫자 맞추기 게임 시작! (0~9 사이 숫자 3개를 ,로 구분하여 입력하세요)")

while True:
    attempts += 1
    user_input = input(f"\n시도 {attempts}: 입력한 숫자 - ")
    player_numbers = list(map(int, user_input.split(',')))

    # 3. 판정 초기화
    strike = 0
    ball = 0

    # 4. Strike & Ball 판정
    for i in range(3):
        if player_numbers[i] == computer_numbers[i]:#リストの１番目（コード上の０）
            strike += 1
        elif player_numbers[i] in computer_numbers:
            ball += 1

    # 5. Out 판정
    if strike == 0 and ball == 0:
        strike_outs += 1
        result = f"결과: {strike} Strike, {ball} Ball, 1 Out"
    else:
        result = f"결과: {strike} Strike, {ball} Ball"

    print(result)

    # 6. 승리 조건
    if strike == 3:
        print("\n게임 종료: 승리")
        print("정답:", *computer_numbers)
        break

    # 7. 패배 조건
    if attempts >= MAX_ATTEMPTS:
        print(f"\n게임 종료: 패배 (시도 횟수 {MAX_ATTEMPTS}회 초과)")
        print("정답:", *computer_numbers)
        break

    if strike_outs >= MAX_OUTS:
        print(f"\n게임 종료: 패배 (스트라이크 아웃 {MAX_OUTS}회 초과)")
        print("정답:", *computer_numbers)
        break