# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

# bar 함수 정의
# of parameters: 5개 EA
# Required: 2개 EA -> a, b, c
# Option: 3개 EA -> d, e
def plot(x, y, c = "red", w = "1", m = None):
    print(x, x, c, w, m)

# bar 함수 호출
plot(2, 3)
plot(2, 3, w = "2")
plot(2, 3, w = "2", m = 'o', c = "red")