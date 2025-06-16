"""
여러 개의 정수와 함께 다양한 옵션(키워드 인자)을 입력 받아, 
조건에 따라 합계를 계산하는 함수를 작성.
옵션은 선택 사항이며, 정의되지 않은 옵션이 포함되면 None을 반환.
"""
#1 정의
def add_numbers(*args, **kwargs):
    #2 사용 가능 키를 설정
    vaild_keys = {'abs', 'only_even', 'unique'}
    #3 위에 없는 키의 경우 = None
    for key in kwargs:
        if key not in vaild_keys:
            print(None)
            return

    #4 기본 값 = None    
    use_abs = kwargs.get('abs', False)         #절댓값
    only_even = kwargs.get('only_even', False) #짝수만
    unique = kwargs.get('unique', False)       #중북 제거

    #5 입력 값:args를 리스트화
    result = list(args)

    #6 abs = True의 경우 -> 절댓값으로 변환
    if use_abs:
        result = [abs(x) for x in result]

    #7 only_even = True의 경우 -> 짝수만 남기기
    if only_even:
        result = [x for x in result if x % 2 == 0]

    #8 unique = True의 경우 -> 중북 제거
    if unique:
        result = list(set(result))

    #9 더하기 출력
    print(f"합계는 {sum(result)}")

# 출력: 합계는 -2        
add_numbers(1, -2, 2, -3)

# 출력: 합계는 4 (|-2|=2, |2|=2 -> 2+2)
add_numbers(1, -2, 2, -3, abs=True, only_even=True)

# 출력: 합계는 15 (중북 제거: 1+2+3+4+5)
add_numbers(1, 2, 2, 3, 3, 4, unique=True)

# 출력: None
add_numbers(1, 2, 3, round=True)