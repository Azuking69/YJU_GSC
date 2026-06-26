# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때
# bar 함수 호출    
# bar 함수 정의

# parameter(매개 변수) -> msg
def bar(val1, val2):
    sum = val1 + val2
    avg = sum / 2

    #변환 값으로 합계와 평균을 선택하고 싶다 ... How?
    return sum, avg, 10

value = bar(1, 3)
print(value[0], value[1])

val_sum, val_avg = value
print(val_avg, val_sum)