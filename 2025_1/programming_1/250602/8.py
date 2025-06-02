# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

# bar 함수 정의
# of parameters: 5개 EA
# Required: 2개 EA -> a, b, c
# Option: 3개 EA -> d, e
def bar(a, b = 10, c, d = 50, e = 60):
    print(a, b, c, d, e)

# bar 함수 호출
bar()