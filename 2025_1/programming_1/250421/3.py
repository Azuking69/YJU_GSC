flag = True
while flag:
    value = int(input("양의 정수를 입력하세요"))

    if value > 0:
        print("입력 값 : ", value)
    else:
        flag = False