#1에서 100까지의 범위 내에서 중복되지 않는 랜덤 정수를 생성
#이를 리스트에 저장한 후 사용자가입력한 인덱스에 해당하는 값을 출력

#사용자는 먼저 생성할 랜덤 정수의 개수 N을 입력
import random #モジュールをインポート
N = int(input("N값을 입력하세요(1-100):"))
if N < 1 or 100 < N:
    print("에러: N은 1이상 100이하의 정수여야 합니다.")

#입력받은 N에 따라, 1부터 100까지의 숫자 중 중복되지 않은 N개의 랜덤 숫자를 생성

#1에서 10까시의 램담한 정수를 생성하여 출력
else:
    random_number = []
    while len (random_number) < N: #N個の異なるランダムな整数が追加されるまで繰返,処理を実行
        num = random.randint(1, 100)
        duplicate = 0
        for i in range(len(random_number)):  
            if random_number[i] == num:  # 既存のリスト内と比較
                duplicate = 1  
                break
        if duplicate == 0:
            random_number.append(num)  
#    print("랜덤한 정수 리스트:", random_number)
    print(f"생성된 리스트:{random_number}")

    M = int(input("원하는 원소의 인덱스를 입력하세요(0-4)"))
    if M < 0 or 4 < M :
        print("에러: 유효한 인덱스 범위를 벗어났습니다.")
    else :
        print(f"선택한 인덱스의 원소:{random_number[M]}")

#random_number = random.randint(1, 100) #1-100選ばれる
#print("랜덤한 정수:", random_number)
