"""
For 문을 사용하여 아래 문자열 내 ‘h’의 개수를 출력하는 프로그램
"""
# 문자열
myString = "hello hyundai hoho"
# count 초기화
count = 0
# For 문을 사용하여 아래 문자열 내 ‘h’의 개수를 출력
# 변수 안에 문자를 넣는다
for char in myString:
    # 'h'가 있으면 count
    if char == 'h':
        count += 1
# 결과 출력
print(f"문자열 내 h 갯수 : {count}")