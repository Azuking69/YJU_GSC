"""
여러 개의 정수를 받아 곱셈 결과를 반환하는 multiply_numbers() 함수를 작성
단, 다양한 옵션을 키워드 인자(kwargs) 로 입력받아 조건에 따라 결과를 처리
"""
# 여러 개의 정수를 받아 곱셈 결과를 반환하는 multiply_numbers() 함수를 작성
def multiply_numbers(*args, **kwargs):
    # 사용 가능 키
    key_list = {'abs', 'nonzero', 'only_odd'}
    # 사용 불기능 시
    for key in kwargs:
        if key not in key_list:
            return None
    
    # 리스트를 복사
    args_list = list(args)

    # 절댓값 변환하고 계산
    if kwargs.get("abs", False):
        args_list = [abs(x) for x in args_list]

    # 홀수만 곱셈 수행
    if kwargs.get("nonzero", False):
        args_list = [x for x in args_list if x % 2 == 1]

    # 0을 제외하고 곱함
    if kwargs.get("only_odd", False):
        args_list = [x for x in args_list if x != 0]

    #곱셈 결과
    result = 1
    for x in args_list:
        result *= x
    print(result)

# 출력: 곱셈 결과는 -6
multiply_numbers(1, -2, 3)
# 출력: 곱셈 결과는 6
multiply_numbers(1, -2, 3, abs=True)
# 출력: 곱셈 결과는 6
multiply_numbers(0, 1, 2, 3, nonzero=True)
# 출력: 곱셈 결과는 15
multiply_numbers(1, 2, 3, 4, 5, only_odd=True)
# 출력: 계산되지 않습니다. None 반환
multiply_numbers(1, 2, wrong=True)