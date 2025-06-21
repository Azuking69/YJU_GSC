"""
가변 인자(*args)와 키워드 인자(**kwargs)를 활용하여 평균, 합계, 최대값, 최소값을 선택적으로 동시에 계산하는 함수를 작성.
"""    
# calculate(*args, **kwargs)를 구현
def calculate(*args, **kwargs):
    # option를 설정
    option_key = ['avg', 'sum', 'max', 'min']
    # args의 요소가 없을때 None
    if not args:
        return None
    # kwargs에 아무 키도 주어지지 않은 경우 None
    if len(kwargs) > len(option_key):
        return None
    
    # 허용되지 않은 키워드가 포함된 경우 None
    for key in kwargs:
        if key not in option_key:
            return None
        
    #args_list에 호출한 값을 저장
    args_list = list(args)
    
    # avg=True: 평균값 계산
    if 'avg' in kwargs and kwargs['avg'] == True:
        avg_total = 0
        for i in args_list:
            avg_total += i
        avg_num = avg_total / len(args_list)
        print_avg = {'avg' : avg_num}
        print_avg
    
    # sum=True: 합계 계산
    if 'sum' in kwargs and kwargs['sum'] == True:
        sum_total = 0
        for j in args_list:
            sum_total += j
        print_sum = {'sum' : sum_total}
        print_sum
        
    #  max=True: 최대값 계산
    if 'max' in kwargs and kwargs['max'] == True:
        for idx, val in enumerate(args_list):
            max_val = args_list[0]
            if idx < 0 and args_list[idx - 1] < args_list[idx]:
                max_val = val
        print_max = {'max' : max_val}
        print_max
    
    # min=True: 최소값 계산
    if 'min' in kwargs and kwargs['min'] == True:
        for idx, val in enumerate(args_list):
            min_val = args_list[0]
            if idx < 0 and args_list[idx - 1] < args_list[idx]:
                min_val = val
            print_min = {'min' : min_val}
            print_min
    
    return
    
    
# 출력: {'avg': 20.0}
print(calculate(10, 20, 30, avg=True))
# 출력: {'sum': 6, 'max': 3}
print(calculate(1, 2, 3, sum=True, max=True))
# 출력: {'min': 50, 'max': 200, 'avg': 116.66666666666667}
print(calculate(100, 50, 200, min=True, max=True, avg=True))
# 출력: None
print(calculate(avg=True))
# 출력: None
print(calculate(1, 2, 3))
# 출력: None
print(calculate(1, 2, 3, total=True))