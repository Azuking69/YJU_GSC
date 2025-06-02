# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

a = None
print(a is None)

def foo(arg):

    if arg == 1:
        print("arg 1: 함수 종료")
        return
    
    print("arg: ", arg)

    return arg + 1

print(foo(1), type(foo(1)))
print(foo(2), type(foo(2)))