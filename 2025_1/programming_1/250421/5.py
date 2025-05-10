"""
입력값이 양수가 아닐 경우,
에러 메시지 출력 후 재입력
양수를 입력 받을 때 까지지
"""
while True: #True의 사이
    input_value = int(input("정수 입력: "))
    
    #양의 정수인 경우, 반복 종료
    if input_value > 0:
        break

    print("양의 정수를 입력하세요")

print("bar")
