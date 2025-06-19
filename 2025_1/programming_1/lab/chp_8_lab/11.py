"""
여러 개의 정수와 함께 다양한 옵션(키워드 인자)을 입력 받아, 
조건에 따라 합계를 계산하는 함수를 작성.
옵션은 선택 사항이며, 정의되지 않은 옵션이 포함되면 None을 반환.
"""
# 함수 정의
def add_numbers(*args, **kwargs):
    # option 정의
    option_list = {'abs', 'only_even', 'unique'}
    # option_list에 없을 때
    for key in kwargs:
        if key not in option_list:
            return None
    
    # list 변화
    args_list = list(args)

    # abs: True일 경우
    if 'abs' in kwargs and kwargs['abs'] == True:
        for idx, val in enumerate(args_list):
            # 모든 숫자를 절댓값으로 변환
            if val < 0:
                args_list[idx] = -val

    # only_even: True일 경우
    if 'only_even' in kwargs and kwargs['only_even'] == True:
        args_list = [val for val in args_list if val % 2 == 0]

    # unique: True일 경우
    if 'unique' in kwargs and kwargs['unique'] == True:
        # 중복을 제거하고 합산
        temp = []
        for val in args:
            if val not in temp:
                temp.append(val)
        args_list = temp

    # 계산
    total = 0
    for x in args_list:
        total += x
    # 출력
    print(total)

# 출력: 합계는 -2        
add_numbers(1, -2, 2, -3)
# 출력: 합계는 4 (|-2|=2, |2|=2 -> 2+2)
add_numbers(1, -2, 2, -3, abs=True, only_even=True)
# 출력: 합계는 15 (중북 제거: 1+2+3+4+5)
add_numbers(1, 2, 2, 3, 3, 4, 5, unique=True)
# 출력: None
print(add_numbers(1, 2, 3, round=True))