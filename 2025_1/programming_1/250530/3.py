# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

def get_input_num():
    msg = "정수를 입력하세요"
    input_val = int(input(msg))

    if input_val < 0:
        print("0과 양의 정수만 입력하세요")

    return input_val

value = get_input_num()
print(value, type(value))