"""
사용자로부터 난수 생성 개수와 범위를 입력받아 리스트에 난수를 저장하고, 
가장 자주 등장한 숫자 3개를 출력하는 프로그램
"""
import random

#1 사용자로부터 다음 3개의 입력을 받는다
#2 N: 생성할 난수의 개수
N = int(input("난수 개수를 입력하세요: "))
#3 A: 난수 발생 시작값
A = int(input("시작 범위를 입력하세요: "))
#4 B: 난수 발생 끝값
B = int(input("끝 범위를 입력하세요: "))

#5 A ~ B 범위의 난수를 N개 생성하여 리스트에 저장한다.
num_list = []
for val in range(N):
    num = random.randint(A, B)
    num_list.append(num)
# print(list)

#6 고유 숫자 리스트
inherent_list = []
for i in num_list:
    if i not in inherent_list:
        inherent_list.append(i)
    else:
        continue
print(f"고유 숫자 리스트: {inherent_list}")

#7 리스트에서 빈도수를 출력
frequency_list = []
for j in inherent_list:
    frequency_list.append(num_list.count(j))
print(f"빈도 숫 리스트: {frequency_list}\n")

#8 리스트에서 가장 빈도수가 높은 숫자 3개를 찾아 출력
top_num = []
top_frequency = []

for _ in range(3):
    if not frequency_list:
        break

    max_value = frequency_list[0]
    for f in frequency_list:
        if f > max_value:
            max_value = f
    
    for i in range(len(frequency_list)):
        if frequency_list[i] == max_value and num_list[i] not in top_num:
            top_num.append(num_list[i])
            top_frequency.append(frequency_list[i])

    #9 最大回数を取り除く（次の最大を探すため）
    i = 0
    while i < len(frequency_list):
        if frequency_list[i] == max_value:
            del frequency_list[i]
            del num_list[i]
        else:
            i += 1

#10 出力
print("가장 많이 등장한 숫자 Top 3 (동점 포함):")
for i in range(len(top_num)):
    print(f"{top_num[i]} → {top_frequency[i]}회")
