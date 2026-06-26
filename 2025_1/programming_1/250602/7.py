# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

# bar 함수 정의
# of parameters: 5개 EA
# Required: 2개 EA -> a, b
# Option: 3개 EA -> c, d, e
def bar(a, b, c = 40, d = 50, e = 60, f = 70, g = 80, i = 90):
    print(a, b, c, d, e)

# bar 함수 호출
bar(b = 10, a = 20, e = 100)
bar(b = 20, 1000)