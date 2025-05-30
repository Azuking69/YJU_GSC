# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

def bar():
    # foo 값을 변경해서 실행 해 볼것
    foo = 1
    
    if foo < 0:
        return
    
    if foo == 1:
        return 1
    
    else:
        return 2

# 1    
print(bar())

def get_input_num():
    msg = "정수를 입력하세요"
    input_val = int(input(msg))
    return input_val

values = [get_input_num() for _ in range(3)]
print(values)