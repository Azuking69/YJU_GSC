"""
주어진 수치 데이터(리스트)를 기반으로 편차, 분산, 표준편차(偏差、分散、標準偏差)를
직접 계산하는 프로그램
"""
import random
import math

#1 사용자로부터 리스트의 개수를 입력받는다
list_num = int(input("리스트 개수를 입력하세요(5~20): "))

#2 입력받은 개수는 반드시 5 이상 20 이하여야 하며, 
# 범위를 벗어날(脱け出す) 경우 에러 메시지를 출력하고 종료한다
if list_num < 5 or 20 <= list_num:
    print("오류: 5~20 사이의 숫자를 입력하세요.")

#3 list화
else:
    random_num_list = [random.randint(1, 100) for _ in range(list_num)]
    # for文で繰り返しながら、その結果をリストとしてまとめる
    # randomtとforの間は半角スペースで区切る

#4 모든 값을 더해서 개수로 나눈 값
    # 変数をリセット
    num_total = 0
    # valに順番にランダム生成された数字を入れていく
    for val in random_num_list:
        num_total += val
        # 결과 출력
        mean = num_total / list_num

#5 각 수가 평균과 얼마나 차이 나는지 나타내는 값
    deviations = []
    for val in random_num_list:
        # 平均（mean）を引いたもの（偏差）
        deviations.append(val - mean)
    
#6 편차들을 제곱해서 평균 낸 것
    # 分散の合計を初期化（最初はゼロ）
    variance = 0
    # リストをひとつずつ取り出す
    for d in deviations:
        #  各偏差を2乗（= 偏差²）
        variance += d**2
    # 最後に個数で割って平均を取る
    variance /= list_num

#7 분산의 제곱근을 씌운 값
    # 分散（variance）から標準偏差（standard deviation）を計算
    std_dev = math.sqrt(variance)

#8 출력
print("\n생성된 리스트: ", random_num_list)
print("평균: ", round(mean, 2))
print("편차: ", [round(d, 2) for d in deviations])
print("분산: ", round(variance, 2))
print("표준편차: ", round(std_dev, 2))