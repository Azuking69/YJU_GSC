"""
일급 시민이 될려면 ->
1) 값을 변수에 저장
2) 함수에 매개변수로 전달
3) 함수의 반환 값
"""

def bar(msg):
    print(msg)

# foo = bar 값을 변수에 저장 O
def foo(my_func, msg):
    my_func(msg)
    return my_func

kin = foo(bar, "hello")
kin("하이")