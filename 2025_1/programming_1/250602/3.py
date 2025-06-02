# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

def foo(arg):

    if arg >= 0:
        return arg
    
    print("U should put 0 or posittive integer")
    return

print(foo(1), type(foo(1)))
print(foo(2), type(foo(2)))