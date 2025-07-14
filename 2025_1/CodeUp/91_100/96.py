"""
바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
"""
#1 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력
boad = []
for _ in range(19):
    boad.append(list(map(int, input("19 * 19 크기의 정수값으로 입력: ").split())))

#2 십자 뒤집기 횟수(n)가 입력
n = int(input("십자 뒤집기 횟수 입력: "))

#3 십자 뒤집기 좌표가 횟수(n) 만큼 입력
for _ in range(n):
    x, y = input("좌표가 횟수 입력: ").split()
    x = int(x) - 1
    y = int(y) - 1

    #4 십자 뒤집기 결과를 출력
    for i in range(19):
        #5 0 -> 1
        if boad[i][int(y)] == 0:
            boad[i][int(y)] = 1
        else:
            boad[i][int(y)] = 0

        #6 1 -> 0
        if boad[int(x)][i] == 1:
            boad[int(x)][i] = 0
        else:
            boad[int(x)][i] = 1
        
#7 출력
for i in range(19):
    print(' '.join(map(str, boad[i])))