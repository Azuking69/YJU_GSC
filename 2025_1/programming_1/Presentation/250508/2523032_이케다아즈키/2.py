"""
While문을 사용하여 1~1000까지의 정수 중 3의배수의 총합을 구하라
"""
# count, result 초기화
count = 0
result = 0
# While문을 사용하여 1~1000까지의 정수 중 3의배수의 총합
# 1000 까지 정의
while count < 1000:
    # 1 개씩 늘다
    count += 1
    # 3의배수의 총합
    if count % 3 == 0:
        result += count
# 결과 출력
print(result)