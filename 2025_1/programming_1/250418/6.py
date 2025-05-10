"""
구구단
2 * 1 = 2, 2 * 2 = 4 ... 2 * 9 = 18
........................ 9 * 9 = 81
"""

#단 짝수 단 
for dan in range(2, 8 + 1, 2):
    #1~9 숫자
    for num in range(1, 9 + 1):
        #출력
        print(f"{dan} X {num} = {dan * num}")
    #단마다 나눈다
    print()

#단 짝수 단 
for dan in range(2, 10):
    # 짝수 이면
    if dan % 2 ==0:        
    #1~9 숫자
        for num in range(1, 9 + 1):
        #출력
            print(f"{dan} X {num} = {dan * num}")
    #단마다 나눈다
        print()