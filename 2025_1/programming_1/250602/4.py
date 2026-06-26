# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

def foo():
    return 1, "hello", 10.0;

test = foo() #(1, "hello", 10.0)
print(test[0], test[1], test[2]) # 출력
a, b, c = foo()

print(a, b, c) # 출력