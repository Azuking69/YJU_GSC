"""
빙고 게임 프로그램 작성
"""
import random

while True:

    #1 입력 받기
    #1-1 사용자로부터 크기 N을 입력받는다
    user_N = int(input("Enter the size of the bingo board (3 to 6): "))

    #1-2 유효하지 않은 값이 입력될 경우, 올바른 값이 입력될 때까지 재입력
    if user_N < 3 or 6 < user_N:
        print("Size must be between 4 and 6. Please try again.")
    
    #2 빙고 보드 생성
    else:
        print("Initial Bingo Board:")
        #2-1 N x N 크기의 빙고 보드를 위해 1차원 리스트를 생성
        num_list = []
        while len(num_list) < user_N ** 2:
            n = random.randint(1, 36)
            if n not in num_list:
                num_list.append(n)
        #2-2 이 리스트는 1부터 36 사이의 중복되지 않은 정수로 채워진다  
        for i in range(user_N):
            for j in range(user_N):
                #3 보드 출력
                print(f"{num_list[i * user_N + j]:>2}", end=" ")
            print()
        break

#4 난수 발생 및 게임 진행
#4-1 사용자가 엔터 키를 누르면, 1부터 36사이 난수를 발생시키고 화면에 출력
count = 0
while True:
    input("Please Enter to generate a random number: ")
    cpu_num = random.randint(1, 36)
    count += 1
    print(f"Random Number {count}: {cpu_num}")

    #4-2 화면에 출력된 난수와 일치하는 보드 상의 숫자는 *로 대체된다
    for i in range(len(num_list)):
        if num_list[i] == cpu_num:
            num_list[i] = "*"
    
    #4-3 매 난수 발생 시 게임 실행 횟수를 출력
    for i in range(user_N):
        for j in range(user_N):
            print(f"{str(num_list[i * user_N + j]):>2}", end=" ")
        print()

    #5 빙고 확인
    #5-1 보드에서 가로, 세로, 또는 대각선(양방향)을 포함하여, 최소 2개 이상의
    #    줄에서 모든 숫자가 *로 대체되면 빙고가 성립
    bingo_count = 0

    #5-1-1 세로
    for i in range(user_N):
        start = i * user_N
        end = start + user_N
        row = num_list[start:end]

        if all(cell == "*" for cell in row):
            bingo_count += 1
    
    #5-1-2 가로
    for j in range(user_N):
        col = [num_list[i * user_N + j] for i in range(user_N)]
        if all (cell == "*" for cell in col):
            bingo_count += 1
    
    #5-1-3 대각선
    if all(num_list[i * user_N + j] == "*" for i in range(user_N)):
        bingo_count += 1
    
    #5-1-4 양방향
    if all(num_list[i * user_N + (user_N - 1 - i)] == "*" for i in range(user_N)):
        bingo_count += 1

    #5-2 2개 이상의 빙고 줄이 완성되면 사용자가 승리
    if bingo_count >= 2:
        print("Congratulations! You've won the game with 2 or more bingos!")
        break