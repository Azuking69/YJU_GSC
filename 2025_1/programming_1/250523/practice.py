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
list = []
for val in range(N):
    num = random.randint(A, B)
    list.append(num)
# print(list)

#6 고유 숫자 리스트
num_list = []
for i in list:
    if i not in num_list:
        num_list.append(i)
    else:
        continue
print(num_list)
    
#7 리스트에서 가장 빈도수가 높은 숫자 3개를 찾아 출력


#7 