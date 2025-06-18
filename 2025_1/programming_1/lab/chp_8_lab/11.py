"""
여러 개의 정수와 함께 다양한 옵션(키워드 인자)을 입력 받아, 
조건에 따라 합계를 계산하는 함수를 작성.
옵션은 선택 사항이며, 정의되지 않은 옵션이 포함되면 None을 반환.
"""
# 함수 정의
def add_numbers(*args, **kwargs):
    # 사용하는 키를 저장
    option_key = {'abs', 'only_even', 'unique'}

    # option_key 안에 없는 것은 다 None
    for check_key in kwargs:
        if check_key not in option_key:
            return None
        
    #list를 복사
    args_list = list(args)

    # option : abs
    if 'abs' in kwargs and kwargs['abs'] == True:
        for idx, val in enumerate(args_list):
            # 숫자가 마이너스이라면 마이너스를 곱셈
            if val < 0:
                args_list[idx] = -val

    # option : only_even
    if 'only_even' in kwargs and kwargs['only_even'] == True:
        args_list = [x for x in args_list if x % 2 == 0]

    # option : unique
    if 'unique' in kwargs and kwargs['unique'] == True:
        temp = []
        for val in args_list:
            if val not in temp:
                temp.append(val)
        args_list = temp

    # 변수 초기화
    total = 0
    # 합계
    for val in args_list:
        total += val

    # 출력
    print(f"합계는 {total}입니다.")

# 출력: 합계는 -2        
add_numbers(1, -2, 2, -3)
# 출력: 합계는 4 (|-2|=2, |2|=2 -> 2+2)
add_numbers(1, -2, 2, -3, abs=True, only_even=True)
# 출력: 합계는 15 (중북 제거: 1+2+3+4+5)
add_numbers(1, 2, 2, 3, 3, 4, 5, unique=True)
# 출력: None
print(add_numbers(1, 2, 3, round=True))